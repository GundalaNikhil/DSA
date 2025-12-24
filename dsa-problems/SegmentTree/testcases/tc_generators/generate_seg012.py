import random
import yaml
import bisect

class SqrtDecomp:
    def __init__(self, n, a):
        self.n = n
        self.a = list(a)
        self.block_size = int(n**0.5) + 1
        self.blocks = []
        self.lazy = []
        for i in range(0, n, self.block_size):
            chunk = self.a[i : i + self.block_size]
            self.blocks.append(sorted(chunk))
            self.lazy.append(0)
            
    def update(self, l, r, x):
        b_l = l // self.block_size
        b_r = r // self.block_size
        
        if b_l == b_r:
            for i in range(l, r + 1):
                self.a[i] += x
            self.blocks[b_l] = sorted(self.a[b_l * self.block_size : min((b_l + 1) * self.block_size, self.n)])
        else:
            # Partial left
            for i in range(l, (b_l + 1) * self.block_size):
                self.a[i] += x
            self.blocks[b_l] = sorted(self.a[b_l * self.block_size : (b_l + 1) * self.block_size])
            # Full blocks
            for i in range(b_l + 1, b_r):
                self.lazy[i] += x
            # Partial right
            for i in range(b_r * self.block_size, r + 1):
                self.a[i] += x
            self.blocks[b_r] = sorted(self.a[b_r * self.block_size : min((b_r + 1) * self.block_size, self.n)])
            
    def query(self, l, r, k):
        # Binary search for the k-th element
        low = -2 * 10**15 # Sufficient range
        high = 2 * 10**15
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if self._count_le(l, r, mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        
    def _count_le(self, l, r, x):
        b_l = l // self.block_size
        b_r = r // self.block_size
        count = 0
        
        if b_l == b_r:
            for i in range(l, r + 1):
                if self.a[i] + self.lazy[b_l] <= x:
                    count += 1
        else:
            # Partial left
            for i in range(l, (b_l + 1) * self.block_size):
                if self.a[i] + self.lazy[b_l] <= x:
                    count += 1
            # Full blocks
            for i in range(b_l + 1, b_r):
                count += bisect.bisect_right(self.blocks[i], x - self.lazy[i])
            # Partial right
            for i in range(b_r * self.block_size, r + 1):
                if self.a[i] + self.lazy[b_r] <= x:
                    count += 1
        return count

def solve(n, q, a, queries):
    sd = SqrtDecomp(n, a)
    results = []
    for op in queries:
        if op[0] == "ADD":
            l, r, x = int(op[1]), int(op[2]), int(op[3])
            sd.update(l, r, x)
        else:
            l, r, k = int(op[1]), int(op[2]), int(op[3])
            results.append(str(sd.query(l, r, k)))
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
    queries = [["ADD", 0, 2, 1], ["KTH", 0, 2, 2]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # 1. Negative updates, multiple queries
    n, q = 5, 4
    a = [10, 20, 30, 40, 50]
    queries = [
        ["ADD", 1, 3, -10], # [10, 10, 20, 30, 50]
        ["KTH", 0, 4, 1],   # 10
        ["KTH", 0, 4, 3],   # 20
        ["KTH", 1, 3, 2]    # 2nd of [10, 20, 30] is 20
    ]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    test_cases["hidden"].append({"input": "1 1\n100\nKTH 0 0 1\n", "output": "100", "category": "edge"})
    
    # Stress Case
    # Reduced size for Python reference
    n, q = 3000, 3000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = []
    for _ in range(q):
        if random.random() < 0.4:
            l = random.randint(0, n-1)
            r = random.randint(l, n-1)
            queries.append(["ADD", l, r, random.randint(-10**9, 10**9)])
        else:
            l = random.randint(0, n-1)
            r = random.randint(l, n-1)
            k = random.randint(1, r - l + 1)
            queries.append(["KTH", l, r, k])
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-012-range-add-kth-order.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
