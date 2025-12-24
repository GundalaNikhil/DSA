import yaml
import random

def solve(m, r):
    return m * r, 2.0**(-r)

def make_test_case(m, r):
    mem, fpr = solve(m, r)
    return {
        "input": f"{m} {r}",
        "output": f"{mem} {fpr:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(6, 4)
        ],
        "public": [
            make_test_case(1, 1),
            make_test_case(100, 8),
            make_test_case(1000, 16)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(10**6, 1))
    tc["hidden"].append(make_test_case(10**6, 32))
    tc["hidden"].append(make_test_case(1, 32))
    
    # Random cases
    for _ in range(5):
        m = random.randint(1, 1000000)
        r = random.randint(1, 32)
        tc["hidden"].append(make_test_case(m, r))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
