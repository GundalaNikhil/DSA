import random
import yaml

def solve(values, k):
    res = values[:k][::-1] + values[k:]
    return res

def make_test_case(values, k):
    n = len(values)
    res = solve(values, k)
    input_str = f"{n}\n" + " ".join(map(str, values)) + f"\n{k}"
    output_str = " ".join(map(str, res))
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([2, 4, 6, 8, 10], 4)
        ],
        "public": [
            make_test_case([1, 2, 3], 1),
            make_test_case([1, 2, 3], 3),
            make_test_case([10, 20, 30, 40], 2)
        ],
        "hidden": []
    }

    # Edge cases: k=1, k=n
    tc["hidden"].append(make_test_case([i for i in range(10)], 1))
    tc["hidden"].append(make_test_case([i for i in range(10)], 10))
    
    # Large sequence
    n_large = 100000
    values_large = [i for i in range(n_large)]
    tc["hidden"].append(make_test_case(values_large, 50000))

    # Random case
    values_rand = [random.randint(-10**9, 10**9) for _ in range(1000)]
    tc["hidden"].append(make_test_case(values_rand, random.randint(1, 1000)))

    # Large random case
    values_large_rand = [random.randint(-10**9, 10**9) for _ in range(100000)]
    tc["hidden"].append(make_test_case(values_large_rand, random.randint(1, 100000)))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
