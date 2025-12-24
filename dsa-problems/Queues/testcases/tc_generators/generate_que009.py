from collections import deque
import random
import yaml

def solve(n, k, values):
    queue = deque()
    results = []
    
    for i in range(n):
        if values[i] < 0:
            queue.append(i)
        
        if i >= k - 1:
            while queue and queue[0] <= i - k:
                queue.popleft()
            
            if queue:
                results.append(values[queue[0]])
            else:
                results.append(0)
    return results

def make_test_case(n, k, values):
    res = solve(n, k, values)
    input_str = f"{n} {k}\n" + " ".join(map(str, values))
    output_str = " ".join(map(str, res))
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(5, 2, [5, -2, -7, 3, 4])
        ],
        "public": [
            make_test_case(3, 1, [1, -1, 1]),
            make_test_case(4, 3, [1, 2, 3, 4]),
            make_test_case(6, 3, [-1, -2, -3, -4, -5, -6])
        ],
        "hidden": []
    }

    # Edge cases: k=1, k=n
    tc["hidden"].append(make_test_case(10, 1, [random.randint(-100, 100) for _ in range(10)]))
    tc["hidden"].append(make_test_case(10, 10, [random.randint(-100, 100) for _ in range(10)]))
    
    # Large sequence
    n_large = 100000
    k_large = 1000
    values_large = [random.randint(-1000, 1000) for _ in range(n_large)]
    tc["hidden"].append(make_test_case(n_large, k_large, values_large))

    # All positive
    tc["hidden"].append(make_test_case(100, 10, [i for i in range(1, 101)]))

    # Stress case
    tc["hidden"].append(make_test_case(100000, 50000, [random.randint(-10**9, 10**9) for _ in range(100000)]))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
