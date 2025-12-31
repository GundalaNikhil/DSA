import sys
import random

class Solution:
    def minimal_polynomial_matrix(self, n: int, MOD: int, matrix: list[list[int]]) -> list[int]:
        
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

        def berlekamp_massey(s):
            C = [1]
            B = [1]
            L = 0
            b = 1
            b_delta = 1
            
            for i in range(len(s)):
                delta = s[i]
                for j in range(1, len(C)):
                    delta = (delta + C[j] * s[i - j]) % MOD
                
                if delta == 0:
                    b += 1
                    continue
                
                T = C[:]
                factor = (delta * modInverse(b_delta)) % MOD
                
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
            return C

        # Random vectors
        random.seed(12345)
        u = [random.randint(0, MOD-1) for _ in range(n)]
        v = [random.randint(0, MOD-1) for _ in range(n)]
        
        seq = []
        currV = list(v)
        
        for _ in range(2 * n + 2):
            val = sum((u[i] * currV[i]) % MOD for i in range(n)) % MOD
            seq.append(val)
            
            nextV = [0] * n
            for r in range(n):
                for c in range(n):
                    nextV[r] = (nextV[r] + matrix[r][c] * currV[c]) % MOD
            currV = nextV
            
        C = berlekamp_massey(seq)
        
        d = len(C) - 1
        # Reverse C to get coefficients from constant to x^d
        res = C[::-1]
        
        return [d] + res

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        MOD = int(next(iterator))
        
        matrix = []
        for _ in range(n):
            row = [int(next(iterator)) for _ in range(n)]
            matrix.append(row)
            
        sol = Solution()
        res = sol.minimal_polynomial_matrix(n, MOD, matrix)
        
        print(res[0])
        print(*(res[1:]))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
