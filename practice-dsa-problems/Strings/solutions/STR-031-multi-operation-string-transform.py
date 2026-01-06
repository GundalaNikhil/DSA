import sys


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        return
    a = input_data[0]
    b = input_data[1]
    costs = [int(x) for x in input_data[2:]]
    cs, cr, ci, cd = costs
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else cr
            dp[i][j] = min(
                dp[i - 1][j] + cd,
                dp[i][j - 1] + ci,
                dp[i - 1][j - 1] + cost,
            )
            
            # Damerau-Levenshtein transposition check
            if (
                i > 1
                and j > 1
                and a[i - 1] == b[j - 2]
                and a[i - 2] == b[j - 1]
            ):
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + cs)
                
    print(dp[n][m])


if __name__ == "__main__":
    solve()
