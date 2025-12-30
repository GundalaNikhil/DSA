import sys

def streak_probability(n: int, k: int) -> float:
    if k > n:
        return 0.0

    # dp[i] = number of sequences of length i with NO streak of k heads
    dp = [0] * (n + 1)

    for i in range(k):
        dp[i] = 1 << i

    dp[k] = (1 << k) - 1

    for i in range(k + 1, n + 1):
        dp[i] = 2 * dp[i - 1] - dp[i - k - 1]

    total = 1 << n
    valid = dp[n]
    return 1.0 - valid / total

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    print(streak_probability(n, k))

if __name__ == "__main__":
    main()
