import sys
import random

def get_digit_sum(x, b):
    s = 0
    temp = x
    while temp > 0:
        s += temp % b
        temp //= b
    return s

def solve(x):
    min_sum = float('inf')
    best_b = 2
    for b in range(2, 37):
        s = get_digit_sum(x, b)
        if s < min_sum:
            min_sum = s
            best_b = b
    return best_b, min_sum

def make_test_case(x):
    b, s = solve(x)
    return {"input": str(x), "output": f"{b} {s}"}

def print_case(c):
    print("  - input: |-")
    print(f"      {c['input']}")
    print("    output: |-")
    print(f"      {c['output']}")

def main():
    tc = {
        "problem_id": "NUM_MINIMAL_BASE_REPRESENTATION__6628",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(31))

    # Public
    tc["public"].append(make_test_case(2))
    tc["public"].append(make_test_case(10))
    tc["public"].append(make_test_case(100))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(2))
    tc["hidden"].append(make_test_case(10**12))
    tc["hidden"].append(make_test_case(36))
    tc["hidden"].append(make_test_case(2**40))

    # Boundary Cases (Powers of bases)
    tc["hidden"].append(make_test_case(2**10))
    tc["hidden"].append(make_test_case(36**4))
    tc["hidden"].append(make_test_case(10**12 - 1))

    # Special Cases (Large primes, values with special patterns)
    tc["hidden"].append(make_test_case(999999999989)) # Large prime
    tc["hidden"].append(make_test_case(123456789012))

    # Normal Cases
    for _ in range(8):
        tc["hidden"].append(make_test_case(random.randint(100, 10**12)))

    # Stress Case
    tc["hidden"].append(make_test_case(10**12))
    tc["hidden"].append(make_test_case(10**12 - 1234567))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
