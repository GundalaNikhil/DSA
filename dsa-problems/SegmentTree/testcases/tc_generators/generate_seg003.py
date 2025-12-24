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
            tree[node] = min(tree[2 * node + 1], tree[2 * node + 2])

    def push(node):
        if lazy[node] != 0:
            tree[2 * node + 1] += lazy[node]
            lazy[2 * node + 1] += lazy[node]
            tree[2 * node + 2] += lazy[node]
            lazy[2 * node + 2] += lazy[node]
            lazy[node] = 0

    def update(node, start, end, l, r, val):
        if l > end or r < start: return
        if l <= start and end <= r:
            tree[node] += val
            lazy[node] += val
            return
        push(node)
        mid = (start + end) // 2
        update(2 * node + 1, start, mid, l, r, val)
        update(2 * node + 2, mid + 1, end, l, r, val)
        tree[node] = min(tree[2 * node + 1], tree[2 * node + 2])

    def query(node, start, end, l, r):
        if l > end or r < start: return float('inf')
        if l <= start and end <= r: return tree[node]
        push(node)
        mid = (start + end) // 2
        return min(query(2 * node + 1, start, mid, l, r), query(2 * node + 2, mid + 1, end, l, r))

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
            queries.append(["MIN", l, r])
    return queries

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, q = 3, 2
    a = [3, 1, 4]
    queries = [["ADD", 0, 2, 2], ["MIN", 1, 2]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # 1. Negative values and large updates
    n, q = 10, 5
    a = [random.randint(-10, 10) for _ in range(n)]
    queries = [["ADD", 0, n-1, -10**9], ["MIN", 0, n-1], ["ADD", 1, 3, 2*10**9], ["MIN", 1, 3], ["MIN", 0, n-1]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    # 1. n=1
    test_cases["hidden"].append({"input": f"1 1\n5\nMIN 0 0\n", "output": "5", "category": "edge"})
    
    # 2. Large MIN range
    n, q = 10**5, 2
    a = [10**9] * n
    queries = [["ADD", 0, n-1, -10**9], ["MIN", 0, n-1]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "edge"})

    # Stress Cases
    # 1. Max N, Q
    n, q = 200000, 200000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = generate_queries(n, q)
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-003-range-min-range-add.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
