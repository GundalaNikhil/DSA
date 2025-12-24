import random

def solve_game(n, m, matrix):
    memo = {}
    def solve(r1, r2, c1, c2):
        if r1 == r2 and c1 == c2:
            return matrix[r1][c1]
        state = (r1, r2, c1, c2)
        if state in memo: return memo[state]
        
        # Player 1 (Max) moves if (r1+r2+c1+c2) parity? 
        # Actually it's cleaner to check who's turn it is based on number of removals.
        # Initial: n*m elements. Each move removes a row or column (multiple elements).
        # Wait, the problem says "Player 1 removes a row/col, then Player 2...".
        # So it's always P1, P2, P1, P2...
        # Number of moves made = (n-1 - (r2-r1)) + (m-1 - (c2-c1))
        moves_made = (n - 1 - (r2 - r1)) + (m - 1 - (c2 - c1))
        
        if moves_made % 2 == 0: # P1's turn (Max)
            res = -float('inf')
            if r1 < r2:
                res = max(res, solve(r1 + 1, r2, c1, c2))
                res = max(res, solve(r1, r2 - 1, c1, c2))
            if c1 < c2:
                res = max(res, solve(r1, r2, c1 + 1, c2))
                res = max(res, solve(r1, r2, c1, c2 - 1))
        else: # P2's turn (Min)
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

new_tests = []
for _ in range(15):
    n = random.randint(2, 6)
    m = random.randint(2, 6)
    matrix = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]
    out = solve_game(n, m, matrix)
    new_tests.append((n, m, matrix, out))

with open("new_gmt013_hidden.txt", "w") as f:
    for n, m, mat, out in new_tests:
        f.write(f"- input: |-\n    {n} {m}\n")
        for row in mat:
            f.write(f"    {' '.join(map(str, row))}\n")
        f.write(f"  output: |-\n    {out}\n")
