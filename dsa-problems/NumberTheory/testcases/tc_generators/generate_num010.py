import sys
import random

def get_sigma(n):
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            s[j] += i
    return s

# Precompute
MAX_R = 1000000
sigma_table = get_sigma(MAX_R)
pref_sigma = [0] * (MAX_R + 1)
MOD = 1000000007
for i in range(1, MAX_R + 1):
    pref_sigma[i] = (pref_sigma[i-1] + sigma_table[i]) % MOD

def solve(L, R):
    return (pref_sigma[R] - pref_sigma[L-1] + MOD) % MOD

def make_test_case(L, R):
    res = solve(L, R)
    return {"input": f"{L} {R}", "output": str(res)}

def print_case(c):
    print("  - input: |-")
    print(f"      {c['input']}")
    print("    output: |-")
    print(f"      {c['output']}")

def main():
    tc = {
        "problem_id": "NUM_SUM_DIVISORS_RANGE__4175",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(2, 4))

    # Public
    tc["public"].append(make_test_case(1, 1))
    tc["public"].append(make_test_case(1, 10))
    tc["public"].append(make_test_case(100, 200))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1, 1))
    tc["hidden"].append(make_test_case(MAX_R, MAX_R))
    tc["hidden"].append(make_test_case(1, MAX_R))
    
    # Boundary Cases
    tc["hidden"].append(make_test_case(MAX_R-1, MAX_R))
    tc["hidden"].append(make_test_case(10**5, 10**5+1))

    # Special Cases (Large ranges)
    tc["hidden"].append(make_test_case(500000, 1000000))
    tc["hidden"].append(make_test_case(1, 500000))

    # Normal Cases
    for _ in range(8):
        L = random.randint(1, MAX_R)
        R = random.randint(L, MAX_R)
        tc["hidden"].append(make_test_case(L, R))

    # Stress Case
    tc["hidden"].append(make_test_case(1, 1000000))
    tc["hidden"].append(make_test_case(999999, 1000000))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
