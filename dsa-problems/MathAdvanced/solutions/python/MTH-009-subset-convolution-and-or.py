import sys

class Solution:
    def subset_convolution_and_or(self, n: int, op: int, A: list[int], B: list[int]) -> list[int]:
        MOD = 1000000007
        size = 1 << n
        
        def fzt_or(a, invert):
            for i in range(n):
                for mask in range(size):
                    if mask & (1 << i):
                        u = a[mask]
                        v = a[mask ^ (1 << i)]
                        if not invert:
                            a[mask] = (u + v) % MOD
                        else:
                            a[mask] = (u - v + MOD) % MOD

        def fzt_and(a, invert):
            for i in range(n):
                for mask in range(size):
                    if not (mask & (1 << i)):
                        u = a[mask]
                        v = a[mask ^ (1 << i)]
                        if not invert:
                            a[mask] = (u + v) % MOD
                        else:
                            a[mask] = (u - v + MOD) % MOD

        if op == 1: # OR
            fzt_or(A, False)
            fzt_or(B, False)
        else: # AND
            fzt_and(A, False)
            fzt_and(B, False)
            
        C = [(A[i] * B[i]) % MOD for i in range(size)]
        
        if op == 1: # OR
            fzt_or(C, True)
        else: # AND
            fzt_and(C, True)
            
        return C

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        op = int(next(iterator))
        size = 1 << n
        
        A = [int(next(iterator)) for _ in range(size)]
        B = [int(next(iterator)) for _ in range(size)]
        
        sol = Solution()
        res = sol.subset_convolution_and_or(n, op, A, B)
        print(*(res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
