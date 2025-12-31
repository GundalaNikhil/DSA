import sys

class Solution:
    def inverse_polynomial(self, P: list[int], n: int, MOD: int) -> list[int]:
        G = 3
        
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

        def ntt(a, invert):
            N = len(a)
            j = 0
            for i in range(1, N):
                bit = N >> 1
                while j & bit:
                    j ^= bit
                    bit >>= 1
                j ^= bit
                if i < j: a[i], a[j] = a[j], a[i]
            
            length = 2
            while length <= N:
                wlen = power(G, (MOD - 1) // length)
                if invert: wlen = modInverse(wlen)
                for i in range(0, N, length):
                    w = 1
                    for j in range(length // 2):
                        u = a[i + j]
                        v = (a[i + j + length // 2] * w) % MOD
                        a[i + j] = (u + v) % MOD
                        a[i + j + length // 2] = (u - v + MOD) % MOD
                        w = (w * wlen) % MOD
                length <<= 1
            
            if invert:
                nInv = modInverse(N)
                for i in range(N): a[i] = (a[i] * nInv) % MOD

        # Iterative Approach
        b = [modInverse(P[0])]
        length = 1
        while length < n:
            length <<= 1
            limit = length << 1
            
            copyA = P[:length] + [0] * (limit - min(len(P), length))
            copyB = b + [0] * (limit - len(b))
            
            ntt(copyA, False)
            ntt(copyB, False)
            
            for i in range(limit):
                term = (copyA[i] * copyB[i]) % MOD
                copyB[i] = (copyB[i] * (2 - term + MOD)) % MOD
            
            ntt(copyB, True)
            b = copyB[:length]
            
        return b[:n]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        n = int(next(iterator))
        P = [int(next(iterator)) for _ in range(k)]
        MOD = int(next(iterator))
        
        sol = Solution()
        res = sol.inverse_polynomial(P, n, MOD)
        print(*(res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
