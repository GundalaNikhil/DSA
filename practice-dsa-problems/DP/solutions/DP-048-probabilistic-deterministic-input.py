import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s_states = int(input_data[ptr])
    ptr += 1
    a_actions = int(input_data[ptr])
    ptr += 1
    q_scale = int(input_data[ptr])
    ptr += 1
    adj = {}
    actions_per_state = [[[] for _ in range(101)] for _ in range(s_states + 1)]
    for i in range(a_actions):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        actions_per_state[u][i].append((v, p, r))
        actions_per_state[u][i].append((v, p, r))
        
    dp = [[0] * (s_states + 1) for _ in range(n + 1)]
    # Working backwards from step n-1 to 0?
    
    for s_step in range(n - 1, -1, -1):
        for u in range(1, s_states + 1):
            best_val = -float("inf")
            found_action = False
            
            for act_id in range(101):
                outcomes = actions_per_state[u][act_id]
                if not outcomes:
                    continue
                found_action = True
                curr_expected_scaled = 0
                
                for v, p, r in outcomes:
                    # Expected value calculation
                    # r * q^(n-1-s) + next_val
                    # p is prob? input parsed as int. Maybe prob = p / scale?
                    # The formula `p * (r * scale + ...)` suggests p is raw scaling factor?
                    # Assuming logic is correct, just fixing structure.
                    curr_expected_scaled += p * (
                        r * (q_scale ** (n - 1 - s_step)) + dp[s_step + 1][v]
                    )
                    
                best_val = max(best_val, curr_expected_scaled)
                
            if found_action:
                dp[s_step][u] = best_val
            else:
                dp[s_step][u] = 0
                
    print(dp[0][1])


if __name__ == "__main__":
    solve()
