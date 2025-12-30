import sys

class Solution:
    def convolution(self, A: list[int], B: list[int], MOD: int) -> list[int]:
        G = 3
        
        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        def modInverse(n):
            return power(n, MOD - 2)

        def ntt(a, invert):
            n = len(a)
            j = 0
            for i in range(1, n):
                bit = n >> 1
                while j & bit:
                    j ^= bit
                    bit >>= 1
                j ^= bit
                if i < j:
                    a[i], a[j] = a[j], a[i]

            length = 2
            while length <= n:
                wlen = power(G, (MOD - 1) // length)
                if invert:
                    wlen = modInverse(wlen)
                
                for i in range(0, n, length):
                    w = 1
                    for j in range(length // 2):
                        u = a[i + j]
                        v = (a[i + j + length // 2] * w) % MOD
                        a[i + j] = (u + v) % MOD
                        a[i + j + length // 2] = (u - v + MOD) % MOD
                        w = (w * wlen) % MOD
                length <<= 1

            if invert:
                nInv = modInverse(n)
                for i in range(n):
                    a[i] = (a[i] * nInv) % MOD

        size = 1
        while size < len(A) + len(B):
            size <<= 1
            
        fa = A + [0] * (size - len(A))
        fb = B + [0] * (size - len(B))
        
        ntt(fa, False)
        ntt(fb, False)
        
        for i in range(size):
            fa[i] = (fa[i] * fb[i]) % MOD
            
        ntt(fa, True)
        
        return fa[:len(A) + len(B) - 1]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        A = [int(next(iterator)) for _ in range(n)]
        m = int(next(iterator))
        B = [int(next(iterator)) for _ in range(m)]
        
        sol = Solution()
        res = sol.convolution(A, B, 998244353)
        print(*(res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
