import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    tr = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        actions.append((int(input_data[ptr]), int(input_data[ptr + 1])))
        ptr += 2
        
    inf = float("inf")
    dp = [[-inf] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    # dp[s][tc] = max reward after s steps with tc technical capability?
    # tc likely capped at s or some limit.
    # Code `tc in range(s + 1)`.
    
    for s in range(1, n + 1):
        for tc in range(s + 1):
            # Option 1: Just progress, no action used?
            # Or `dp[s][tc]` comes from `dp[s-1][tc-1]` + tr (if tc > 0)
            # tr is tech reward/increment?
            
            if tc > 0 and dp[s - 1][tc - 1] != -inf:
                dp[s][tc] = max(dp[s][tc], dp[s - 1][tc - 1] + tr)
                
            # Option 2: Use action
            # Actions require `req`. Give `r`.
            # If we use action, do we change `tc`?
            # Code: `dp[s][tc] = max(..., dp[s-1][tc] + best_act)`
            # So tc doesn't change if we pick action? But we need tc >= req.
            # And `best_act` is max reward among all available actions for this `tc`.
            # Note: `best_act` calc was nested inside loop in original code, which is inefficient but correct logic-wise if actions are small.
            # But here `best_act` depends on `tc`.
            
            best_act = -inf
            for r, req in actions:
                if tc >= req:
                    best_act = max(best_act, r)
                    
            if best_act != -inf and dp[s - 1][tc] != -inf:
                dp[s][tc] = max(dp[s][tc], dp[s - 1][tc] + best_act)
                
    ans = max(dp[n])
    print(ans if ans != -inf else 0)


if __name__ == "__main__":
    solve()
