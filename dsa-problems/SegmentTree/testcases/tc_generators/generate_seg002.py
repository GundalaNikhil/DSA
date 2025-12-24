import random
import yaml

def solve(n, q, a, queries):
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = a[start]
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def push(node, start, end):
        if lazy[node] != 0:
            mid = (start + end) // 2
            tree[2 * node + 1] += lazy[node] * (mid - start + 1)
            lazy[2 * node + 1] += lazy[node]
            tree[2 * node + 2] += lazy[node] * (end - mid)
            lazy[2 * node + 2] += lazy[node]
            lazy[node] = 0

    def update(node, start, end, l, r, val):
        if l > end or r < start: return
        if l <= start and end <= r:
            tree[node] += val * (end - start + 1)
            lazy[node] += val
            return
        push(node, start, end)
        mid = (start + end) // 2
        update(2 * node + 1, start, mid, l, r, val)
        update(2 * node + 2, mid + 1, end, l, r, val)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def query(node, start, end, l, r):
        if l > end or r < start: return 0
        if l <= start and end <= r: return tree[node]
        push(node, start, end)
        mid = (start + end) // 2
        return query(2 * node + 1, start, mid, l, r) + query(2 * node + 2, mid + 1, end, l, r)

    build(0, 0, n - 1)
    results = []
    for op in queries:
        if op[0] == "ADD":
            l, r, x = op[1:]
            update(0, 0, n - 1, l, r, x)
        else:
            l, r = op[1:]
            results.append(str(query(0, 0, n - 1, l, r)))
    return results

def make_test_case(n, q, a, queries):
    input_str = f"{n} {q}\n"
    input_str += " ".join(map(str, a)) + "\n"
    for op in queries:
        input_str += " ".join(map(str, op)) + "\n"
    output_str = "\n".join(solve(n, q, a, queries))
    return input_str, output_str

def generate_queries(n, q, prob_add=0.5):
    queries = []
    for _ in range(q):
        l = random.randint(0, n - 1)
        r = random.randint(l, n - 1)
        if random.random() < prob_add:
            val = random.randint(-10**9, 10**9)
            queries.append(["ADD", l, r, val])
        else:
            queries.append(["SUM", l, r])
    return queries

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, q = 3, 3
    a = [0, 0, 0]
    queries = [["ADD", 0, 1, 5], ["ADD", 1, 2, 2], ["SUM", 0, 2]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # 1. Zero initial, large updates
    n, q = 10, 5
    a = [0] * n
    queries = [["ADD", 0, n-1, 10**9], ["SUM", 0, n-1], ["ADD", 1, 3, -10**9], ["SUM", 0, n-1], ["SUM", 1, 3]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    # 1. n=1
    test_cases["hidden"].append({"input": f"1 1\n5\nSUM 0 0\n", "output": "5", "category": "edge"})
    
    # 2. Large NEGATIVE values
    n, q = 5, 2
    a = [-10**9] * 5
    queries = [["ADD", 0, 4, -10**9], ["SUM", 0, 4]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "edge"})

    # Stress Cases
    # 1. Max N, Q
    n, q = 200000, 200000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = generate_queries(n, q)
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-002-range-add-range-sum.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
