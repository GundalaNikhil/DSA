import sys
import random
import math

def solve(q, queries):
    results = []
    for a, m in queries:
        results.append("true" if math.gcd(a, m) == 1 else "false")
    return results

def make_test_case(queries):
    q = len(queries)
    res = solve(q, queries)
    inp = f"{q}\n" + "\n".join(f"{a} {m}" for a, m in queries)
    out = "\n".join(res)
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
        "problem_id": "NUM_MODULAR_INVERSE_EXISTENCE__3507",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case([(4, 7)]))

    # Public
    tc["public"].append(make_test_case([(1, 1), (2, 4), (3, 10)]))
    tc["public"].append(make_test_case([(10, 5), (7, 13)]))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case([(1, 1)]))
    tc["hidden"].append(make_test_case([(10**9, 10**9)]))
    tc["hidden"].append(make_test_case([(1, 10**9)]))
    tc["hidden"].append(make_test_case([(10**9, 1)]))

    # Boundary Cases
    tc["hidden"].append(make_test_case([(10**9, 10**9-1)]))
    tc["hidden"].append(make_test_case([(10**8, 10**8+1)]))

    # Special Constraint Cases (Large Primes)
    p1 = 999999937
    p2 = 1000000007
    tc["hidden"].append(make_test_case([(p1, p2), (p1, p1), (p1, 2*p1)]))

    # Normal Cases
    for _ in range(5):
        q = random.randint(10, 50)
        queries = [(random.randint(1, 10**9), random.randint(1, 10**9)) for _ in range(q)]
        tc["hidden"].append(make_test_case(queries))

    # Stress Case
    q_stress = 100000
    queries_stress = [(random.randint(1, 10**9), random.randint(1, 10**9)) for _ in range(q_stress)]
    tc["hidden"].append(make_test_case(queries_stress))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
