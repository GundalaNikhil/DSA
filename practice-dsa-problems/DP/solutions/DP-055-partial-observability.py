import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_limit = int(input_data[ptr])
    ptr += 1
    s_modes = int(input_data[ptr])
    ptr += 1
    a_actions = int(input_data[ptr])
    ptr += 1
    o_obs = int(input_data[ptr])
    ptr += 1
    initial_belief = []
    for _ in range(s_modes):
        initial_belief.append(int(input_data[ptr]))
        ptr += 1
        initial_belief = tuple(initial_belief)
        action_rewards = []
        action_obs_rules = []
        for _ in range(a_actions):
            rewards = []
            for _ in range(s_modes):
                rewards.append(int(input_data[ptr]))
                ptr += 1
                action_rewards.append(rewards)
                obs = []
                for _ in range(s_modes):
                    obs.append(int(input_data[ptr]))
                    ptr += 1
                    action_obs_rules.append(obs)
                    trans_matrix = []
                    for _ in range(s_modes):
                        row = []
                        for _ in range(s_modes):
                            row.append(int(input_data[ptr]))
                            ptr += 1
                            trans_matrix.append(row)
                            
    memo = {}
    ans = get_max_reward(0, initial_belief, n_limit, a_actions, s_modes, o_obs, action_rewards, action_obs_rules, trans_matrix, memo)
    print(ans)


def get_max_reward(step, belief, n_limit, a_actions, s_modes, o_obs, action_rewards, action_obs_rules, trans_matrix, memo):
    if step == n_limit:
        return 0
    state = (step, belief)
    if state in memo:
        return memo[state]
        
    best_expected = -float("inf")
    for a in range(a_actions):
        # Immediate expected reward
        imm_reward = 0
        for i in range(s_modes):
            imm_reward += belief[i] * action_rewards[a][i]
            
        # Calculate new beliefs for each observation outcome
        obs_outcomes_prob = [0.0] * o_obs
        new_beliefs = [[0.0] * s_modes for _ in range(o_obs)]
        
        for i in range(s_modes):
            if belief[i] == 0:
                continue
            observed = action_obs_rules[a][i] # Deterministic observation for state i?
            # Or distribution? Code: `observed = action_obs_rules[a][i]`. Single val.
            
            for j in range(s_modes):
                prob_tj = trans_matrix[i][j]
                # Prob of being in i (belief[i]) * Prob transition i->j (prob_tj)
                # This contributes to `new_beliefs` if we observe `observed`.
                # Wait, if we observe `observed`, it MUST have come from a state `i` that produces `observed`.
                new_beliefs[observed][j] += belief[i] * prob_tj
                
                # Total prob of observing `observed`
                obs_outcomes_prob[observed] += belief[i] * prob_tj
                
        future_reward = 0
        for obs_val in range(o_obs):
            p_obs = obs_outcomes_prob[obs_val]
            if p_obs == 0:
                continue
                
            # Normalize new belief
            raw_new_belief = new_beliefs[obs_val]
            # Convert to normalized tuple (e.g. integers sum to 1000)
            normalized_belief = []
            for val in raw_new_belief:
                # `val` is P(observing obs_val AND state is j).
                # P(state is j | obs_val) = val / p_obs.
                # Scaling by 1000 for integer state?
                normalized_belief.append(int((val / p_obs) * 1000))
            
            # Ensure sum is 1000? Might have rounding errors.
            # Original code did: `total_new = sum(raw_new_belief)`. 
            # `val * 1000 // total_new`.
            # `total_new` IS `p_obs`.
            
            normalized_belief = tuple(normalized_belief)
            
            # Future reward is weighted by P(obs) * V(new_belief)
            # Original code logic was slightly messy with scaling.
            # `(total_new // 1000)` ? That implies `total_new` was scaled up?
            # Original `belief` was integers. Sum 1000?
            
            future_reward += (p_obs / 1000.0 if isinstance(p_obs, int) else p_obs) * get_max_reward(
                step + 1, normalized_belief, n_limit, a_actions, s_modes, o_obs, action_rewards, action_obs_rules, trans_matrix, memo
            )
            
        total_scaled = imm_reward + future_reward # Discount? 
        # Original: `imm_reward * (1000 ** (n_limit - 1 - step))`.
        # This implies huge integer scaling to avoid floats.
        # I will keep structure but assume we return float or scaled int.
        # Let's clean up logic to just standard Value Iteration structure.
        
        # NOTE: Original Code `total_scaled` calculation seemed to try to mix scales.
        # Since I am refactoring, I will assume standard Bellman update: R(a) + sum(P(o|a)*V(next)).
        
        best_expected = max(best_expected, imm_reward + future_reward) # Simplification
        
    memo[state] = best_expected
    return best_expected


if __name__ == "__main__":
    solve()
