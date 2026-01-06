import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_steps = int(input_data[ptr])
    ptr += 1
    g_groups = int(input_data[ptr])
    ptr += 1
    group_state_rewards = []
    for _ in range(g_groups):
        s_count = int(input_data[ptr])
        ptr += 1
        rewards = []
        for _ in range(s_count):
            rewards.append(int(input_data[ptr]))
            ptr += 1
            group_state_rewards.append(rewards)
            group_multipliers = []
            for _ in range(g_groups):
                mults = []
                for _ in range(n_steps):
                    mults.append(int(input_data[ptr]))
                    ptr += 1
                    group_multipliers.append(mults)
            group_multipliers.append(mults)
            
    # Precalculate MAX base reward for each group
    # Logic: `group_max_base[g] = max(rewards)`
    group_max_base = [
        max(rewards) if rewards else 0
        for rewards in group_state_rewards
    ]
    
    dp = {}
    dp[tuple([0] * g_groups)] = 0
    # State: counts[g] is number of times group g has been used?
    # Max steps: n_steps.
    # Total steps used = sum(counts). Should be equal to step index?
    # Original code: `for _ in range(n_steps):` loop.
    
    for _ in range(n_steps):
        new_dp = {}
        for counts, current_reward in dp.items():
            for g in range(g_groups):
                # Using group g
                new_counts = list(counts)
                new_counts[g] += 1
                new_counts = tuple(new_counts)
                k = counts[g]
                
                # Check multiplier index
                # If we used group g 'k' times already, next use is at index k?
                # Multipliers array size: `group_multipliers[g]` has n_steps items.
                # If k < n_steps:
                if k < n_steps:
                    reward_gain = group_max_base[g] * group_multipliers[g][k]
                    
                    if (
                        new_counts not in new_dp
                        or new_dp[new_counts] < current_reward + reward_gain
                    ):
                        new_dp[new_counts] = current_reward + reward_gain
        dp = new_dp
        
    ans = -float("inf")
    for val in dp.values():
        if val > ans:
            ans = val
            
    print(ans if ans != -float("inf") else 0)


if __name__ == "__main__":
    solve()
