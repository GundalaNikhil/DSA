import random
import yaml

def solve(n, q1, q2):
    return [q2, q1]

def make_test_case(q1, q2):
    n = len(q1)
    res = solve(n, q1, q2)
    input_str = f"{n}\n" + " ".join(map(str, q1)) + "\n" + " ".join(map(str, q2))
    output_str = " ".join(map(str, res[0])) + "\n" + " ".join(map(str, res[1]))
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([4, 5], [7, 8])
        ],
        "public": [
            make_test_case([1], [2]),
            make_test_case([1, 2, 3], [4, 5, 6]),
            make_test_case([10, 20], [30, 40])
        ],
        "hidden": []
    }

    # Edge cases: n=1, large n
    tc["hidden"].append(make_test_case([100], [200]))
    
    # All same in q1, all same in q2
    tc["hidden"].append(make_test_case([1]*100, [2]*100))

    # Large random case
    n_large = 100000
    q1_large = [random.randint(-10**9, 10**9) for _ in range(n_large)]
    q2_large = [random.randint(-10**9, 10**9) for _ in range(n_large)]
    tc["hidden"].append(make_test_case(q1_large, q2_large))

    # Stress case
    tc["hidden"].append(make_test_case([i for i in range(100000)], [100000-i for i in range(100000)]))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
