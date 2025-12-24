import random
import yaml
from collections import Counter

def solve(n, q, a, queries):
    results = []
    for l, r, t in queries:
        # Brute force for ground truth
        subarray = a[l:r+1]
        counts = Counter(subarray)
        
        best_val = -1
        max_f = -1
        
        for v, f in counts.items():
            if f >= t:
                if f > max_f:
                    max_f = f
                    best_val = v
                elif f == max_f:
                    if best_val == -1 or v < best_val:
                        best_val = v
        results.append(str(best_val))
    return results

def make_test_case(n, q, a, queries):
    input_str = f"{n} {q}\n"
    input_str += " ".join(map(str, a)) + "\n"
    for op in queries:
        input_str += f"MAJ {op[0]} {op[1]} {op[2]}\n"
    output_str = "\n".join(solve(n, q, a, queries))
    return input_str, output_str

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, q = 5, 1
    a = [1, 1, 2, 3, 1]
    queries = [(0, 4, 3)]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # 1. Multiple candidates
    # In [1, 2, 1, 2, 3], both 1 and 2 appear twice.
    # T=2 should give 1 (smallest of 1 and 2).
    n, q = 5, 2
    a = [1, 2, 1, 2, 3]
    queries = [(0, 4, 2), (0, 4, 3)]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # 1. Negative values
    n, q = 5, 1
    a = [-1, -1, -2, -2, -1]
    queries = [(0, 4, 3)]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "negative"})
    
    # 2. No majority (T > L)
    test_cases["hidden"].append({"input": "3 1\n1 2 3\nMAJ 0 2 2\n", "output": "-1", "category": "edge"})

    # Stress Case
    # Increase N, Q slightly but keep it manageable for brute force
    n, q = 2000, 2000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    # Create some actual majorities (> L/2)
    majorities = [random.randint(-10**9, 10**9) for _ in range(50)]
    for v in majorities:
        for _ in range(random.randint(20, 100)):
            a[random.randint(0, n-1)] = v
            
    queries = []
    for _ in range(q):
        l = random.randint(0, n-1)
        r = random.randint(l, n-1)
        length = r - l + 1
        # T is chosen to be majority-like (around L/2) to suit Misra-Gries
        t = random.randint(length // 2, length)
        if t == 0: t = 1
        queries.append((l, r, t))
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-009-range-t-threshold-majority.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
