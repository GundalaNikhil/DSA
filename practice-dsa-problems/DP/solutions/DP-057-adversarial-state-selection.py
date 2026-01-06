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
    actions_per_state = [[[] for _ in range(a_actions)] for _ in range(s_states + 1)]
    for i in range(a_actions):
        k = int(input_data[ptr])
        ptr += 1
        for _ in range(k):
            u = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            r = int(input_data[ptr])
            ptr += 1

            actions_per_state[u][i].append((v, r))
            
    dp = [[0] * (s_states + 1) for _ in range(n + 1)]
    
    for s_step in range(n - 1, -1, -1):
        for u in range(1, s_states + 1):
            best_action_val = -float("inf")
            found_action = False
            
            for i in range(a_actions):
                outcomes = actions_per_state[u][i]
                if not outcomes:
                    continue
                found_action = True
                worst_outcome_val = float("inf")
                
                # Adversary chooses v to minimize reward
                for v, r in outcomes:
                    worst_outcome_val = min(
                        worst_outcome_val, r + dp[s_step + 1][v]
                    )
                best_action_val = max(best_action_val, worst_outcome_val)
                
            if found_action:
                dp[s_step][u] = best_action_val
            else:
                dp[s_step][u] = -float("inf")
                
    ans = dp[0][1]
    print(ans if ans != -float("inf") else -1)


if __name__ == "__main__":
    solve()
