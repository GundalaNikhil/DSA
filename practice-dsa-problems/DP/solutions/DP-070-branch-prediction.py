import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k_strats = int(input_data[ptr])
    ptr += 1
    c_switch = int(input_data[ptr])
    ptr += 1
    outcomes_str = input_data[ptr]
    ptr += 1
    outcomes = [int(x) for x in outcomes_str]
    strategies = []
    for _ in range(k_strats):
        s_count = int(input_data[ptr])
        ptr += 1
        preds = []
        for _ in range(s_count):
            preds.append(int(input_data[ptr]))
            ptr += 1
            next_states = []
            for _ in range(s_count):
                s0 = int(input_data[ptr])
                ptr += 1
                s1 = int(input_data[ptr])
                ptr += 1
                next_states.append((s0, s1))
            strategies.append((s_count, preds, next_states))

            
    curr_states = [0] * k_strats
    # dp[i]: cost if we are CURRENTLY using strategy i
    # Init: 0? Code: `dp = [0] * k_strats`.
    dp = [0] * k_strats
    
    for t in range(n):
        outcome = outcomes[t]
        new_dp = [float("inf")] * k_strats
        
        # Current predictions of all strategies
        current_preds = [strategies[i][1][curr_states[i]] for i in range(k_strats)]
        
        min_prev_dp = min(dp)
        
        for i in range(k_strats):
            # Option 1: Stay in i
            # Cost = dp[i] + miss_penalty(i)
            mis = 1 if current_preds[i] != outcome else 0
            stay_cost = dp[i] + mis
            
            # Option 2: Switch to i from any best j
            # Cost = min(dp) + switch_cost + miss_penalty(i)
            # Wait, if we switch TO i, we pay switch cost.
            # Then we use strategy i for THIS prediction? Or next?
            # Problem typically: predict, observe, update.
            # If we switch, we switch BEFORE predict?
            # Code: `min_prev_dp + c_switch + mis`. So yes, switch before predict.
            
            switch_cost = min_prev_dp + c_switch + mis
            
            new_dp[i] = min(stay_cost, switch_cost)
            
        # Update internal states of strategies
        # They update based on outcome REGARDLESS of whether we used them?
        # "Branch Prediction": usually all predictors run parallel.
        for i in range(k_strats):
            curr_states[i] = strategies[i][2][curr_states[i]][outcome]
            
        dp = new_dp
        
    print(min(dp))


if __name__ == "__main__":
    solve()
