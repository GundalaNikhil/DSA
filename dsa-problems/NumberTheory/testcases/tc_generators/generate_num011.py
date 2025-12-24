import sys
import random

def solve(n, jumps):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    jumps_sorted = sorted(list(set(jumps)))
    for i in range(1, n + 1):
        for j in jumps_sorted:
            if i >= j:
                dp[i] = (dp[i] + dp[i-j]) % MOD
            else:
                break
    return dp[n]

def make_test_case(n, jumps):
    res = solve(n, jumps)
    inp = f"{n} {len(jumps)}\n" + " ".join(map(str, jumps))
    out = str(res)
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
        "problem_id": "NUM_WAYS_CLIMB_JUMP_SET__7681",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(4, [1, 3]))

    # Public
    tc["public"].append(make_test_case(1, [1]))
    tc["public"].append(make_test_case(1, [2])) # Impossible
    tc["public"].append(make_test_case(10, [1, 2]))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1, [1]))
    tc["hidden"].append(make_test_case(1, [100000]))
    tc["hidden"].append(make_test_case(100000, [100001])) # Impossible
    tc["hidden"].append(make_test_case(100000, [1]))

    # Boundary Cases
    tc["hidden"].append(make_test_case(100000, [1, 2]))
    tc["hidden"].append(make_test_case(100000, list(range(1, 21))))

    # Negative/Impossible Cases
    tc["hidden"].append(make_test_case(5, [2, 4])) # Only evens
    tc["hidden"].append(make_test_case(100, [3, 7])) # Multiples of... not exactly, but GCD issues

    # Special Cases (Large jump sizes)
    tc["hidden"].append(make_test_case(100000, [50000, 100000]))
    tc["hidden"].append(make_test_case(100000, [1, 100000]))

    # Normal Cases
    for _ in range(5):
        n = random.randint(100, 1000)
        m = random.randint(1, 10)
        jumps = random.sample(range(1, 50), m)
        tc["hidden"].append(make_test_case(n, jumps))

    # Stress Case
    tc["hidden"].append(make_test_case(100000, list(range(1, 21))))
    tc["hidden"].append(make_test_case(100000, random.sample(range(1, 100), 20)))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
