import random
import yaml
import bisect

def solve(n, q, a, queries):
    # Coordinate compression
    sorted_vals = sorted(list(set(a)))
    rank_map = {v: i for i, v in enumerate(sorted_vals)}
    m = len(sorted_vals)
    
    # Offline queries
    indexed_queries = []
    for i, (r, k) in enumerate(queries):
        indexed_queries.append((r, k, i))
    indexed_queries.sort()
    
    bit = [0] * (m + 1)
    def update(idx, val):
        idx += 1
        while idx <= m:
            bit[idx] += val
            idx += idx & (-idx)
            
    def query_bit(k):
        # Find k-th smallest using BIT binary lifting
        idx = 0
        for i in range(m.bit_length() - 1, -1, -1):
            next_idx = idx + (1 << i)
            if next_idx <= m and bit[next_idx] < k:
                idx = next_idx
                k -= bit[idx]
        return idx # 0-based rank

    results = [None] * q
    curr_r = -1
    for r, k, i in indexed_queries:
        while curr_r < r:
            curr_r += 1
            update(rank_map[a[curr_r]], 1)
        res_rank = query_bit(k)
        results[i] = str(sorted_vals[res_rank])
    return results

def make_test_case(n, q, a, queries):
    input_str = f"{n} {q}\n"
    input_str += " ".join(map(str, a)) + "\n"
    for r, k in queries:
        input_str += f"PREFIX {r} {k}\n"
    output_str = "\n".join(solve(n, q, a, queries))
    return input_str, output_str

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, q = 4, 1
    a = [5, 1, 3, 2]
    queries = [(3, 2)]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # 1. Sorted array
    n, q = 5, 2
    a = [1, 2, 3, 4, 5]
    queries = [(2, 2), (4, 1)] # prefix [1,2,3], 2nd smallest = 2; prefix [1,2,3,4,5], 1st = 1
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    # 1. n=1
    test_cases["hidden"].append({"input": f"1 1\n10\nPREFIX 0 1\n", "output": "10", "category": "edge"})
    
    # 2. Large values, negative values
    n, q = 5, 2
    a = [10**9, -10**9, 0, 5, -5]
    queries = [(4, 1), (4, 5)]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "edge"})

    # Stress Cases
    # 1. Max N, Q
    n, q = 200000, 200000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = []
    for _ in range(q):
        r = random.randint(0, n - 1)
        k = random.randint(1, r + 1)
        queries.append((r, k))
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-005-kth-order-stat-prefix.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
