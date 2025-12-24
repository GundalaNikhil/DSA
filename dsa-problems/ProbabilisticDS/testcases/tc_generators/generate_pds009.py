import yaml
import random

def solve(hashes):
    k = len(hashes)
    return (k - 1) / hashes[k - 1]

def make_test_case(hashes):
    res = solve(hashes)
    return {
        "input": f"{len(hashes)}\n" + " ".join(map(str, hashes)),
        "output": f"{res:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([0.1, 0.2, 0.4])
        ],
        "public": [
            make_test_case([0.01, 0.02]),
            make_test_case([0.1, 0.2, 0.3, 0.4, 0.5]),
            make_test_case([0.001, 0.002, 0.005, 0.01])
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case([0.1, 0.99999]))
    tc["hidden"].append(make_test_case([0.00001, 0.00002]))
    
    # Random cases
    for _ in range(5):
        k = random.randint(2, 100)
        hashes = sorted([random.random() for _ in range(k)])
        while hashes[-1] == 0: # Ensure valid denominator
             hashes = sorted([random.random() for _ in range(k)])
        tc["hidden"].append(make_test_case(hashes))

    # Stress case
    k_stress = 100000
    hashes_stress = sorted([random.uniform(0.1, 0.9) for _ in range(k_stress)])
    tc["hidden"].append(make_test_case(hashes_stress))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
