import sys
import random

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solve_crt(a_list, m_list):
    if not a_list: return 0
    
    x1, m1 = a_list[0], m_list[0]
    for i in range(1, len(a_list)):
        a2, m2 = a_list[i], m_list[i]
        
        # Solving k*m1 = a2 - x1 (mod m2)
        g, k1, k2 = gcd_extended(m1, m2)
        diff = a2 - x1
        if diff % g != 0:
            return None
        
        # x = x1 + (diff // g) * k1 * m1
        mod = m2 // g
        k = ((diff // g) % mod * (k1 % mod) + mod) % mod
        
        new_m = (m1 * m2) // g
        x1 = (x1 + k * m1) % new_m
        m1 = new_m
        
    return x1

def make_test_case(a, m):
    res = solve_crt(a, m)
    inp = f"{len(a)}\n" + "\n".join(f"{ai} {mi}" for ai, mi in zip(a, m))
    out = "NO" if res is None else str(res)
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
        "problem_id": "NUM_CRT_EXISTENCE_VALUE__5186",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case([2, 5], [6, 9]))

    # Public
    tc["public"].append(make_test_case([2, 5, 2], [3, 7, 5])) # coprime
    tc["public"].append(make_test_case([2, 5], [6, 12])) # no solution: x % 6=2 implies x % 2 = 0; x % 12=5 implies x % 2 = 1.

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case([0], [10**9]))
    tc["hidden"].append(make_test_case([123], [10**9]))
    tc["hidden"].append(make_test_case([0]*10, [1]*10)) # Smallest non-negative mod 1 is 0

    # Boundary Cases
    tc["hidden"].append(make_test_case([1, 1], [10**9, 10**9-1]))

    # No Solution Cases
    tc["hidden"].append(make_test_case([1, 2], [2, 4]))
    tc["hidden"].append(make_test_case([1, 2, 3], [10, 10, 10]))

    # Special Cases (Large primes, large result)
    tc["hidden"].append(make_test_case([1, 1, 1], [999999937, 1000000007, 1000000009])) # Large result? all 1s -> 1.
    tc["hidden"].append(make_test_case([10, 20, 30], [999999937, 1000000007, 1000000009]))

    # Normal Cases
    for _ in range(5):
        k = random.randint(2, 5)
        m = [random.randint(2, 1000) for _ in range(k)]
        a = [random.randint(0, mi - 1) for mi in m]
        tc["hidden"].append(make_test_case(a, m))

    # Stress Case
    k_stress = 4 # Keep LCM within __int128 range (~10^38)
    m_stress = [random.randint(10**8, 10**9) for _ in range(k_stress)]
    a_stress = [random.randint(0, mi - 1) for mi in m_stress]
    tc["hidden"].append(make_test_case(a_stress, m_stress))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
