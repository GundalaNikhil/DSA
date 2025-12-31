import sys

class Solution:
    def invert_vandermonde(self, n: int, MOD: int, x: list[int]) -> list[list[int]]:
        
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

        # Compute P(x) = product(x - x_k)
        P = [0] * (n + 1)
        P[0] = 1
        
        for k in range(n):
            # Multiply by (x - x_k)
            # P_new[i] = P_old[i-1] - x_k * P_old[i]
            prev = P[0]
            P[0] = (MOD - x[k] * P[0] % MOD) % MOD
            for i in range(1, k + 2):
                temp = P[i]
                P[i] = (prev - x[k] * P[i] % MOD + MOD) % MOD
                prev = temp
                
        inv = [[0] * n for _ in range(n)]
        
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j: continue
                prod = (prod * (x[i] - x[j] + MOD)) % MOD
            w = modInverse(prod)
            
            # Synthetic division P(x) / (x - x_i)
            q_k = 0
            for k in range(n, 0, -1):
                val = (P[k] + x[i] * q_k) % MOD
                q_k = val
                inv[k - 1][i] = (val * w) % MOD
                
        return inv

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        MOD = int(next(iterator))
        x = [int(next(iterator)) for _ in range(n)]
        
        sol = Solution()
        res = sol.invert_vandermonde(n, MOD, x)
        
        for row in res:
            print(*(row))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
