import random
import yaml
import math

def gcd(a, b):
    return math.gcd(abs(a), abs(b))

class SegmentTree:
    def __init__(self, n, a, forbidden):
        self.n = n
        self.tree = [0] * (4 * n)
        self._build(0, 0, n - 1, a, forbidden)
        
    def _build(self, node, start, end, a, forbidden):
        if start == end:
            self.tree[node] = 0 if forbidden[start] else abs(a[start])
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid, a, forbidden)
        self._build(2 * node + 2, mid + 1, end, a, forbidden)
        self.tree[node] = math.gcd(self.tree[2 * node + 1], self.tree[2 * node + 2])
        
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = math.gcd(self.tree[2 * node + 1], self.tree[2 * node + 2])
        
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        g1 = self.query(2 * node + 1, start, mid, l, r)
        g2 = self.query(2 * node + 2, mid + 1, end, l, r)
        return math.gcd(g1, g2)

def solve(n, q, a, forbidden_set, queries):
    forbidden = [False] * n
    for i in forbidden_set: forbidden[i] = True
    
    st = SegmentTree(n, a, forbidden)
    results = []
    
    curr_a = list(a)
    for op in queries:
        if op[0] == "TOGGLE":
            idx = int(op[1])
            forbidden[idx] = not forbidden[idx]
            val = 0 if forbidden[idx] else abs(curr_a[idx])
            st.update(0, 0, n - 1, idx, val)
        elif op[0] == "SET":
            idx = int(op[1])
            x = int(op[2])
            curr_a[idx] = x
            if not forbidden[idx]:
                st.update(0, 0, n - 1, idx, abs(x))
        elif op[0] == "GCD":
            l, r = int(op[1]), int(op[2])
            results.append(str(st.query(0, 0, n - 1, l, r)))
            
    return results

def make_test_case(n, q, a, f_set, queries):
    input_str = f"{n} {q}\n"
    input_str += " ".join(map(str, a)) + "\n"
    input_str += f"{len(f_set)}\n"
    if f_set:
        input_str += "\n".join(map(str, f_set)) + "\n"
    for op in queries:
        input_str += " ".join(map(str, op)) + "\n"
    output_str = "\n".join(solve(n, q, list(a), set(f_set), queries))
    return input_str, output_str

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, q = 3, 3
    a = [6, 9, 3]
    f_set = [1]
    queries = [["GCD", 0, 2], ["TOGGLE", 1], ["GCD", 0, 2]]
    input_str, output_str = make_test_case(n, q, a, f_set, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # 1. Negative numbers and updates
    n, q = 5, 4
    a = [12, -18, 24, -30, 36]
    f_set = [0, 4]
    queries = [
        ["GCD", 0, 4], # gcd(-18, 24, -30) = 6
        ["SET", 1, 6],  # a[1]=6, f[1]=False -> gcd(6, 24, -30) = 6
        ["TOGGLE", 4], # f[4]=False -> gcd(6, 24, -30, 36) = 6
        ["GCD", 0, 4]
    ]
    input_str, output_str = make_test_case(n, q, a, f_set, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    # 1. All forbidden
    n, q = 3, 1
    a = [10, 20, 30]
    f_set = [0, 1, 2]
    queries = [["GCD", 0, 2]]
    input_str, output_str = make_test_case(n, q, a, f_set, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "edge"})
    
    # 2. Large numbers, zero GCD
    n, q = 5, 1
    a = [0, 0, 0, 0, 0]
    f_set = []
    queries = [["GCD", 0, 4]]
    input_str, output_str = make_test_case(n, q, a, f_set, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "edge"})

    # Stress case
    n, q = 10000, 10000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    f_count = random.randint(0, n)
    f_set = random.sample(range(n), f_count)
    queries = []
    for _ in range(q):
        r = random.random()
        if r < 0.2:
            queries.append(["TOGGLE", random.randint(0, n-1)])
        elif r < 0.4:
            queries.append(["SET", random.randint(0, n-1), random.randint(-10**9, 10**9)])
        else:
            l = random.randint(0, n-1)
            r = random.randint(l, n-1)
            queries.append(["GCD", l, r])
    input_str, output_str = make_test_case(n, q, a, f_set, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-010-range-gcd-skip-zones.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
