import random

def solve_game(n, A):
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + A[i]
    
    def get_sum(i, j):
        return prefix_sum[j+1] - prefix_sum[i]
    
    memo = {}
    def solve(i, j):
        if i == j: return 0
        state = (i, j)
        if state in memo: return memo[state]
        
        res = -float('inf')
        for k in range(i, j):
            sum_left = get_sum(i, k)
            sum_right = get_sum(k + 1, j)
            
            val_take_left = -sum_left - solve(k + 1, j)
            val_take_right = -sum_right - solve(i, k)
            
            res = max(res, min(val_take_left, val_take_right))
        
        memo[state] = res
        return res
    
    return solve(0, n - 1)

new_tests = []
for _ in range(20):
    n = random.randint(2, 20)
    A = [random.randint(1, 100) for _ in range(n)]
    out = solve_game(n, A)
    new_tests.append((n, A, out))

with open("new_gmt014_hidden.txt", "w") as f:
    for n, A, out in new_tests:
        f.write(f"- input: |-\n    {n}\n    {' '.join(map(str, A))}\n  output: |-\n    {out}\n")
