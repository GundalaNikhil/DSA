import sys
import random

def get_f(n):
    f = [0] * (n + 1)
    for i in range(2, n + 1):
        if f[i] == 0:
            for j in range(i, n + 1, i):
                f[j] += 1
    return f

# Precompute once
MAX_N = 1000000
f_table = get_f(MAX_N)
pref_f = [0] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    pref_f[i] = pref_f[i-1] + f_table[i]

def solve(n, q, queries):
    return [pref_f[min(r, MAX_N)] - pref_f[min(l-1, MAX_N)] for l, r in queries]

def make_test_case(n, queries):
    q = len(queries)
    res = solve(n, q, queries)
    inp = f"{n} {q}\n" + "\n".join(f"{l} {r}" for l, r in queries)
    out = "\n".join(map(str, res))
    return {"input": inp, "output": out}

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    tc = {
        "problem_id": "NUM_DISTINCT_PRIME_FACTORS_PREFIX__5173",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(6, [(2, 5)]))

    # Public
    tc["public"].append(make_test_case(10, [(1, 10), (5, 5)]))
    tc["public"].append(make_test_case(1, [(1, 1)]))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1, [(1, 1)]))
    tc["hidden"].append(make_test_case(MAX_N, [(1, MAX_N)]))
    tc["hidden"].append(make_test_case(10, [(1, 1), (10, 10)]))

    # Boundary Cases
    tc["hidden"].append(make_test_case(100, [(1, 100), (99, 100)]))
    tc["hidden"].append(make_test_case(MAX_N, [(MAX_N-1, MAX_N)]))

    # Special Constraint Cases (Highly composite numbers)
    # 2*3*5*7*11*13*17 = 510510
    tc["hidden"].append(make_test_case(MAX_N, [(510510, 510510), (2310, 2310)]))

    # Normal Cases
    for _ in range(5):
        n = random.randint(100, 10000)
        q = random.randint(5, 20)
        queries = []
        for _ in range(q):
            l = random.randint(1, n)
            r = random.randint(l, n)
            queries.append((l, r))
        tc["hidden"].append(make_test_case(n, queries))

    # Stress Case
    q_stress = 100000
    queries_stress = []
    for _ in range(q_stress):
        l = random.randint(1, MAX_N)
        r = random.randint(l, MAX_N)
        queries_stress.append((l, r))
    tc["hidden"].append(make_test_case(MAX_N, queries_stress))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
