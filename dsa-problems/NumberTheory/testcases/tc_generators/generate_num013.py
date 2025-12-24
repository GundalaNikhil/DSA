import sys
import random

MOD = 1000000007
MAX = 1000001
fact = [1] * MAX
inv = [1] * MAX
for i in range(1, MAX):
    fact[i] = (fact[i-1] * i) % MOD

inv[MAX-1] = pow(fact[MAX-1], MOD - 2, MOD)
for i in range(MAX-2, -1, -1):
    inv[i] = (inv[i+1] * (i+1)) % MOD

def nCr(n, k):
    if k < 0 or k > n: return 0
    num = fact[n]
    den = (inv[k] * inv[n-k]) % MOD
    return (num * den) % MOD

def solve(n, k):
    comb = nCr(n, k)
    vowels = pow(5, k, MOD)
    consonants = pow(21, n - k, MOD)
    return (comb * vowels % MOD * consonants % MOD)

def make_test_case(n, k):
    res = solve(n, k)
    return {"input": f"{n} {k}", "output": str(res)}

def print_case(c):
    print("  - input: |-")
    print(f"      {c['input']}")
    print("    output: |-")
    print(f"      {c['output']}")

def main():
    tc = {
        "problem_id": "NUM_COUNT_STRINGS_EXACT_VOWELS__6419",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(2, 1))

    # Public
    tc["public"].append(make_test_case(1, 0))
    tc["public"].append(make_test_case(1, 1))
    tc["public"].append(make_test_case(3, 2))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1000000, 0))
    tc["hidden"].append(make_test_case(1000000, 1000000))
    tc["hidden"].append(make_test_case(1, 0))
    tc["hidden"].append(make_test_case(1, 1))

    # Boundary Cases
    tc["hidden"].append(make_test_case(1000000, 1))
    tc["hidden"].append(make_test_case(1000000, 999999))
    tc["hidden"].append(make_test_case(1000000, 500000))

    # Special Cases
    tc["hidden"].append(make_test_case(42, 7))

    # Normal Cases
    for _ in range(8):
        n = random.randint(10, 1000000)
        k = random.randint(0, n)
        tc["hidden"].append(make_test_case(n, k))

    # Stress Case
    tc["hidden"].append(make_test_case(1000000, 777777))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
