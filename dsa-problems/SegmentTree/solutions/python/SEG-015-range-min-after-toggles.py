import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

class Solution:
    def process(self, arr: list[int], ops: list[list[str]]) -> list[int]:
        n = len(arr)
        # Tree stores (min, max, lazy_add, lazy_flip)
        # Using separate arrays for performance
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        tree_add = [0] * (4 * n)
        tree_flip = [False] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree_min[node] = arr[start]
                tree_max[node] = arr[start]
            else:
                mid = (start + end) // 2
                build(2 * node + 1, start, mid)
                build(2 * node + 2, mid + 1, end)
                tree_min[node] = min(tree_min[2 * node + 1], tree_min[2 * node + 2])
                tree_max[node] = max(tree_max[2 * node + 1], tree_max[2 * node + 2])

        def apply_flip(node):
            tree_min[node], tree_max[node] = -tree_max[node], -tree_min[node]
            tree_add[node] = -tree_add[node]
            tree_flip[node] = not tree_flip[node]

        def apply_add(node, val):
            tree_min[node] += val
            tree_max[node] += val
            tree_add[node] += val

        def push(node, start, end):
            if tree_flip[node]:
                apply_flip(2 * node + 1)
                apply_flip(2 * node + 2)
                tree_flip[node] = False
            if tree_add[node] != 0:
                apply_add(2 * node + 1, tree_add[node])
                apply_add(2 * node + 2, tree_add[node])
                tree_add[node] = 0

        def update_add(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                apply_add(node, val)
                return
            
            push(node, start, end)
            mid = (start + end) // 2
            update_add(2 * node + 1, start, mid, l, r, val)
            update_add(2 * node + 2, mid + 1, end, l, r, val)
            tree_min[node] = min(tree_min[2 * node + 1], tree_min[2 * node + 2])
            tree_max[node] = max(tree_max[2 * node + 1], tree_max[2 * node + 2])

        def update_flip(node, start, end, l, r):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                apply_flip(node)
                return
            
            push(node, start, end)
            mid = (start + end) // 2
            update_flip(2 * node + 1, start, mid, l, r)
            update_flip(2 * node + 2, mid + 1, end, l, r)
            tree_min[node] = min(tree_min[2 * node + 1], tree_min[2 * node + 2])
            tree_max[node] = max(tree_max[2 * node + 1], tree_max[2 * node + 2])

        def query(node, start, end, l, r):
            if l > end or r < start:
                return float('inf')
            if l <= start and end <= r:
                return tree_min[node]
            
            push(node, start, end)
            mid = (start + end) // 2
            return min(query(2 * node + 1, start, mid, l, r),
                       query(2 * node + 2, mid + 1, end, l, r))

        build(0, 0, n - 1)
        results = []
        
        for op in ops:
            if op[0] == "ADD":
                update_add(0, 0, n - 1, int(op[1]), int(op[2]), int(op[3]))
            elif op[0] == "FLIP":
                update_flip(0, 0, n - 1, int(op[1]), int(op[2]))
            else:
                results.append(query(0, 0, n - 1, int(op[1]), int(op[2])))
                
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
        if type == "ADD":
            ops.append([type, next(it), next(it), next(it)])
        elif type == "FLIP":
            ops.append([type, next(it), next(it)])
        else:
            ops.append([type, next(it), next(it)])
    
    sol = Solution()
    results = sol.process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
