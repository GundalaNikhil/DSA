import math
import yaml
import random

def solve(m, alpha):
    p_fail = math.exp(-((1 - alpha)**2 * m) / 2.0)
    return 1 - p_fail

def make_test_case(m, alpha):
    p_success = solve(m, alpha)
    return {
        "input": f"{m} {alpha}",
        "output": f"{p_success:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(50, 0.8)
        ],
        "public": [
            make_test_case(100, 0.5),
            make_test_case(1000, 0.9),
            make_test_case(10, 0.1)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(1, 0.5))
    tc["hidden"].append(make_test_case(10**6, 0.99))
    tc["hidden"].append(make_test_case(10**6, 0.01))
    
    # Random cases
    for _ in range(5):
        m = random.randint(100, 1000000)
        alpha = random.uniform(0.1, 0.95)
        tc["hidden"].append(make_test_case(m, alpha))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
