import sys
import math

class Solution:
    def multiply_polynomials(self, A: list[int], B: list[int]) -> list[int]:
        MOD = 1000000007
        n = 1
        while n < len(A) + len(B):
            n <<= 1
            
        # Standard FFT implementation
        def fft(a, invert):
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
                ang = 2 * math.pi / length * (-1 if invert else 1)
                wlen = complex(math.cos(ang), math.sin(ang))
                for i in range(0, n, length):
                    w = complex(1, 0)
                    for j in range(length // 2):
                        u = a[i + j]
                        v = a[i + j + length // 2] * w
                        a[i + j] = u + v
                        a[i + j + length // 2] = u - v
                        w *= wlen
                length <<= 1
                
            if invert:
                for i in range(n):
                    a[i] /= n

        # Splitting for precision
        S = 32000
        a0 = [complex(x % S, 0) for x in A] + [0] * (n - len(A))
        a1 = [complex(x // S, 0) for x in A] + [0] * (n - len(A))
        b0 = [complex(x % S, 0) for x in B] + [0] * (n - len(B))
        b1 = [complex(x // S, 0) for x in B] + [0] * (n - len(B))
        
        fft(a0, False); fft(a1, False)
        fft(b0, False); fft(b1, False)
        
        c0 = [a0[i] * b0[i] for i in range(n)]
        c2 = [a1[i] * b1[i] for i in range(n)]
        c1 = [(a0[i] + a1[i]) * (b0[i] + b1[i]) - c0[i] - c2[i] for i in range(n)]
        
        fft(c0, True); fft(c1, True); fft(c2, True)
        
        res = []
        for i in range(len(A) + len(B) - 1):
            v0 = int(c0[i].real + 0.5) % MOD
            v1 = int(c1[i].real + 0.5) % MOD
            v2 = int(c2[i].real + 0.5) % MOD
            val = (v2 * S * S + v1 * S + v0) % MOD
            res.append(val)
            
        return res

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
        res = sol.multiply_polynomials(A, B)
        print(*(res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
