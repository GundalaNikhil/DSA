import math
import yaml
import random

def solve(T, lam, times):
    total = 0
    for t_i in times:
        total += math.exp(-lam * (T - t_i))
    return total

def make_test_case(T, lam, times):
    res = solve(T, lam, times)
    return {
        "input": f"{T} {lam} {len(times)}\n" + " ".join(map(str, times)),
        "output": f"{res:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(10, 0.1, [10, 8, 5])
        ],
        "public": [
            make_test_case(0, 0.5, [0]),
            make_test_case(100, 1.0, [100, 99, 98]),
            make_test_case(100, 0.01, [100, 50, 0])
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(10**9, 0.0001, [10**9, 0]))
    tc["hidden"].append(make_test_case(1, 1.0, [0]))
    
    # Random cases
    for _ in range(5):
        T = random.randint(100, 1000)
        lam = random.uniform(0.01, 0.5)
        m = random.randint(1, 1000)
        times = [random.randint(0, T) for _ in range(m)]
        tc["hidden"].append(make_test_case(T, lam, times))

    # Stress case
    m_stress = 100000
    T_stress = 10**9
    times_stress = [random.randint(T_stress - 1000, T_stress) for _ in range(m_stress)]
    tc["hidden"].append(make_test_case(T_stress, 0.1, times_stress))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
