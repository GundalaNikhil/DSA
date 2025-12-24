import math
import yaml
import random

def solve(epsilon, delta):
    w = math.ceil(math.e / epsilon)
    d = math.ceil(math.log(1.0 / delta))
    return w, d

def make_test_case(epsilon, delta):
    w, d = solve(epsilon, delta)
    return {
        "input": f"{epsilon} {delta}",
        "output": f"{w} {d}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(0.01, 0.01)
        ],
        "public": [
            make_test_case(0.05, 0.05),
            make_test_case(0.001, 0.001),
            make_test_case(0.1, 0.01)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(0.5, 0.5))
    tc["hidden"].append(make_test_case(0.0001, 0.0001))
    
    # Random cases
    for _ in range(5):
        epsilon = random.uniform(0.0001, 0.1)
        delta = random.uniform(0.0001, 0.1)
        tc["hidden"].append(make_test_case(epsilon, delta))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
