import sys

class Solution:
    def determinant_gaussian(self, n: int, MOD: int, matrix: list[list[int]]) -> int:
        
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

        det = 1
        
        for i in range(n):
            pivot = i
            while pivot < n and matrix[pivot][i] == 0:
                pivot += 1
            
            if pivot == n:
                return 0
            
            if pivot != i:
                matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
                det = (MOD - det) % MOD
            
            det = (det * matrix[i][i]) % MOD
            inv = modInverse(matrix[i][i])
            
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    factor = (matrix[j][i] * inv) % MOD
                    # Optimize: only update from column i onwards
                    # Python slicing is convenient but creates copies. Loop is better for O(1) space.
                    for k in range(i, n):
                        sub = (factor * matrix[i][k]) % MOD
                        matrix[j][k] = (matrix[j][k] - sub + MOD) % MOD
                        
        return det

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
        print(sol.determinant_gaussian(n, MOD, matrix))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
