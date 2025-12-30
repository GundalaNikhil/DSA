import sys

class Solution:
    def lagrange_interpolation_mod(self, k: int, X: int, MOD: int, points: list[list[int]]) -> int:
        
        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1: res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        def modInverse(n):
            return power(n, MOD - 2)

        ans = 0
        
        # O(k^2) approach
        for i in range(k):
            xi, yi = points[i]
            
            num = 1
            den = 1
            
            for j in range(k):
                if i == j: continue
                xj = points[j][0]
                
                num = (num * (X - xj)) % MOD
                den = (den * (xi - xj)) % MOD
            
            term = (yi * num) % MOD
            term = (term * modInverse(den)) % MOD
            ans = (ans + term) % MOD
            
        return (ans + MOD) % MOD

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        X = int(next(iterator))
        MOD = int(next(iterator))
        
        points = []
        for _ in range(k):
            points.append([int(next(iterator)), int(next(iterator))])
            
        sol = Solution()
        print(sol.lagrange_interpolation_mod(k, X, MOD, points))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
