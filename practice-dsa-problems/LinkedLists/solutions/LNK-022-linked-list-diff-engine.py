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
    A = []
    for _ in range(n):
        A.append(int(input_data[ptr]))
        ptr += 1
        
    B = []
    for _ in range(m):
        B.append(int(input_data[ptr]))
        ptr += 1
        
    ci = int(input_data[ptr])
    ptr += 1
    cd = int(input_data[ptr])
    ptr += 1
    cr = int(input_data[ptr])
    ptr += 1
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    for i in range(1, n + 1):
        dp[i][0] = i * cd
    for j in range(1, m + 1):
        dp[0][j] = j * ci
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i][j - 1] + ci,      # Insert
                    dp[i - 1][j] + cd,      # Delete
                    dp[i - 1][j - 1] + cr,  # Replace
                )
                
    print(dp[n][m])


if __name__ == "__main__":
    solve()
