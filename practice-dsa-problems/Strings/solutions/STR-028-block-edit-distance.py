import sys


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        return
    a = input_data[0]
    b = input_data[1]
    l_limit = int(input_data[2])
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    cost = 0 if a[i - 1] == b[j - 1] else 1
                    dp[i][j] = min(
                        dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost
                    )
                    for k in range(1, l_limit + 1):
                        if i >= k and j >= k:
                            dp[i][j] = min(dp[i][j], dp[i - k][j - k] + 1)
                            
    print(dp[n][m])


if __name__ == "__main__":
    solve()
