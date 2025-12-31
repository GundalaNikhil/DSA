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

def modInverse(n, mod):
    return power(n, mod - 2, mod)

def count_strings(n: int, k: int) -> int:
    MOD = 1000000007
    
    if k < 0 or k > n:
        return 0
        
    # Compute nCr
    # Since we only need one nCr, we can compute directly without full array if we wanted O(k) or O(n)
    # But O(n) precompute is fine.
    
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
        
    invFact = [1] * (n + 1)
    invFact[n] = modInverse(fact[n], MOD)
    for i in range(n - 1, 1, -1):
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD
        
    nCr = fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
    
    vowels = power(5, k, MOD)
    consonants = power(21, n - k, MOD)
    
    return nCr * vowels % MOD * consonants % MOD

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    print(count_strings(n, k))

if __name__ == "__main__":
    main()
