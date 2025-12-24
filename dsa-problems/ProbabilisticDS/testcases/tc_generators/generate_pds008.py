import yaml
import random

def solve(a, b):
    k = len(a)
    matches = 0
    for i in range(k):
        if a[i] == b[i]:
            matches += 1
    return matches / k

def make_test_case(a, b):
    res = solve(a, b)
    return {
        "input": f"{len(a)}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, b)),
        "output": f"{res:.6f}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([0.1, 0.2, 0.3, 0.4, 0.5], [0.1, 0.25, 0.3, 0.6, 0.7])
        ],
        "public": [
            make_test_case([0.1]*5, [0.1]*5),
            make_test_case([0.1]*5, [0.2]*5),
            make_test_case([0.5, 0.5], [0.5, 0.6])
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case([0.999], [0.999]))
    tc["hidden"].append(make_test_case([0.999], [0.998]))
    
    # Boundary cases: All same, all different
    k = 100
    tc["hidden"].append(make_test_case([0.1]*k, [0.1]*k))
    tc["hidden"].append(make_test_case([0.1]*k, [0.2]*k))
    
    # Random cases
    for _ in range(5):
        k_rand = random.randint(10, 1000)
        a = [round(random.random(), 4) for _ in range(k_rand)]
        b = [a[i] if random.random() < 0.5 else round(random.random(), 4) for i in range(k_rand)]
        tc["hidden"].append(make_test_case(a, b))

    # Stress case
    k_stress = 100000
    a_stress = [round(random.random(), 4) for _ in range(k_stress)]
    b_stress = [a_stress[i] if random.random() < 0.3 else round(random.random(), 4) for i in range(k_stress)]
    tc["hidden"].append(make_test_case(a_stress, b_stress))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
