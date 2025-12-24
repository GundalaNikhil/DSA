import math
import yaml
import random

def solve(n, b):
    cells = math.ceil(1.23 * n)
    return cells * b, 2.0**(-b)

def make_test_case(n, b):
    mem, fpr = solve(n, b)
    return {
        "input": f"{n} {b}",
        "output": f"{mem} {fpr:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(1000, 8)
        ],
        "public": [
            make_test_case(100, 4),
            make_test_case(500, 10),
            make_test_case(1, 1)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(10**6, 1))
    tc["hidden"].append(make_test_case(10**6, 16))
    tc["hidden"].append(make_test_case(1, 16))
    
    # Boundary cases: n that makes 1.23*n have a fractional part close to .0 or .999
    tc["hidden"].append(make_test_case(100, 8)) # 123.0
    tc["hidden"].append(make_test_case(81, 8)) # 1.23 * 81 = 99.63
    
    # Random cases
    for _ in range(5):
        n = random.randint(1, 1000000)
        b = random.randint(1, 16)
        tc["hidden"].append(make_test_case(n, b))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
