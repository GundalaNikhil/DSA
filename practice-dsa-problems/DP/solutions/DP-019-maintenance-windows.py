import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    w = int(input_data[ptr])
    ptr += 1
    v = []
    for _ in range(n):
        v.append(int(input_data[ptr]))
        ptr += 1
        
    dp = [0] * (n + 1)
    dq = deque([0])
    
    for i in range(1, n + 1):
        if dq[0] < i - w:
            dq.popleft()
            
        # dp[i] = cost to have maintenance at i ?
        # Code: `dp[i] = v[i - 1] + dp[dq[0]]`
        # dq stores indices j < i. `dq[0]` is best previous index.
        # This is sliding window minimum of DP values.
        # Maintenance Windows: maybe must have maintenance every W days?
        # So look back W days for min cost.
        dp[i] = v[i - 1] + dp[dq[0]]
        
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)
        
    res_skipped = float("inf")
    # Must have last maintenance within last W window to cover end?
    for i in range(n - w + 1, n + 1):
        res_skipped = min(res_skipped, dp[i])
        
    # Result is `sum(v) - res_skipped`? Or is res_skipped the Min Cost?
    # Original code printed `sum(v) - res_skipped`.
    # Maybe problem is "Maximize value kept", where maintenance is cost?
    # Or "Minimizing lost value"?
    # If `dp` computes min cost of maintenance.
    # `res_skipped` is min cost to cover everything.
    # But usually DP returns the answer directly.
    # If code does `sum(v) - ...`, let's preserve it.
    print(sum(v) - res_skipped)


if __name__ == "__main__":
    solve()
