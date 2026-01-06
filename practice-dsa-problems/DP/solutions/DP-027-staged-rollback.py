import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    r_limit = int(input_data[ptr])
    ptr += 1
    cost = int(input_data[ptr])
    ptr += 1
    v = []
    for _ in range(n):
        v.append(int(input_data[ptr]))
        ptr += 1
        
    inf = float("inf")
    # dp[i][r] = max score at step i, with 'r' rollback points available?
    dp = [[-inf] * (r_limit + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for r in range(r_limit + 1):
            if dp[i - 1][r] != -inf:
                # Option 1: Continue normally?
                # Code: `dp[i][r] = max(..., dp[i-1][r] + v[i-1])`
                dp[i][r] = max(dp[i][r], dp[i - 1][r] + v[i - 1])
                
        # Option 2: Rollback?
        # A rollback might consume 'r' resource (or generate it?).
        # Original code: `if r > 0: for j in range(i): ... dp[i][r] = max(.., dp[j][r-1] - cost)`
        # This implies we can jump from j < i to i, costing 1 'r' unit and 'cost' value?
        # Maybe "Staged Rollback" means reverting state to j?
        # If we jump from j to i, we skip intermediate steps?
        # Loop `for r in range(r_limit + 1)` needs distinct handling if modifying r.
        # Original code iterated `i`, then `r`. Then inside usage of `if r > 0`.
        # Safe to iterate r.
        
        for r in range(1, r_limit + 1):
            # Check transitions from previous steps j < i
             for j in range(i):
                 # Jumping from j to i using 1 rollback credit
                 if dp[j][r - 1] != -inf:
                     dp[i][r] = max(dp[i][r], dp[j][r - 1] - cost)
                     
    ans = max(dp[n])
    print(ans if ans != -inf else 0)


if __name__ == "__main__":
    solve()
