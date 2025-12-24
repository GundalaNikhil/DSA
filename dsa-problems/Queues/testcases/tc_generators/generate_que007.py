import random
import yaml
import bisect
from collections import deque

def solve(n, k, values):
    if n == 0 or k == 0:
        return []
        
    results = []
    
    # For max and min
    max_dq = deque()
    min_dq = deque()
    
    # For median (using sorted list for simplicity in generator)
    window = sorted(values[:k])
    
    def get_instability(idx):
        nonlocal max_dq, min_dq
        
        # Max/Min are handled by the sliding window loop
        # But we need them for the current window [idx-k+1, idx]
        # Actually it's easier to just calculate for each window in generator
        win = values[idx-k+1 : idx+1]
        v_max = max(win)
        v_min = min(win)
        
        # Median
        median = window[(k-1)//2]
        
        if median == 0:
            return 0
        return (v_max - v_min) // median

    for i in range(n):
        if i >= k:
            # Remove values[i-k] from sorted window
            old_val = values[i-k]
            idx_to_remove = bisect.bisect_left(window, old_val)
            window.pop(idx_to_remove)
            # Add values[i]
            bisect.insort(window, values[i])
        
        if i >= k - 1:
            win = values[i-k+1 : i+1]
            v_max = max(win)
            v_min = min(win)
            median = window[(k-1)//2]
            if median == 0:
                results.append(0)
            else:
                results.append((v_max - v_min) // median)
                
    return results

def make_test_case(n, k, values):
    res = solve(n, k, values)
    input_str = f"{n} {k}\n" + " ".join(map(str, values))
    output_str = " ".join(map(str, res))
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(5, 3, [5, 1, 4, 6, 2])
        ],
        "public": [
            make_test_case(3, 1, [10, 20, 30]),
            make_test_case(4, 2, [1, 2, 3, 4]),
            make_test_case(6, 3, [0, 0, 0, 0, 0, 0])
        ],
        "hidden": []
    }

    # Edge cases: k=1, k=n
    tc["hidden"].append(make_test_case(10, 1, [random.randint(1, 100) for _ in range(10)]))
    tc["hidden"].append(make_test_case(10, 10, [random.randint(1, 100) for _ in range(10)]))
    
    # Zero median case
    tc["hidden"].append(make_test_case(10, 3, [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]))

    # Large sequence (smaller for generator performance but valid complexity)
    n_large = 50000
    k_large = 1000
    values_large = [random.randint(1, 1000000) for _ in range(n_large)]
    tc["hidden"].append(make_test_case(n_large, k_large, values_large))

    # Stress case with negative values (Wait, constraints say 32-bit signed integer, can they be negative?)
    # Problem statement says sensors, usually non-negative but let's include some negatives.
    values_rand = [random.randint(-1000, 1000) for _ in range(1000)]
    tc["hidden"].append(make_test_case(1000, 100, values_rand))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
