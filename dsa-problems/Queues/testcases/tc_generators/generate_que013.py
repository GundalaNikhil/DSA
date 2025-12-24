from collections import deque
import random
import yaml

def solve(n, t, k, times):
    queue = deque()
    results = []
    for time in times:
        while queue and queue[0] < time - t:
            queue.popleft()
        
        if len(queue) < k:
            results.append("true")
            queue.append(time)
        else:
            results.append("false")
    return results

def make_test_case(t, k, times):
    n = len(times)
    res = solve(n, t, k, times)
    input_str = f"{n} {t} {k}\n" + " ".join(map(str, times))
    output_str = " ".join(res)
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(4, 1, [2, 4, 6, 9])
        ],
        "public": [
            make_test_case(1, 1, [1, 1, 1, 2, 2]),
            make_test_case(10, 10, [i for i in range(10)]),
            make_test_case(5, 2, [0, 1, 2, 3, 4, 10, 11, 12])
        ],
        "hidden": []
    }

    # Edge cases: k=1, k=n, t=1, t=10^9
    tc["hidden"].append(make_test_case(10**9, 1, [1, 10**8, 10**9]))
    tc["hidden"].append(make_test_case(1, 100, [0] * 100))
    
    # Large n
    n_large = 100000
    times_large = sorted([random.randint(0, 10**9) for _ in range(n_large)])
    tc["hidden"].append(make_test_case(random.randint(1, 1000), random.randint(1, 100), times_large))

    # All allowed
    tc["hidden"].append(make_test_case(1, 1, [i*2 for i in range(1000)]))

    # All but first k rejected
    tc["hidden"].append(make_test_case(1000, 10, [1] * 1000))

    # Stress case
    tc["hidden"].append(make_test_case(10**6, 500, sorted([random.randint(0, 10**9) for _ in range(100000)])))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
