import random
import yaml

class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [None] * (4 * n)
        self._build(0, 0, n - 1, a)
        
    def _build(self, node, start, end, a):
        if start == end:
            self.tree[node] = a[start]
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid, a)
        self._build(2 * node + 2, mid + 1, end, a)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        
    def _push(self, node, start, end):
        if self.lazy[node] is not None:
            mid = (start + end) // 2
            self.lazy[2 * node + 1] = self.lazy[node]
            self.tree[2 * node + 1] = (mid - start + 1) * self.lazy[node]
            self.lazy[2 * node + 2] = self.lazy[node]
            self.tree[2 * node + 2] = (end - mid) * self.lazy[node]
            self.lazy[node] = None
            
    def update(self, node, start, end, l, r, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.lazy[node] = val
            self.tree[node] = (end - start + 1) * val
            return
        self._push(node, start, end)
        mid = (start + end) // 2
        self.update(2 * node + 1, start, mid, l, r, val)
        self.update(2 * node + 2, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        self._push(node, start, end)
        mid = (start + end) // 2
        return self.query(2 * node + 1, start, mid, l, r) + self.query(2 * node + 2, mid + 1, end, l, r)

def solve(n, q, a, queries):
    st = SegmentTree(n, a)
    results = []
    for op in queries:
        if op[0] == "SETPREFIX":
            k, x = int(op[1]), int(op[2])
            if k > 0:
                st.update(0, 0, n - 1, 0, k - 1, x)
        else:
            l, r = int(op[1]), int(op[2])
            results.append(str(st.query(0, 0, n - 1, l, r)))
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
    n, q = 3, 2
    a = [1, 2, 3]
    queries = [["SETPREFIX", 2, 5], ["SUM", 0, 2]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # Overlapping prefix updates
    n, q = 5, 4
    a = [0, 0, 0, 0, 0]
    queries = [
        ["SETPREFIX", 3, 10], # [10, 10, 10, 0, 0]
        ["SETPREFIX", 2, 20], # [20, 20, 10, 0, 0]
        ["SUM", 0, 4],        # 50
        ["SUM", 1, 2]         # 30
    ]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    test_cases["hidden"].append({"input": "1 1\n5\nSUM 0 0\n", "output": "5", "category": "edge"})
    
    # Large numbers
    n, q = 3, 1
    a = [10**9, 10**9, 10**9]
    queries = [["SUM", 0, 2]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "boundary"})

    # Stress Case
    n, q = 10000, 10000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = []
    for _ in range(q):
        if random.random() < 0.3:
            queries.append(["SETPREFIX", random.randint(1, n), random.randint(-10**9, 10**9)])
        else:
            l = random.randint(0, n-1)
            r = random.randint(l, n-1)
            queries.append(["SUM", l, r])
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-014-k-smallest-prefix-updates.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
