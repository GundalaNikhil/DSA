import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    m_mod = int(input_data[1])
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1 % m_mod
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] + 1) % m_mod
            else:
                dp[i][j] = (
                    dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + m_mod
                ) % m_mod
                
    print(dp[0][n - 1])


if __name__ == "__main__":
    solve()
