import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

class Solution:
    def process(self, arr: list[int], ops: list[list[str]]) -> list[int]:
        n = len(arr)
        # Tree stores (sum, lazy_val, has_lazy)
        tree_sum = [0] * (4 * n)
        tree_lazy = [0] * (4 * n)
        tree_has_lazy = [False] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree_sum[node] = arr[start]
            else:
                mid = (start + end) // 2
                build(2 * node + 1, start, mid)
                build(2 * node + 2, mid + 1, end)
                tree_sum[node] = tree_sum[2 * node + 1] + tree_sum[2 * node + 2]

        def push(node, start, end):
            if tree_has_lazy[node]:
                mid = (start + end) // 2
                val = tree_lazy[node]
                
                # Left child
                tree_lazy[2 * node + 1] = val
                tree_has_lazy[2 * node + 1] = True
                tree_sum[2 * node + 1] = val * (mid - start + 1)
                
                # Right child
                tree_lazy[2 * node + 2] = val
                tree_has_lazy[2 * node + 2] = True
                tree_sum[2 * node + 2] = val * (end - mid)
                
                tree_has_lazy[node] = False

        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                tree_lazy[node] = val
                tree_has_lazy[node] = True
                tree_sum[node] = val * (end - start + 1)
                return
            
            push(node, start, end)
            mid = (start + end) // 2
            update(2 * node + 1, start, mid, l, r, val)
            update(2 * node + 2, mid + 1, end, l, r, val)
            tree_sum[node] = tree_sum[2 * node + 1] + tree_sum[2 * node + 2]

        def query(node, start, end, l, r):
            if l > end or r < start:
                return 0
            if l <= start and end <= r:
                return tree_sum[node]
            
            push(node, start, end)
            mid = (start + end) // 2
            return query(2 * node + 1, start, mid, l, r) + \
                   query(2 * node + 2, mid + 1, end, l, r)

        build(0, 0, n - 1)
        results = []
        
        for op in ops:
            if op[0] == "SETPREFIX":
                k = int(op[1])
                x = int(op[2])
                if k > 0:
                    update(0, 0, n - 1, 0, k - 1, x)
            else:
                l = int(op[1])
                r = int(op[2])
                results.append(query(0, 0, n - 1, l, r))
                
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
        ops.append([type, next(it), next(it)])
    
    sol = Solution()
    results = sol.process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
