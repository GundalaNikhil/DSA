import sys

class Solution:
    def berlekamp_massey(self, m: int, n: int, MOD: int, S: list[int]) -> int:
        
        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1: res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        def modInverse(x):
            return power(x, MOD - 2)

        C = [1]
        B = [1]
        L = 0
        b = 1
        b_delta = 1
        
        for i in range(m):
            delta = S[i]
            for j in range(1, len(C)):
                delta = (delta + C[j] * S[i - j]) % MOD
            
            if delta == 0:
                b += 1
                continue
            
            T = C[:]
            factor = (delta * modInverse(b_delta)) % MOD
            
            # C = C - factor * x^b * B
            if len(C) < len(B) + b:
                C.extend([0] * (len(B) + b - len(C)))
                
            for j in range(len(B)):
                val = (B[j] * factor) % MOD
                idx = j + b
                C[idx] = (C[idx] - val + MOD) % MOD
            
            if 2 * L <= i:
                L = i + 1 - L
                B = T
                b_delta = delta
                b = 1
            else:
                b += 1
        
        K = len(C) - 1
        if K == 0: return 0
        
        Rec = [(MOD - C[i+1]) % MOD for i in range(K)]
        
        if n < m: return S[n]
        
        # Kitamasa
        def combine(A, B_poly):
            # A, B are polys of degree < K
            prod = [0] * (2 * K)
            for i in range(len(A)):
                for j in range(len(B_poly)):
                    prod[i + j] = (prod[i + j] + A[i] * B_poly[j]) % MOD
            
            # Reduce
            for i in range(len(prod) - 1, K - 1, -1):
                factor = prod[i]
                if factor == 0: continue
                for j in range(K):
                    target = i - 1 - j
                    prod[target] = (prod[target] + factor * Rec[j]) % MOD
            
            return prod[:K]

        res = [0] * K
        res[0] = 1
        
        base = [0] * K
        if K > 0: base[1 % K] = 1
        
        exp = n
        while exp > 0:
            if exp % 2 == 1: res = combine(res, base)
            base = combine(base, base)
            exp //= 2
            
        ans = 0
        for i in range(K):
            ans = (ans + res[i] * S[i]) % MOD
            
        return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        m = int(next(iterator))
        n = int(next(iterator))
        S = [int(next(iterator)) for _ in range(m)]
        MOD = int(next(iterator))
        
        sol = Solution()
        print(sol.berlekamp_massey(m, n, MOD, S))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
