import yaml
import random

def solve(count, sign):
    vals = [c * m for c, m in zip(count, sign)]
    vals.sort()
    return vals[len(vals) // 2]

def make_test_case(count, sign):
    res = solve(count, sign)
    d = len(count)
    input_str = f"{d}\n" + "\n".join(f"{count[i]} {sign[i]}" for i in range(d))
    return {
        "input": input_str,
        "output": str(res)
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([10, 9, 11], [1, -1, 1])
        ],
        "public": [
            make_test_case([5, 5, 5], [1, 1, 1]),
            make_test_case([100], [1]),
            make_test_case([10, 20, 30, 40, 50], [1, -1, 1, -1, 1])
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case([0, 0, 0], [1, -1, 1]))
    tc["hidden"].append(make_test_case([10**9, 10**9, 10**9], [1, 1, 1]))
    
    # Boundary cases: All same signs, mixed signs
    tc["hidden"].append(make_test_case([1, 2, 3, 4, 5], [1]*5))
    tc["hidden"].append(make_test_case([1, 2, 3, 4, 5], [-1]*5))
    
    # Random cases
    for _ in range(5):
        d = random.choice(range(1, 101, 2))
        counts = [random.randint(-1000, 1000) for _ in range(d)]
        signs = [random.choice([1, -1]) for _ in range(d)]
        tc["hidden"].append(make_test_case(counts, signs))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
