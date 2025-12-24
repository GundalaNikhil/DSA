import sys
import random

def solve(x):
    s = str(x)
    min_prod = float('inf')
    found = False
    for i in range(1, len(s)):
        p1 = int(s[:i])
        p2 = int(s[i:])
        if p1 * p2 > 0:
            prod = p1 * p2
            if prod < min_prod:
                min_prod = prod
                found = True
    return min_prod if found else float('inf')

def make_test_case(x):
    res = solve(x)
    return {"input": str(x), "output": str(res)}

def print_case(c):
    print("  - input: |-")
    print(f"      {c['input']}")
    print("    output: |-")
    print(f"      {c['output']}")

def main():
    tc = {
        "problem_id": "NUM_MINIMAL_SPLIT_EQUAL_PRODUCT__3562",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(1234))

    # Public
    tc["public"].append(make_test_case(11))
    tc["public"].append(make_test_case(102))
    tc["public"].append(make_test_case(99))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(11))
    tc["hidden"].append(make_test_case(100000000001))
    # Removed 10^12 because it has no non-zero products

    # Boundary Cases
    tc["hidden"].append(make_test_case(12))
    tc["hidden"].append(make_test_case(999999999999))

    # Special Cases
    tc["hidden"].append(make_test_case(105))
    tc["hidden"].append(make_test_case(1005))

    # Normal Cases
    for _ in range(9):
        x = random.randint(11, 10**12-1)
        # Ensure at least one non-zero product
        while solve(x) == float('inf'):
            x = random.randint(11, 10**12-1)
        tc["hidden"].append(make_test_case(x))

    # Stress Case
    tc["hidden"].append(make_test_case(123456789012))
    tc["hidden"].append(make_test_case(908070605040))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
