import math
import yaml
import random

def solve(b, r, s):
    return 1 - (1 - s**r)**b

def make_test_case(b, r, s):
    res = solve(b, r, s)
    return {
        "input": f"{b} {r} {s}",
        "output": f"{res:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(5, 2, 0.5)
        ],
        "public": [
            make_test_case(1, 1, 0.5),
            make_test_case(10, 1, 0.1),
            make_test_case(1, 10, 0.9)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(1000, 1000, 0.5))
    tc["hidden"].append(make_test_case(1000, 1000, 0.99))
    tc["hidden"].append(make_test_case(1000, 1, 1.0))
    tc["hidden"].append(make_test_case(1, 1000, 0.0))
    
    # Boundary cases
    tc["hidden"].append(make_test_case(20, 5, 0.7))
    tc["hidden"].append(make_test_case(100, 10, 0.5))
    
    # Random cases
    for _ in range(5):
        b = random.randint(1, 100)
        r = random.randint(1, 100)
        s = random.random()
        tc["hidden"].append(make_test_case(b, r, s))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
