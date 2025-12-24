import random
import yaml

class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.min_val = [0] * (4 * n)
        self.max_val = [0] * (4 * n)
        self.lazy_a = [1] * (4 * n) # multiplier
        self.lazy_b = [0] * (4 * n) # adder
        self._build(0, 0, n - 1, a)
        
    def _build(self, node, start, end, a):
        if start == end:
            self.min_val[node] = a[start]
            self.max_val[node] = a[start]
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid, a)
        self._build(2 * node + 2, mid + 1, end, a)
        self.min_val[node] = min(self.min_val[2 * node + 1], self.min_val[2 * node + 2])
        self.max_val[node] = max(self.max_val[2 * node + 1], self.max_val[2 * node + 2])
        
    def _apply(self, node, a, b):
        # New val = a * old_val + b
        if a == 1:
            self.min_val[node] += b
            self.max_val[node] += b
        else:
            # a == -1
            n_min = -self.max_val[node] + b
            n_max = -self.min_val[node] + b
            self.min_val[node] = n_min
            self.max_val[node] = n_max
        
        # update lazy tags: (a_new, b_new) composed with (a_old, b_old)
        # g(f(v)) = a_g(a_f*v + b_f) + b_g = (a_g*a_f)v + (a_g*b_f + b_g)
        self.lazy_b[node] = a * self.lazy_b[node] + b
        self.lazy_a[node] = a * self.lazy_a[node]
        
    def _push(self, node, start, end):
        if self.lazy_a[node] != 1 or self.lazy_b[node] != 0:
            self._apply(2 * node + 1, self.lazy_a[node], self.lazy_b[node])
            self._apply(2 * node + 2, self.lazy_a[node], self.lazy_b[node])
            self.lazy_a[node] = 1
            self.lazy_b[node] = 0
            
    def update_affine(self, node, start, end, l, r, a, b):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self._apply(node, a, b)
            return
        self._push(node, start, end)
        mid = (start + end) // 2
        self.update_affine(2 * node + 1, start, mid, l, r, a, b)
        self.update_affine(2 * node + 2, mid + 1, end, l, r, a, b)
        self.min_val[node] = min(self.min_val[2 * node + 1], self.min_val[2 * node + 2])
        self.max_val[node] = max(self.max_val[2 * node + 1], self.max_val[2 * node + 2])
        
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return self.min_val[node]
        self._push(node, start, end)
        mid = (start + end) // 2
        return min(self.query(2 * node + 1, start, mid, l, r),
                   self.query(2 * node + 2, mid + 1, end, l, r))

def solve(n, q, a, queries):
    st = SegmentTree(n, a)
    results = []
    for op in queries:
        if op[0] == "ADD":
            l, r, x = int(op[1]), int(op[2]), int(op[3])
            st.update_affine(0, 0, n - 1, l, r, 1, x)
        elif op[0] == "FLIP":
            l, r = int(op[1]), int(op[2])
            st.update_affine(0, 0, n - 1, l, r, -1, 0)
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
    n, q = 3, 3
    a = [1, -2, 3]
    queries = [["FLIP", 0, 2], ["ADD", 1, 2, 1], ["MIN", 0, 2]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # Nested flips and additions
    n, q = 5, 5
    a = [10, -5, 8, 2, -10]
    queries = [
        ["ADD", 0, 4, 5],   # [15, 0, 13, 7, -5]
        ["FLIP", 1, 3],    # [15, 0, -13, -7, -5]
        ["MIN", 0, 4],     # -13
        ["FLIP", 0, 4],    # [-15, 0, 13, 7, 5]
        ["MIN", 1, 2]      # 0
    ]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    test_cases["hidden"].append({"input": "1 1\n5\nMIN 0 0\n", "output": "5", "category": "edge"})
    test_cases["hidden"].append({"input": "1 2\n-5\nFLIP 0 0\nMIN 0 0\n", "output": "5", "category": "edge"})
    
    # Large numbers
    n, q = 2, 2
    a = [10**9, -10**9]
    queries = [["ADD", 0, 1, 10**9], ["MIN", 0, 1]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "boundary"})

    # Stress Case
    n, q = 10000, 10000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = []
    for _ in range(q):
        r = random.random()
        if r < 0.2:
            l = random.randint(0, n-1)
            r2 = random.randint(l, n-1)
            queries.append(["ADD", l, r2, random.randint(-10**9, 10**9)])
        elif r < 0.4:
            l = random.randint(0, n-1)
            r2 = random.randint(l, n-1)
            queries.append(["FLIP", l, r2])
        else:
            l = random.randint(0, n-1)
            r2 = random.randint(l, n-1)
            queries.append(["MIN", l, r2])
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-015-range-min-after-toggles.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
