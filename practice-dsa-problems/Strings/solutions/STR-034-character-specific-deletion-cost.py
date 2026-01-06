import sys


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 28:
        return
    a = input_data[0]
    b = input_data[1]
    costs = [int(x) for x in input_data[2:]]
    n, m = len(a), len(b)
    total_a = sum(costs[ord(c) - ord("a")] for c in a)
    total_b = sum(costs[ord(c) - ord("a")] for c in b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + costs[ord(a[i - 1]) - ord("a")]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    print(total_a + total_b - 2 * dp[n][m])


if __name__ == "__main__":
    solve()
