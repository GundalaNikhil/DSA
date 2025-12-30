import sys

def expected_comparisons(n: int, k: int) -> float:
    dp = [[0.0] * (n + 1) for _ in range(n + 1)]
    col_sum = [[0.0] * (n + 1) for _ in range(n + 1)]
    diag_sum = [[0.0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            total = 0.0
            
            # Left subproblems: pivot > j
            # Sizes j to i-1, target j
            if i - 1 >= j:
                total += col_sum[j][i - 1] - col_sum[j][j - 1]
                
            # Right subproblems: pivot < j
            # Diff = i - j
            d = i - j
            if j > 1:
                total += diag_sum[d][i - 1]
                
            dp[i][j] = (i - 1) + total / i
            
            col_sum[j][i] = col_sum[j][i - 1] + dp[i][j]
            diag_sum[i - j][i] = diag_sum[i - j][i - 1] + dp[i][j]
            
    return dp[n][k]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    print(f"{expected_comparisons(n, k):.6f}")

if __name__ == "__main__":
    main()
