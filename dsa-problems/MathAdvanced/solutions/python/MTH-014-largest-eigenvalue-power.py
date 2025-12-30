import sys
import math

class Solution:
    def largest_eigenvalue_power(self, n: int, maxIter: int, matrix: list[list[float]], epsilon: float) -> float:
        v = [1.0] * n
        lambda_val = 0.0
        
        for _ in range(maxIter):
            # w = A * v
            w = [0.0] * n
            for i in range(n):
                for j in range(n):
                    w[i] += matrix[i][j] * v[j]
            
            # Rayleigh Quotient
            num = sum(v[i] * w[i] for i in range(n))
            den = sum(v[i] * v[i] for i in range(n))
            
            new_lambda = 0.0 if den == 0 else num / den
            
            if abs(new_lambda - lambda_val) < epsilon:
                return new_lambda
            
            lambda_val = new_lambda
            
            # Normalize
            max_val = max(abs(x) for x in w)
            if max_val < 1e-9: break
            
            v = [x / max_val for x in w]
            
        return lambda_val

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        maxIter = int(next(iterator))
        
        matrix = []
        for _ in range(n):
            row = [float(next(iterator)) for _ in range(n)]
            matrix.append(row)
            
        epsilon = float(next(iterator))
        
        sol = Solution()
        res = sol.largest_eigenvalue_power(n, maxIter, matrix, epsilon)
        print(f"{res:.6f}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
