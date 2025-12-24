import sys
import random

def get_phi(n):
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi

# Precompute phi once for efficiency if generating many cases
# But N is small enough to do per-case or once for max N.
MAX_N = 100000
phi_table = get_phi(MAX_N)
pref_phi = [0] * (MAX_N + 1)
for i in range(2, MAX_N + 1):
    pref_phi[i] = pref_phi[i-1] + phi_table[i]

def solve(n):
    if n < 2: return 0
    return pref_phi[min(n, MAX_N)]

def make_test_case(n):
    res = solve(n)
    return {"input": str(n), "output": str(res)}

def print_case(c):
    print("  - input: |-")
    print(f"      {c['input']}")
    print("    output: |-")
    print(f"      {c['output']}")

def main():
    tc = {
        "problem_id": "NUM_COPRIME_PAIR_COUNT__7194",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(5))

    # Public
    tc["public"].append(make_test_case(1))
    tc["public"].append(make_test_case(2))
    tc["public"].append(make_test_case(10))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1))
    tc["hidden"].append(make_test_case(3))
    tc["hidden"].append(make_test_case(100000))
    
    # Boundary Cases
    tc["hidden"].append(make_test_case(99999))
    tc["hidden"].append(make_test_case(10000))

    # Negative/Special (though no negative answer exists)
    # N=1 is a good "negative" case in terms of 0 pairs.

    # Normal Cases
    for n in [50, 100, 500, 1000, 5000, 20000, 50000, 75000]:
        tc["hidden"].append(make_test_case(n))
    
    for _ in range(5):
        tc["hidden"].append(make_test_case(random.randint(2, 100000)))

    # Stress Case
    tc["hidden"].append(make_test_case(100000))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
