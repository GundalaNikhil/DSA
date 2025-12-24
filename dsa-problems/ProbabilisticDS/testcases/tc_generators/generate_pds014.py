import yaml
import random

def solve(n, sizes):
    s = sum(x*x for x in sizes)
    return s, "YES" if s <= 4*n else "NO"

def make_test_case(n, sizes):
    s, res = solve(n, sizes)
    return {
        "input": f"{n} {len(sizes)}\n" + " ".join(map(str, sizes)),
        "output": f"{s} {res}"
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(6, [2, 1, 3])
        ],
        "public": [
            make_test_case(10, [1]*10),
            make_test_case(10, [10]),
            make_test_case(10, [5, 5])
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case(1, [1]))
    tc["hidden"].append(make_test_case(10**6, [1]*(10**6)))
    tc["hidden"].append(make_test_case(10**6, [10**6]))
    
    # Random cases
    for _ in range(5):
        n = random.randint(100, 1000)
        t = random.randint(1, n)
        # Random partition of n into t buckets
        # Use stars and bars or just simplified
        sizes = [1]*t
        for _ in range(n - t):
            sizes[random.randint(0, t - 1)] += 1
        tc["hidden"].append(make_test_case(n, sizes))

    # Stress case
    n_stress = 1000000
    tc["hidden"].append(make_test_case(n_stress, [1]*n_stress))
    
    # Stress with large buckets
    tc["hidden"].append(make_test_case(n_stress, [n_stress // 2, n_stress // 2]))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
