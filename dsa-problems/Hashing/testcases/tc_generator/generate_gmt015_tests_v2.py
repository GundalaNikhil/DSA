import random

def get_grundy(i, k):
    return (i % (k + 1)) + 1

def solve(n, k, s):
    xor_sum = 0
    for i in range(len(s)):
        if s[i] == 'H':
            xor_sum ^= get_grundy(i, k)
    return "First" if xor_sum > 0 else "Second"

def generate_test(n, k):
    s = "".join(random.choice(['H', 'T']) for _ in range(n))
    output = solve(n, k, s)
    return s, output

new_tests = []
# Edge cases
new_tests.append((1, 1, "H"))
new_tests.append((1, 1, "T"))
new_tests.append((10, 1, "T" * 10))
new_tests.append((10, 10, "H" * 10))

# Random cases
for _ in range(20):
    n = random.randint(5, 50)
    k = random.randint(1, 5)
    s, out = generate_test(n, k)
    new_tests.append((n, k, s, out))

with open("new_gmt015_hidden.txt", "w") as f:
    for t in new_tests:
        if len(t) == 3: # Manual edge cases
            n, k, s = t
            out = solve(n, k, s)
        else:
            n, k, s, out = t
        f.write(f"- input: |-\n    {n} {k}\n    {s}\n  output: |-\n    {out}\n")
