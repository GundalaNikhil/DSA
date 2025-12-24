import sys
import random
import math

def solve(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return math.gcd(dx, dy) + 1

def make_test_case(x1, y1, x2, y2):
    res = solve(x1, y1, x2, y2)
    return {"input": f"{x1} {y1} {x2} {y2}", "output": str(res)}

def print_case(c):
    print("  - input: |-")
    print(f"      {c['input']}")
    print("    output: |-")
    print(f"      {c['output']}")

def main():
    tc = {
        "problem_id": "NUM_LATTICE_POINTS_ON_SEGMENT__6330",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(0, 0, 6, 4))

    # Public
    tc["public"].append(make_test_case(0, 0, 0, 0))
    tc["public"].append(make_test_case(0, 0, 5, 0))
    tc["public"].append(make_test_case(1, 1, 4, 4))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(0, 0, 0, 0)) # Origin only
    tc["hidden"].append(make_test_case(10**9, 10**9, 10**9, 10**9))
    tc["hidden"].append(make_test_case(-10**9, -10**9, 10**9, 10**9))
    tc["hidden"].append(make_test_case(0, 0, 10**9, 0))
    tc["hidden"].append(make_test_case(0, 0, 0, 10**9))

    # Boundary Cases
    tc["hidden"].append(make_test_case(0, 0, 10**9, 10**9-1))
    tc["hidden"].append(make_test_case(0, 0, 10**9, 10**7))

    # Special Cases (Horizontal, Vertical, Slanted with gcd=1, etc.)
    tc["hidden"].append(make_test_case(-5, -5, -5, 100)) # Vertical
    tc["hidden"].append(make_test_case(-100, 42, 200, 42)) # Horizontal
    tc["hidden"].append(make_test_case(1, 1, 1000000007, 1000000009)) # Slanted gcd=2

    # Normal Cases
    for _ in range(8):
        x1 = random.randint(-10**6, 10**6)
        y1 = random.randint(-10**6, 10**6)
        x2 = random.randint(-10**6, 10**6)
        y2 = random.randint(-10**6, 10**6)
        tc["hidden"].append(make_test_case(x1, y1, x2, y2))

    # Stress Case
    tc["hidden"].append(make_test_case(10**9, 10**9, -10**9, -10**9))
    tc["hidden"].append(make_test_case(10**9, 10**9-1, -10**9, -10**9+1))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
