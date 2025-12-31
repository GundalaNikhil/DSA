import sys

class Node:
    def __init__(self, val=None):
        if val is not None:
            self.max_len = 1
            self.pref_len = 1
            self.suff_len = 1
            self.length = 1
            self.left_val = val
            self.right_val = val
        else:
            self.max_len = 0
            self.pref_len = 0
            self.suff_len = 0
            self.length = 0
            self.left_val = 0
            self.right_val = 0

def process(arr: list[int], updates: list[tuple[int, int]]) -> list[int]:
    n = len(arr)
    tree = [None] * (4 * n)
    
    def merge(left, right):
        res = Node()
        res.length = left.length + right.length
        res.left_val = left.left_val
        res.right_val = right.right_val
        
        res.max_len = max(left.max_len, right.max_len)
        res.pref_len = left.pref_len
        res.suff_len = right.suff_len
        
        if left.right_val < right.left_val:
            res.max_len = max(res.max_len, left.suff_len + right.pref_len)
            if left.pref_len == left.length:
                res.pref_len = left.length + right.pref_len
            if right.suff_len == right.length:
                res.suff_len = right.length + left.suff_len
                
        return res

    def build(node, start, end):
        if start == end:
            tree[node] = Node(arr[start])
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = Node(val)
        else:
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node + 1, start, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, end, idx, val)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

    build(0, 0, n - 1)
    results = []
    
    for idx, val in updates:
        update(0, 0, n - 1, idx, val)
        results.append(tree[0].max_len)
        
    return results

def main():
    import sys
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    updates = []
    for _ in range(q):
        type = next(it) # SET
        updates.append((int(next(it)), int(next(it))))
    
    results = process(arr, updates)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
