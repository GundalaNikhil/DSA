import sys

class Solution:
    def convolution_multi_mod_crt(self, n: int, m: int, A: list[int], B: list[int], targetMod: int) -> list[int]:
        
        def power(base, exp, mod):
            res = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1: res = (res * base) % mod
                base = (base * base) % mod
                exp //= 2
            return res

        def modInverse(n, mod):
            return power(n, mod - 2, mod)

        def ntt(a, invert, mod, g):
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
                wlen = power(g, (mod - 1) // length, mod)
                if invert: wlen = modInverse(wlen, mod)
                for i in range(0, n, length):
                    w = 1
                    for j in range(length // 2):
                        u = a[i + j]
                        v = (a[i + j + length // 2] * w) % mod
                        a[i + j] = (u + v) % mod
                        a[i + j + length // 2] = (u - v + mod) % mod
                        w = (w * wlen) % mod
                length <<= 1
            
            if invert:
                nInv = modInverse(n, mod)
                for i in range(n):
                    a[i] = (a[i] * nInv) % mod

        def convolve(A, B, mod, g):
            size = 1
            while size < len(A) + len(B): size <<= 1
            fa = A + [0] * (size - len(A))
            fb = B + [0] * (size - len(B))
            ntt(fa, False, mod, g)
            ntt(fb, False, mod, g)
            for i in range(size): fa[i] = (fa[i] * fb[i]) % mod
            ntt(fa, True, mod, g)
            return fa

        P1, G1 = 998244353, 3
        P2, G2 = 1004535809, 3
        P3, G3 = 469762049, 3
        
        c1 = convolve(A, B, P1, G1)
        c2 = convolve(A, B, P2, G2)
        c3 = convolve(A, B, P3, G3)
        
        length = n + m - 1
        res = []
        
        P1_inv_P2 = modInverse(P1, P2)
        P1P2_inv_P3 = modInverse((P1 * P2) % P3, P3)
        
        for i in range(length):
            a1 = c1[i]
            a2 = c2[i]
            a3 = c3[i]
            
            x1 = a1
            x2 = ((a2 - x1 + P2) % P2 * P1_inv_P2) % P2
            x3 = ((a3 - x1 - x2 * P1 % P3 + 2 * P3) % P3 * P1P2_inv_P3) % P3
            
            ans = (x1 + x2 * P1) % targetMod
            ans = (ans + (x3 * ((P1 * P2) % targetMod)) % targetMod) % targetMod
            res.append(ans)
            
        return res

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        A = [int(next(iterator)) for _ in range(n)]
        B = [int(next(iterator)) for _ in range(m)]
        MOD = int(next(iterator))
        
        sol = Solution()
        res = sol.convolution_multi_mod_crt(n, m, A, B, MOD)
        print(*(res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
