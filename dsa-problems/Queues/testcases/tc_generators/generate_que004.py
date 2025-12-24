import random
import yaml

def solve(values):
    n = len(values)
    half = n // 2
    first_half = values[:half]
    second_half = values[half:]
    res = []
    for i in range(half):
        res.append(first_half[i])
        res.append(second_half[i])
    return res

def make_test_case(values):
    n = len(values)
    res = solve(values)
    input_str = f"{n}\n" + " ".join(map(str, values))
    output_str = " ".join(map(str, res))
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([11, 12, 13, 14])
        ],
        "public": [
            make_test_case([1, 2]),
            make_test_case([1, 2, 3, 4, 5, 6])
        ],
        "hidden": []
    }

    # Edge cases: Minimum even length
    tc["hidden"].append(make_test_case([10, 20]))
    
    # Large sequence
    n_large = 100000
    values_large = [i for i in range(n_large)]
    tc["hidden"].append(make_test_case(values_large))

    # Random case
    values_rand = [random.randint(-10**9, 10**9) for _ in range(1000)]
    tc["hidden"].append(make_test_case(values_rand))

    # Another large random case
    values_large_rand = [random.randint(-10**9, 10**9) for _ in range(100000)]
    tc["hidden"].append(make_test_case(values_large_rand))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
