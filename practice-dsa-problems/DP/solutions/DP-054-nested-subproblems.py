import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k_segments = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        a.append(int(input_data[ptr]))
        ptr += 1
        
    # Precompute Max Subarray sum for all ranges [i, j]?
    # Code `ms[i][j] = best`.
    ms = [[-float("inf")] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            # Max Subarray in a[i...j]
            best_sub = -float("inf")
            curr = 0
            for x in range(i, j + 1):
                curr += a[x]
                if curr > best_sub:
                    best_sub = curr
                if curr < 0:
                    curr = 0
            ms[i][j] = best_sub
            
    # DP: Split array into K segments such that sum of "values" is max?
    # Value of segment = max subarray sum in that segment?
    # dp[k][i] = max total value using k segments ending at index i
    
    dp = [[-float("inf")] * n for _ in range(k_segments + 1)]
    
    # Init k=1
    for i in range(n):
        dp[1][i] = ms[0][i]
        
    for k in range(2, k_segments + 1):
         for i in range(k - 1, n):
             # Try splitting at j < i
             for j in range(k - 2, i):
                 if dp[k - 1][j] != -float("inf"):
                     dp[k][i] = max(
                         dp[k][i],
                         dp[k - 1][j] + ms[j + 1][i],
                     )
                     
    print(dp[k_segments][n - 1])


if __name__ == "__main__":
    solve()
