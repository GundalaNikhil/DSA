import math
import yaml
import random

def solve(m, a, b):
    if m == 16:
        alpha = 0.673
    elif m == 32:
        alpha = 0.697
    elif m == 64:
        alpha = 0.709
    else:
        alpha = 0.7213 / (1 + 1.079 / m)
    
    total_sum = 0
    for i in range(m):
        r = max(a[i], b[i])
        total_sum += math.pow(2, -r)
    
    return alpha * (m ** 2) / total_sum

def make_test_case(a, b):
    m = len(a)
    e = solve(m, a, b)
    return {
        "input": f"{m}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, b)),
        "output": f"{e:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([1]*16, [2]*16)
        ],
        "public": [
            make_test_case([0]*16, [0]*16),
            make_test_case([1]*32, [1]*32),
            make_test_case([1, 2]*8, [2, 1]*8)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case([0]*16, [20]*16))
    tc["hidden"].append(make_test_case([10]*65536, [5]*65536))
    
    # Random cases
    for m in [16, 128, 1024]:
        a = [random.randint(0, 10) for _ in range(m)]
        b = [random.randint(0, 10) for _ in range(m)]
        tc["hidden"].append(make_test_case(a, b))

    # Stress case
    m_stress = 65536
    a_stress = [random.randint(0, 20) for _ in range(m_stress)]
    b_stress = [random.randint(0, 20) for _ in range(m_stress)]
    tc["hidden"].append(make_test_case(a_stress, b_stress))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
