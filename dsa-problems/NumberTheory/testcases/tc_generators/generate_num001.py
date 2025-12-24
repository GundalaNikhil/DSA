import sys
import random
import math

def gcd(a, b):
    return math.gcd(abs(a), abs(b))

def solve(n, q, a, queries):
    if not a: return []
    pref = [0] * n
    pref[0] = abs(a[0])
    for i in range(1, n):
        pref[i] = gcd(pref[i-1], a[i])
    return [pref[r] for r in queries]

def make_test_case(n, q, a, queries):
    res = solve(n, q, a, queries)
    inp = f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(map(str, queries))
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
        "problem_id": "NUM_CLASSROOM_GCD_PREFIX_QUERIES__4821",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(3, 3, [12, 18, 6], [0, 1, 2]))

    # Public
    tc["public"].append(make_test_case(1, 1, [100], [0]))
    tc["public"].append(make_test_case(5, 2, [10, 20, 30, 40, 50], [2, 4]))
    tc["public"].append(make_test_case(4, 4, [0, 0, 5, 10], [0, 1, 2, 3]))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1, 1, [0], [0]))
    tc["hidden"].append(make_test_case(1, 1, [10**9], [0]))
    tc["hidden"].append(make_test_case(1, 1, [-10**9], [0]))
    tc["hidden"].append(make_test_case(2, 2, [7, 7], [0, 1]))
    tc["hidden"].append(make_test_case(5, 5, [0, 0, 0, 0, 0], [0, 1, 2, 3, 4]))

    # Boundary Cases
    tc["hidden"].append(make_test_case(2, 1, [10**9, 10**9-1], [1]))
    tc["hidden"].append(make_test_case(3, 3, [1, 2, 3], [0, 1, 2]))

    # Negative/Zero Cases (Handling GCD with zero)
    tc["hidden"].append(make_test_case(4, 4, [0, 5, 0, 10], [0, 1, 2, 3]))
    tc["hidden"].append(make_test_case(3, 1, [-12, -18, -6], [2]))

    # Special Constraint Cases (Large GCDs, primes)
    tc["hidden"].append(make_test_case(5, 3, [30030, 60060, 90090, 120120, 150150], [0, 2, 4])) # Multiples of 2*3*5*7*11*13
    tc["hidden"].append(make_test_case(4, 2, [999999937, 999999937, 0, 999999937], [1, 3])) # Large prime

    # Normal Cases
    for _ in range(5):
        n = random.randint(10, 50)
        q = random.randint(5, 20)
        a = [random.randint(-1000, 1000) for _ in range(n)]
        queries = [random.randint(0, n-1) for _ in range(q)]
        tc["hidden"].append(make_test_case(n, q, a, queries))

    # Stress Case
    n_stress = 200000
    q_stress = 5
    a_stress = [random.randint(1, 10**9) for _ in range(n_stress)]
    queries_stress = [0, n_stress//2, n_stress-1]
    tc["hidden"].append(make_test_case(n_stress, len(queries_stress), a_stress, queries_stress))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
