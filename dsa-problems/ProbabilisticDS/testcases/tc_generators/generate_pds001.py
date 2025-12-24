import math
import random
import yaml

def solve(n, f):
    ln2 = math.log(2)
    m_float = -(n * math.log(f)) / (ln2 ** 2)
    m = math.ceil(m_float)
    k_float = (m / n) * ln2
    k = round(k_float)
    exponent = -(k * n) / m
    fpr = (1 - math.exp(exponent)) ** k
    return m, k, fpr

def make_test_case(n, f):
    m, k, fpr = solve(n, f)
    return {
        "input": f"{n} {f}",
        "output": f"{m} {k} {fpr:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(1000, 0.01)
        ],
        "public": [
            make_test_case(500, 0.05),
            make_test_case(2000, 0.001),
            make_test_case(100, 0.1)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(1, 0.5))
    tc["hidden"].append(make_test_case(1, 0.0001))
    tc["hidden"].append(make_test_case(1000000, 0.01))
    tc["hidden"].append(make_test_case(1000000, 0.000001))

    # Boundary cases
    tc["hidden"].append(make_test_case(10, 0.99))
    tc["hidden"].append(make_test_case(10, 0.01))
    
    # Random cases
    for _ in range(5):
        n = random.randint(100, 1000000)
        f = random.uniform(0.0001, 0.1)
        tc["hidden"].append(make_test_case(n, f))

    # Stress cases
    tc["hidden"].append(make_test_case(10**6, 1e-6))
    tc["hidden"].append(make_test_case(10**6, 1e-9))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
