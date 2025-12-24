import random
import yaml

class Node:
    def __init__(self, val=0, size=0):
        if size == 0:
            self.pre = 0
            self.suf = 0
            self.max_len = 0
            self.first = 0
            self.last = 0
            self.size = 0
        else:
            self.pre = 1
            self.suf = 1
            self.max_len = 1
            self.first = val
            self.last = val
            self.size = 1

def merge(L, R):
    if L.size == 0: return R
    if R.size == 0: return L
    res = Node()
    res.size = L.size + R.size
    res.first = L.first
    res.last = R.last
    res.max_len = max(L.max_len, R.max_len)
    res.pre = L.pre
    res.suf = R.suf
    
    if L.last < R.first:
        res.max_len = max(res.max_len, L.suf + R.pre)
        if L.pre == L.size:
            res.pre = L.size + R.pre
        if R.suf == R.size:
            res.suf = R.size + L.suf
            
    return res

class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.tree = [Node() for _ in range(4 * n)]
        self._build(0, 0, n - 1, a)
        
    def _build(self, node, start, end, a):
        if start == end:
            self.tree[node] = Node(a[start], 1)
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid, a)
        self._build(2 * node + 2, mid + 1, end, a)
        self.tree[node] = merge(self.tree[2 * node + 1], self.tree[2 * node + 2])
        
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = Node(val, 1)
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

def solve(n, q, a, queries):
    st = SegmentTree(n, a)
    results = []
    for op in queries:
        idx, val = op[1], op[2]
        st.update(0, 0, n - 1, idx, val)
        results.append(str(st.tree[0].max_len))
    return results

def make_test_case(n, q, a, queries):
    input_str = f"{n} {q}\n"
    input_str += " ".join(map(str, a)) + "\n"
    for op in queries:
        input_str += f"SET {op[1]} {op[2]}\n"
    output_str = "\n".join(solve(n, q, a, queries))
    return input_str, output_str

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, q = 3, 1
    a = [1, 2, 1]
    queries = [["SET", 2, 3]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # 1. Multiple updates
    n, q = 5, 3
    a = [5, 4, 3, 2, 1]
    queries = [["SET", 2, 10], ["SET", 0, 1], ["SET", 4, 11]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    test_cases["hidden"].append({"input": "1 1\n10\nSET 0 5\n", "output": "1", "category": "edge"})
    
    # Stress Case
    n, q = 10000, 10000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = [["SET", random.randint(0, n-1), random.randint(-10**9, 10**9)] for _ in range(q)]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-008-longest-increasing-subarray-updates.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
