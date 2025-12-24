import random
import yaml

def solve(n, values, k):
    if n == 0:
        return []
    k = k % n
    return values[k:] + values[:k]

def make_test_case(values, k):
    n = len(values)
    res = solve(n, values, k)
    input_str = f"{n}\n" + " ".join(map(str, values)) + f"\n{k}"
    output_str = " ".join(map(str, res))
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([4, 9, 1, 7], 3)
        ],
        "public": [
            make_test_case([1, 2, 3, 4, 5], 0),
            make_test_case([1, 2, 3, 4, 5], 5),
            make_test_case([1, 2, 3, 4, 5], 11)
        ],
        "hidden": []
    }

    # Edge cases: n=1, Large k
    tc["hidden"].append(make_test_case([100], 10**9))
    
    # Boundary cases: k = n-1
    tc["hidden"].append(make_test_case([i for i in range(100)], 99))

    # Large random case
    n_large = 100000
    values_large = [random.randint(-10**9, 10**9) for _ in range(n_large)]
    k_large = random.randint(0, 10**9)
    tc["hidden"].append(make_test_case(values_large, k_large))

    # Another large random case
    tc["hidden"].append(make_test_case(values_large, random.randint(0, 10**9)))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
