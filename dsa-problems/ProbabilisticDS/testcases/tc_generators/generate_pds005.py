import yaml
import random

def solve(stream, k):
    counters = {}
    for x in stream:
        if x in counters:
            counters[x] += 1
        elif len(counters) < k - 1:
            counters[x] = 1
        else:
            to_remove = []
            for key in counters:
                counters[key] -= 1
                if counters[key] == 0:
                    to_remove.append(key)
            for key in to_remove:
                del counters[key]
    return sorted(list(counters.keys()))

def make_test_case(stream, k):
    res = solve(stream, k)
    return {
        "input": f"{len(stream)} {k}\n" + " ".join(map(str, stream)),
        "output": " ".join(map(str, res))
    }

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([1, 2, 1, 3, 1, 2, 4], 3)
        ],
        "public": [
            make_test_case([1, 1, 1, 1, 1], 2),
            make_test_case([1, 2, 3, 4, 1, 2, 3, 4], 4),
            make_test_case([10, 20, 10, 30, 10, 40], 3)
        ],
        "hidden": []
    }

    # Edge cases
    tc["hidden"].append(make_test_case([5], 2))
    tc["hidden"].append(make_test_case([1, 2, 3, 4, 5], 10))
    tc["hidden"].append(make_test_case([1, 2, 3, 4, 5], 2)) # Should be empty or small
    
    # Boundary cases
    tc["hidden"].append(make_test_case([10**9] * 5, 2))
    
    # Large n, small k (Stress)
    n_stress = 100000
    k_stress = 10
    stream_stress = [random.randint(1, 100) for _ in range(n_stress)]
    tc["hidden"].append(make_test_case(stream_stress, k_stress))

    # Large k
    tc["hidden"].append(make_test_case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1000))

    # All items different, small k
    tc["hidden"].append(make_test_case(list(range(100)), 5))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
