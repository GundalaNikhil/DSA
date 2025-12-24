import random
import yaml

class LinearBasis:
    def __init__(self):
        self.basis = [0] * 31
        
    def insert(self, x):
        for i in range(30, -1, -1):
            if not (x >> i): continue
            if not self.basis[i]:
                self.basis[i] = x
                return True
            x ^= self.basis[i]
        return False
        
    def query_max(self):
        res = 0
        for i in range(30, -1, -1):
            if (res ^ self.basis[i]) > res:
                res ^= self.basis[i]
        return res

def merge_basis(b1, b2):
    res = LinearBasis()
    res.basis = list(b1.basis)
    for x in b2.basis:
        if x: res.insert(x)
    return res

class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.tree = [LinearBasis() for _ in range(4 * n)]
        self._build(0, 0, n - 1, a)
        
    def _build(self, node, start, end, a):
        if start == end:
            self.tree[node].insert(a[start])
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid, a)
        self._build(2 * node + 2, mid + 1, end, a)
        self.tree[node] = merge_basis(self.tree[2 * node + 1], self.tree[2 * node + 2])
        
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = LinearBasis()
            self.tree[node].insert(val)
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = merge_basis(self.tree[2 * node + 1], self.tree[2 * node + 2])
        
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return LinearBasis()
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        b1 = self.query(2 * node + 1, start, mid, l, r)
        b2 = self.query(2 * node + 2, mid + 1, end, l, r)
        return merge_basis(b1, b2)

def solve(n, q, a, queries):
    st = SegmentTree(n, a)
    results = []
    for op in queries:
        if op[0] == "SET":
            idx, val = int(op[1]), int(op[2])
            st.update(0, 0, n - 1, idx, val)
        elif op[0] == "MAXXOR":
            l, r = int(op[1]), int(op[2])
            basis = st.query(0, 0, n - 1, l, r)
            results.append(str(basis.query_max()))
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
    a = [1, 2, 3]
    queries = [["MAXXOR", 0, 2]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    n, q = 5, 3
    a = [1, 2, 4, 8, 16]
    queries = [["MAXXOR", 0, 4], ["SET", 2, 0], ["MAXXOR", 0, 4]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    test_cases["hidden"].append({"input": "1 1\n0\nMAXXOR 0 0\n", "output": "0", "category": "edge"})
    
    # Stress Case
    # Max bits 30
    n, q = 2000, 2000 # Keep small for Python reference solution
    a = [random.randint(0, 2**30 - 1) for _ in range(n)]
    queries = []
    for _ in range(q):
        if random.random() < 0.3:
            queries.append(["SET", random.randint(0, n-1), random.randint(0, 2**30 - 1)])
        else:
            l = random.randint(0, n-1)
            r = random.randint(l, n-1)
            queries.append(["MAXXOR", l, r])
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-007-range-xor-basis.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
