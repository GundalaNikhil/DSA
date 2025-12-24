import math
import yaml
import random

def solve(m, k, c, n):
    lam = (k * n) / m
    max_val = (1 << c) - 1
    prob_sum = 0
    term = math.exp(-lam)
    for i in range(max_val + 1):
        prob_sum += term
        term = term * lam / (i + 1)
    return 1 - prob_sum

def make_test_case(m, k, c, n):
    prob = solve(m, k, c, n)
    return {
        "input": f"{m} {k} {c} {n}",
        "output": f"{prob:.15f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(1000, 3, 4, 500)
        ],
        "public": [
            make_test_case(500, 2, 3, 200),
            make_test_case(1000, 4, 5, 1000),
            make_test_case(2000, 5, 2, 500)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(1, 1, 1, 1))
    tc["hidden"].append(make_test_case(10**6, 20, 10, 10**6))
    tc["hidden"].append(make_test_case(10**6, 1, 1, 1))
    
    # Large lambda (should be close to 1)
    tc["hidden"].append(make_test_case(100, 20, 1, 1000))
    
    # Small lambda (should be close to 0)
    tc["hidden"].append(make_test_case(1000000, 1, 4, 100))

    # Random cases
    for _ in range(5):
        m = random.randint(100, 100000)
        k = random.randint(1, 10)
        c = random.randint(1, 4)
        n = random.randint(100, 100000)
        tc["hidden"].append(make_test_case(m, k, c, n))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
