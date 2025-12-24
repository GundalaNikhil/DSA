import random
import yaml

class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.tree = [(float('inf'), -1)] * (4 * n)
        self._build(0, 0, n - 1, a)
        
    def _build(self, node, start, end, a):
        if start == end:
            self.tree[node] = (a[start], start)
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid, a)
        self._build(2 * node + 2, mid + 1, end, a)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])
        
    def _merge(self, a, b):
        if a[0] < b[0]: return a
        if b[0] < a[0]: return b
        return a if a[1] <= b[1] else b
        
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = (val, idx)
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])
        
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return (float('inf'), -1)
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        q1 = self.query(2 * node + 1, start, mid, l, r)
        q2 = self.query(2 * node + 2, mid + 1, end, l, r)
        return self._merge(q1, q2)

def solve(n, q, a, queries):
    st = SegmentTree(n, a)
    results = []
    for op in queries:
        if op[0] == "SET":
            idx, val = int(op[1]), int(op[2])
            st.update(0, 0, n - 1, idx, val)
        else:
            l, r = int(op[1]), int(op[2])
            results.append(str(st.query(0, 0, n - 1, l, r)[1]))
    return results

def make_test_case(n, q, a, queries):
    input_str = f"{n} {q}\n"
    input_str += " ".join(map(str, a)) + "\n"
    for op in queries:
        input_str += " ".join(map(str, op)) + "\n"
    output_str = "\n".join(solve(n, q, a, queries))
    return input_str, output_str

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, q = 3, 1
    a = [4, 2, 2]
    queries = [["MINIDX", 0, 2]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # Multiple updates and same values
    n, q = 5, 3
    a = [10, 5, 10, 5, 10]
    queries = [
        ["MINIDX", 0, 4], # idx 1
        ["SET", 1, 10],   # a = [10, 10, 10, 5, 10]
        ["MINIDX", 0, 4]  # idx 3
    ]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    test_cases["hidden"].append({"input": "1 1\n5\nMINIDX 0 0\n", "output": "0", "category": "edge"})
    
    # Large values
    n, q = 3, 1
    a = [10**18, 10**18, 10**18]
    queries = [["MINIDX", 0, 2]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "boundary"})

    # Stress Case
    n, q = 10000, 10000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = []
    for _ in range(q):
        if random.random() < 0.3:
            queries.append(["SET", random.randint(0, n-1), random.randint(-10**9, 10**9)])
        else:
            l = random.randint(0, n-1)
            r = random.randint(l, n-1)
            queries.append(["MINIDX", l, r])
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-011-range-min-index.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
