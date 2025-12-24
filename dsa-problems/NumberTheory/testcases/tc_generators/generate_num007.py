import sys
import random
import math

def get_prime_factors(n):
    factors = {}
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            factors[d] = count
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

def solve_query(a, l, r, MOD):
    max_factors = {}
    for i in range(l, r + 1):
        factors = get_prime_factors(a[i])
        for p, count in factors.items():
            max_factors[p] = max(max_factors.get(p, 0), count)
    
    res = 1
    for p, count in max_factors.items():
        for _ in range(count):
            res = (res * p) % MOD
    return res

def make_test_case(n, q, MOD, a, queries):
    res = [solve_query(a, l, r, MOD) for l, r in queries]
    inp = f"{n} {q} {MOD}\n" + " ".join(map(str, a)) + "\n" + "\n".join(f"{l} {r}" for l, r in queries)
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
        "problem_id": "NUM_LCM_OF_RANGES__8402",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(3, 1, 1000000007, [2, 6, 3], [(0, 1)]))

    # Public
    tc["public"].append(make_test_case(5, 2, 1000000007, [1, 2, 3, 4, 5], [(0, 4), (1, 3)]))
    tc["public"].append(make_test_case(4, 2, 100, [10, 20, 30, 40], [(0, 1), (2, 3)]))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1, 1, 1000000007, [10**9], [(0, 0)]))
    tc["hidden"].append(make_test_case(2, 1, 1000000007, [10**9, 10**9], [(0, 1)]))
    tc["hidden"].append(make_test_case(21, 1, 10**9+7, [1]*21, [(0, 20)]))

    # Boundary Cases (Range length 21)
    tc["hidden"].append(make_test_case(30, 2, 10**9+7, [random.randint(1, 100) for _ in range(30)], [(0, 20), (9, 29)]))

    # Special Constraint Cases (Large primes, small MOD)
    p1 = 999999937
    p2 = 1000000007
    tc["hidden"].append(make_test_case(3, 1, 10**9+7, [p1, p2, p1], [(0, 2)]))
    tc["hidden"].append(make_test_case(3, 1, 2, [2, 4, 8], [(0, 2)]))

    # Normal Cases
    for _ in range(5):
        n = random.randint(50, 100)
        q = random.randint(5, 15)
        mod = random.randint(10, 10**9)
        a = [random.randint(1, 10**6) for _ in range(n)]
        queries = []
        for _ in range(q):
            l = random.randint(0, n - 1)
            r = min(l + 20, n - 1)
            queries.append((l, r))
        tc["hidden"].append(make_test_case(n, q, mod, a, queries))

    # Stress Case
    n_stress = 200000
    q_stress = 5
    mod_stress = 10**9+7
    a_stress = [random.randint(10**8, 10**9) for _ in range(n_stress)]
    queries_stress = []
    for i in range(q_stress):
        l = random.randint(0, n_stress - 21)
        queries_stress.append((l, l + 20))
    tc["hidden"].append(make_test_case(n_stress, q_stress, mod_stress, a_stress, queries_stress))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
