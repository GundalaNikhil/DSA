import sys

class Solution:
    def matrix_exp_linear_recurrence(self, k: int, n: int, MOD: int, coeffs: list[int], initial: list[int]) -> int:
        if n < k:
            return initial[n]
            
        def multiply(A, B):
            C = [[0] * k for _ in range(k)]
            for i in range(k):
                for l in range(k):
                    if A[i][l] == 0: continue
                    for j in range(k):
                        C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % MOD
            return C

        def power(A, exp):
            res = [[0] * k for _ in range(k)]
            for i in range(k): res[i][i] = 1
            while exp > 0:
                if exp % 2 == 1: res = multiply(res, A)
                A = multiply(A, A)
                exp //= 2
            return res

        T = [[0] * k for _ in range(k)]
        for j in range(k):
            T[0][j] = coeffs[j]
        for i in range(1, k):
            T[i][i - 1] = 1
            
        T_pow = power(T, n - k + 1)
        
        ans = 0
        # Initial vector is [a_{k-1}, a_{k-2}, ..., a_0]
        # We multiply T_pow[0] (first row) with this vector
        for j in range(k):
            ans = (ans + T_pow[0][j] * initial[k - 1 - j]) % MOD
            
        return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        n = int(next(iterator))
        MOD = int(next(iterator))
        
        coeffs = [int(next(iterator)) for _ in range(k)]
        initial = [int(next(iterator)) for _ in range(k)]
        
        sol = Solution()
        print(sol.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
