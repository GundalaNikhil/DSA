import random
import yaml

MOD = 1000000007

class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.tree = [[0, 0, 0] for _ in range(4 * n)]
        self._build(0, 0, n - 1, a)
        
    def _build(self, node, start, end, a):
        if start == end:
            v = a[start] % MOD
            self.tree[node] = [v, (v * v) % MOD, (v * v % MOD * v) % MOD]
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid, a)
        self._build(2 * node + 2, mid + 1, end, a)
        self.tree[node] = [(self.tree[2 * node + 1][i] + self.tree[2 * node + 2][i]) % MOD for i in range(3)]
        
    def update(self, node, start, end, idx, val):
        if start == end:
            v = val % MOD
            self.tree[node] = [v, (v * v) % MOD, (v * v % MOD * v) % MOD]
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = [(self.tree[2 * node + 1][i] + self.tree[2 * node + 2][i]) % MOD for i in range(3)]
        
    def query(self, node, start, end, l, r, p):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node][p-1]
        mid = (start + end) // 2
        q1 = self.query(2 * node + 1, start, mid, l, r, p)
        q2 = self.query(2 * node + 2, mid + 1, end, l, r, p)
        return (q1 + q2) % MOD

def solve(n, q, a, queries):
    st = SegmentTree(n, a)
    results = []
    for op in queries:
        if op[0] == "SET":
            idx, x = int(op[1]), int(op[2])
            st.update(0, 0, n - 1, idx, x)
        else:
            l, r, p = int(op[1]), int(op[2]), int(op[3])
            results.append(str(st.query(0, 0, n - 1, l, r, p)))
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
    n, q = 2, 2
    a = [2, 3]
    queries = [["SUM", 0, 1, 2], ["SUM", 0, 1, 3]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # Negative numbers and updates
    n, q = 3, 3
    a = [-1, 2, -3]
    queries = [
        ["SUM", 0, 2, 2], # (-1)^2 + 2^2 + (-3)^2 = 1+4+9 = 14
        ["SET", 1, 0],    # arr = [-1, 0, -3]
        ["SUM", 0, 2, 3]  # (-1)^3 + 0^3 + (-3)^3 = -1 - 27 = -28 -> 1000000007 - 28
    ]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    test_cases["hidden"].append({"input": "1 1\n5\nSUM 0 0 1\n", "output": "5", "category": "edge"})
    
    # Large numbers and MOD
    n, q = 2, 2
    a = [10**9, 10**9]
    queries = [["SUM", 0, 1, 3], ["SET", 0, 999999999]]
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
            p = random.randint(1, 3)
            queries.append(["SUM", l, r, p])
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-013-range-sum-multiple-powers.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
