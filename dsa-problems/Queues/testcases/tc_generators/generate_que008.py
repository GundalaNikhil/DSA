import random
import yaml
import bisect

def solve(n, k, values):
    if n == 0 or k == 0:
        return []
    
    results = []
    window = sorted(values[:k])
    
    #定义获取第二小值的辅助函数
    def get_second_min():
        if k == 1:
            return window[0]
        return window[1]

    results.append(get_second_min())
    
    for i in range(k, n):
        # Remove values[i-k]
        old_val = values[i-k]
        idx_to_remove = bisect.bisect_left(window, old_val)
        window.pop(idx_to_remove)
        # Add values[i]
        bisect.insort(window, values[i])
        results.append(get_second_min())
                
    return results

def make_test_case(n, k, values):
    res = solve(n, k, values)
    input_str = f"{n} {k}\n" + " ".join(map(str, values))
    output_str = " ".join(map(str, res))
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(5, 3, [6, 2, 5, 1, 7])
        ],
        "public": [
            make_test_case(3, 1, [10, 20, 30]),
            make_test_case(4, 2, [1, 1, 2, 2]),
            make_test_case(6, 3, [5, 4, 3, 2, 1, 0])
        ],
        "hidden": []
    }

    # Edge cases: k=1, k=n
    tc["hidden"].append(make_test_case(10, 1, [random.randint(1, 100) for _ in range(10)]))
    tc["hidden"].append(make_test_case(10, 10, [random.randint(1, 100) for _ in range(10)]))
    
    # All same values
    tc["hidden"].append(make_test_case(5, 3, [7, 7, 7, 7, 7]))

    # Large random case
    n_large = 50000
    k_large = 1000
    values_large = [random.randint(-10**9, 10**9) for _ in range(n_large)]
    tc["hidden"].append(make_test_case(n_large, k_large, values_large))

    # Stress case
    tc["hidden"].append(make_test_case(1000, 500, [random.randint(-10**9, 10**9) for _ in range(1000)]))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
