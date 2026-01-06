import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    n = len(s)
    ptr = 1
    weights = [[0] * 26 for _ in range(26)]
    for i in range(26):
        for j in range(26):
            weights[i][j] = int(input_data[ptr])
            ptr += 1
            
    # Run DP
    dp = [[0] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                char_idx = ord(s[i]) - ord("a")
                dp[i][j] = weights[char_idx][char_idx]
            else:
                if s[i] == s[j]:
                    char_idx = ord(s[i]) - ord("a")
                    inner = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                    dp[i][j] = max(
                        dp[i][j], inner + 2 * weights[char_idx][char_idx]
                    )
                dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j - 1])
                
    print(dp[0][n - 1])


if __name__ == "__main__":
    solve()
