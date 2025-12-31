import sys

class Solution:
    def fwht_xor_convolution(self, k: int, A: list[int], B: list[int]) -> list[int]:
        MOD = 1000000007
        n = 1 << k
        
        def fwht(a, invert):
            length = 1
            while length < n:
                for i in range(0, n, 2 * length):
                    for j in range(length):
                        u = a[i + j]
                        v = a[i + j + length]
                        a[i + j] = (u + v) % MOD
                        a[i + j + length] = (u - v + MOD) % MOD
                length <<= 1
            
            if invert:
                invN = pow(n, MOD - 2, MOD)
                for i in range(n):
                    a[i] = (a[i] * invN) % MOD

        fwht(A, False)
        fwht(B, False)
        
        C = [(A[i] * B[i]) % MOD for i in range(n)]
        
        fwht(C, True)
        return C

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        n = 1 << k
        A = [int(next(iterator)) for _ in range(n)]
        B = [int(next(iterator)) for _ in range(n)]
        
        sol = Solution()
        res = sol.fwht_xor_convolution(k, A, B)
        print(*(res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
