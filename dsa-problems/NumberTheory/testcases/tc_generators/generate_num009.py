import sys
import random

def pow_mod(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

def solve(a, m, e):
    if m == 1: return 0
    res = 1
    base = a % m
    for digit in e:
        d = int(digit)
        # res = (res^10 * base^d) % m
        res = pow_mod(res, 10, m)
        res = (res * pow_mod(base, d, m)) % m
    return res

def make_test_case(a, m, e):
    res = solve(a, m, e)
    return {"input": f"{a} {m}\n{e}", "output": str(res)}

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    tc = {
        "problem_id": "NUM_MODULAR_EXPONENT_DIGIT_STREAM__9056",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(3, 7, "5"))

    # Public
    tc["public"].append(make_test_case(2, 10, "3"))
    tc["public"].append(make_test_case(5, 13, "0"))
    tc["public"].append(make_test_case(10, 100, "123"))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1, 1, "12345"))
    tc["hidden"].append(make_test_case(10**9, 10**9, "1"))
    tc["hidden"].append(make_test_case(10**9, 2, "100000"))
    tc["hidden"].append(make_test_case(2, 10**9, "0"))

    # Boundary Cases
    tc["hidden"].append(make_test_case(2, 10**9+7, "1" + "0"*9999))
    tc["hidden"].append(make_test_case(7, 11, "99999"))

    # Special Cases (Large exponents)
    tc["hidden"].append(make_test_case(3, 10**9+7, "123456789"*1000))
    tc["hidden"].append(make_test_case(999999937, 1000000007, "9876543210"*50))

    # Normal Cases
    for _ in range(5):
        a = random.randint(1, 10**9)
        m = random.randint(2, 10**9)
        e_len = random.randint(5, 100)
        e = "".join(str(random.randint(0, 9)) for _ in range(e_len)).lstrip("0")
        if not e: e = "0"
        tc["hidden"].append(make_test_case(a, m, e))

    # Stress Case
    e_max = "9" * 100000
    tc["hidden"].append(make_test_case(12345678, 10**9+7, e_max))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
