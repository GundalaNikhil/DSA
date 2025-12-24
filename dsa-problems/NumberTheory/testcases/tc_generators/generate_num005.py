import sys
import random

def fact(n, p):
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % p
    return res

def solve(n, p):
    k = n // p
    rem = int(n % p)
    res = fact(rem, p)
    if k % 2 == 1:
        res = (p - res) % p
    return res

def make_test_case(n, p):
    res = solve(n, p)
    return {"input": f"{n} {p}", "output": str(res)}

def print_case(c):
    print("  - input: |-")
    print(f"      {c['input']}")
    print("    output: |-")
    print(f"      {c['output']}")

def main():
    tc = {
        "problem_id": "NUM_FACTORIALS_MISSING_PRIMES__2941",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(6, 5))

    # Public
    tc["public"].append(make_test_case(10, 5))
    tc["public"].append(make_test_case(4, 7))
    tc["public"].append(make_test_case(1, 2))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1, 1000003)) # Large prime
    tc["hidden"].append(make_test_case(10**12, 2))
    tc["hidden"].append(make_test_case(10**12, 1000003))
    
    # Boundary Cases
    tc["hidden"].append(make_test_case(5, 5))
    tc["hidden"].append(make_test_case(4, 5))
    tc["hidden"].append(make_test_case(10, 3))

    # Special Constraint Cases (p is large prime)
    large_p = 999983 # prime < 10^6
    tc["hidden"].append(make_test_case(large_p, large_p))
    tc["hidden"].append(make_test_case(large_p + 5, large_p))

    # Normal Cases
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for _ in range(5):
        p = random.choice(primes)
        n = random.randint(1, 1000)
        tc["hidden"].append(make_test_case(n, p))

    for _ in range(5):
        p = 1000003 # Large prime
        n = random.randint(10**10, 10**12)
        tc["hidden"].append(make_test_case(n, p))

    # Stress Case
    tc["hidden"].append(make_test_case(10**12, 999983))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
