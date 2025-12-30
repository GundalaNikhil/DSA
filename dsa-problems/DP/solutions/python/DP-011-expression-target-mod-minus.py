MOD = 1_000_000_007

def count_expressions(s: str, M: int, K: int, L: int) -> int:
    # Handle edge cases
    if L <= 0 or M <= 0:
        return 0

    n = len(s)
    # dp[pos][remainder][has_minus] = count of ways
    dp = [[[0]*2 for _ in range(M)] for __ in range(n+1)]

    # Initialize: try all possible first chunks
    for l in range(1, min(L, n) + 1):
        if s[0] == '0' and l > 1:
            break
        val = int(s[0:l]) % M
        dp[l][val][0] = 1

    # Fill DP table
    for pos in range(1, n):
        for rem in range(M):
            for has_minus in range(2):
                ways = dp[pos][rem][has_minus]
                if ways == 0:
                    continue

                # Try all possible next chunks
                for l in range(1, min(L, n - pos) + 1):
                    if s[pos] == '0' and l > 1:
                        break

                    val = int(s[pos:pos+l]) % M

                    # Option 1: Add this chunk (keep has_minus state)
                    addRem = (rem + val) % M
                    dp[pos+l][addRem][has_minus] = (dp[pos+l][addRem][has_minus] + ways) % MOD

                    # Option 2: Subtract this chunk (set has_minus to 1)
                    subRem = (rem - val) % M
                    dp[pos+l][subRem][1] = (dp[pos+l][subRem][1] + ways) % MOD

    # Return count of expressions that end at position n with remainder K and at least one minus
    return dp[n][K][1]


def main():
    s = input().strip()
    M, K, L = map(int, input().split())
    print(count_expressions(s, M, K, L))

if __name__ == "__main__":
    main()
