import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

class Solution:
    def process(self, arr: list[int], ops: list[list[str]]) -> list[int]:
        n = len(arr)
        # Tree stores tuples (val, index)
        tree = [(0, 0)] * (4 * n)
        
        def merge(p1, p2):
            if p1[0] < p2[0]:
                return p1
            elif p2[0] < p1[0]:
                return p2
            else:
                return p1 if p1[1] < p2[1] else p2

        def build(node, start, end):
            if start == end:
                tree[node] = (arr[start], start)
            else:
                mid = (start + end) // 2
                build(2 * node + 1, start, mid)
                build(2 * node + 2, mid + 1, end)
                tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = (val, idx)
            else:
                mid = (start + end) // 2
                if idx <= mid:
                    update(2 * node + 1, start, mid, idx, val)
                else:
                    update(2 * node + 2, mid + 1, end, idx, val)
                tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def query(node, start, end, l, r):
            if l > end or r < start:
                return (float('inf'), -1)
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
                l, r = int(op[1]), int(op[2])
                res = query(0, 0, n - 1, l, r)
                results.append(res[1])
        return results

def main():
    import sys
    sys.setrecursionlimit(300000)
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
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
