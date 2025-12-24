import random
import yaml

def solve(values):
    n = len(values)
    l, r = 0, n - 1
    res = []
    turn = 0
    while l <= r:
        if turn % 2 == 0:
            res.append(values[l])
            l += 1
        else:
            res.append(values[r])
            r -= 1
        turn += 1
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
            make_test_case([2, 4, 6, 8])
        ],
        "public": [
            make_test_case([1]),
            make_test_case([1, 2, 3]),
            make_test_case([10, 20, 30, 40, 50])
        ],
        "hidden": []
    }

    # Edge cases: n=1, Large odd/even n
    tc["hidden"].append(make_test_case([i for i in range(100)]))
    tc["hidden"].append(make_test_case([i for i in range(101)]))
    
    # Large sequence
    n_large = 100000
    values_large = [random.randint(-10**9, 10**9) for _ in range(n_large)]
    tc["hidden"].append(make_test_case(values_large))

    # All same values
    tc["hidden"].append(make_test_case([7] * 1000))

    # Stress case
    tc["hidden"].append(make_test_case([abs(i) % 1000000 for i in range(100000)]))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
