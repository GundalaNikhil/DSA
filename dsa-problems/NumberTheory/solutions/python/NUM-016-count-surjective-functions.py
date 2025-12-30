import sys

def power(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def count_surjections(n: int, k: int) -> int:
    MOD = 1000000007
    
    if k > n:
        return 0
        
    # Precompute Combinations
    C = [[0] * (k + 1) for _ in range(k + 1)]
    for i in range(k + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
            
    ans = 0
    for i in range(k + 1):
        term = (C[k][i] * power(k - i, n, MOD)) % MOD
        if i % 2 == 1:
            ans = (ans - term + MOD) % MOD
        else:
            ans = (ans + term) % MOD
            
    return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    print(count_surjections(n, k))

if __name__ == "__main__":
    main()
