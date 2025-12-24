import random
import yaml

def solve(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res

def make_test_case(a, b):
    n, m = len(a), len(b)
    res = solve(a, b)
    input_str = f"{n}\n" + " ".join(map(str, a)) + f"\n{m}\n" + " ".join(map(str, b))
    output_str = " ".join(map(str, res))
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([3, 5, 9], [1, 4, 10])
        ],
        "public": [
            make_test_case([], [1, 2, 3]),
            make_test_case([1, 2, 3], []),
            make_test_case([1, 3, 5], [2, 4, 6])
        ],
        "hidden": []
    }

    # Edge cases: n=0, m=0, Both large
    tc["hidden"].append(make_test_case([], []))
    tc["hidden"].append(make_test_case([10] * 5, [10] * 5))
    
    # Large sequence
    n_large, m_large = 100000, 100000
    a_large = sorted([random.randint(-10**9, 10**9) for _ in range(n_large)])
    b_large = sorted([random.randint(-10**9, 10**9) for _ in range(m_large)])
    tc["hidden"].append(make_test_case(a_large, b_large))

    # Stress case: interwoven
    a_inter = [i * 2 for i in range(50000)]
    b_inter = [i * 2 + 1 for i in range(50000)]
    tc["hidden"].append(make_test_case(a_inter, b_inter))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
