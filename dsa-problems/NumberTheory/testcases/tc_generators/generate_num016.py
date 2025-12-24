import sys
import random

MOD = 1000000007

def nCr_small(n, r):
    if r < 0 or r > n: return 0
    if r == 0 or r == n: return 1
    if r > n // 2: r = n - r
    
    num = 1
    for i in range(r):
        num = num * (n - i) // (i + 1)
    return num % MOD

def solve(n, k):
    res = 0
    for i in range(k + 1):
        term = nCr_small(k, i) * pow(k - i, n, MOD) % MOD
        if i % 2 == 1:
            res = (res - term + MOD) % MOD
        else:
            res = (res + term) % MOD
    return res

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
        "problem_id": "NUM_COUNT_SURJECTIVE_FUNCTIONS__7773",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(3, 2))

    # Public
    tc["public"].append(make_test_case(1, 1))
    tc["public"].append(make_test_case(5, 5))
    tc["public"].append(make_test_case(3, 1))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1, 1))
    tc["hidden"].append(make_test_case(30, 30))
    tc["hidden"].append(make_test_case(30, 1))

    # Boundary Cases
    tc["hidden"].append(make_test_case(30, 15))
    tc["hidden"].append(make_test_case(30, 2))

    # Special Cases
    tc["hidden"].append(make_test_case(2, 2))
    tc["hidden"].append(make_test_case(10, 5))

    # Normal Cases
    for _ in range(8):
        k = random.randint(1, 30)
        n = random.randint(k, 30)
        tc["hidden"].append(make_test_case(n, k))

    # Stress Case (Max values)
    tc["hidden"].append(make_test_case(30, 30))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
