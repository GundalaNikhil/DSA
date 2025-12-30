import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

class Solution:
    def process(self, arr: list[int], ops: list[list[str]]) -> list[int]:
        n = len(arr)
        MOD = 1000000007
        
        # Tree stores tuples (sum1, sum2, sum3)
        tree = [(0, 0, 0)] * (4 * n)
        
        def make_node(val):
            v = val % MOD
            v2 = (v * v) % MOD
            v3 = (v2 * v) % MOD
            return (v, v2, v3)

        def merge(n1, n2):
            return (
                (n1[0] + n2[0]) % MOD,
                (n1[1] + n2[1]) % MOD,
                (n1[2] + n2[2]) % MOD
            )

        def build(node, start, end):
            if start == end:
                tree[node] = make_node(arr[start])
            else:
                mid = (start + end) // 2
                build(2 * node + 1, start, mid)
                build(2 * node + 2, mid + 1, end)
                tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = make_node(val)
            else:
                mid = (start + end) // 2
                if idx <= mid:
                    update(2 * node + 1, start, mid, idx, val)
                else:
                    update(2 * node + 2, mid + 1, end, idx, val)
                tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def query(node, start, end, l, r):
            if l > end or r < start:
                return (0, 0, 0)
            if l <= start and end <= r:
                return tree[node]
            
            mid = (start + end) // 2
            p1 = query(2 * node + 1, start, mid, l, r)
            p2 = query(2 * node + 2, mid + 1, end, l, r)
            return merge(p1, p2)

        build(0, 0, n - 1)
        results = []
        
        for op in ops:
            if op[0] == "SET":
                idx = int(op[1])
                val = int(op[2])
                update(0, 0, n - 1, idx, val)
            else:
                l = int(op[1])
                r = int(op[2])
                p = int(op[3])
                res = query(0, 0, n - 1, l, r)
                results.append(res[p-1])
                
        return results

def main():
    import sys
    sys.setrecursionlimit(300000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    ops = []
    for _ in range(q):
        type = next(it)
        if type == "SET":
            ops.append([type, next(it), next(it)])
        else:
            ops.append([type, next(it), next(it), next(it)])
    
    sol = Solution()
    results = sol.process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
