from typing import List
import sys

# Increase recursion depth
sys.setrecursionlimit(20000)

def matrix_game(n: int, m: int, matrix: List[List[int]]) -> int:
    memo = {}

    def solve(r1, r2, c1, c2):
        state = (r1, r2, c1, c2)
        if state in memo:
            return memo[state]
        
        if r1 == r2 and c1 == c2:
            return matrix[r1][c1]
        
        moves_made = (n - (r2 - r1 + 1)) + (m - (c2 - c1 + 1))
        is_max = (moves_made % 2 == 0)
        
        if is_max:
            res = -float('inf')
            if r1 < r2:
                res = max(res, solve(r1 + 1, r2, c1, c2))
                res = max(res, solve(r1, r2 - 1, c1, c2))
            if c1 < c2:
                res = max(res, solve(r1, r2, c1 + 1, c2))
                res = max(res, solve(r1, r2, c1, c2 - 1))
        else:
            res = float('inf')
            if r1 < r2:
                res = min(res, solve(r1 + 1, r2, c1, c2))
                res = min(res, solve(r1, r2 - 1, c1, c2))
            if c1 < c2:
                res = min(res, solve(r1, r2, c1 + 1, c2))
                res = min(res, solve(r1, r2, c1, c2 - 1))
        
        memo[state] = res
        return res

    return solve(0, n - 1, 0, m - 1)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        matrix = []
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(int(next(iterator)))
            matrix.append(row)
            
        print(matrix_game(n, m, matrix))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
