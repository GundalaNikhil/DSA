import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    f = []
    for _ in range(m - 1):
        f.append(int(input_data[ptr]))
        ptr += 1
        b = []
        for _ in range(m - 1):
            b.append(int(input_data[ptr]))
            ptr += 1
            
    inf = float("inf")
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    dp[0][1] = 0
    
    for move in range(n):
        for pos in range(1, m + 1):
            if dp[move][pos] == inf:
                continue
            
            # Forward
            if pos < m:
                cost = f[pos - 1]
                dp[move + 1][pos + 1] = min(
                    dp[move + 1][pos + 1], dp[move][pos] + cost
                )
                
            # Backward
            if pos > 1:
                cost = b[pos - 2]
                dp[move + 1][pos - 1] = min(
                    dp[move + 1][pos - 1], dp[move][pos] + cost
                )
                
    ans = dp[n][m]
    print(ans if ans != inf else -1)


if __name__ == "__main__":
    solve()
