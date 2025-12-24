import random

def solve(n, A, L):
    xor_sum = 0
    for i in range(n):
        xor_sum ^= (A[i] % (L[i] + 1))
    return "First" if xor_sum > 0 else "Second"

new_tests = []
# Edge cases
new_tests.append((1, [1], [1]))
new_tests.append((1, [10], [1]))
new_tests.append((2, [2, 2], [2, 2]))

# Random cases
for _ in range(20):
    n = random.randint(2, 10)
    A = [random.randint(1, 100) for _ in range(n)]
    L = [random.randint(1, 10) for _ in range(n)]
    out = solve(n, A, L)
    new_tests.append((n, A, L, out))

with open("new_gmt016_hidden.txt", "w") as f:
    for t in new_tests:
        if len(t) == 3:
            n, A, L = t
            out = solve(n, A, L)
        else:
            n, A, L, out = t
        f.write(f"- input: |-\n    {n}\n    {' '.join(map(str, A))}\n    {' '.join(map(str, L))}\n  output: |-\n    {out}\n")
