import math
import yaml
import random

def solve(R):
    phi = 0.77351
    return (2**R) / phi

def make_test_case(R):
    res = solve(R)
    return {
        "input": str(R),
        "output": f"{res:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(4)
        ],
        "public": [
            make_test_case(0),
            make_test_case(1),
            make_test_case(10),
            make_test_case(20)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(30))
    tc["hidden"].append(make_test_case(20))
    tc["hidden"].append(make_test_case(21))
    tc["hidden"].append(make_test_case(22))
    
    # Random cases
    for _ in range(5):
        R = random.randint(0, 30)
        tc["hidden"].append(make_test_case(R))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
