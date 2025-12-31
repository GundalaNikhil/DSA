import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Node:
    def __init__(self, count=0, left=None, right=None):
        self.count = count
        self.left = left
        self.right = right

def kth_prefix(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    # Coordinate Compression
    unique = sorted(list(set(arr)))
    val_map = {val: i for i, val in enumerate(unique)}
    m = len(unique)
    
    # Build Null Tree
    def build(l, r):
        node = Node()
        if l == r:
            return node
        mid = (l + r) // 2
        node.left = build(l, mid)
        node.right = build(mid + 1, r)
        return node

    null_root = build(0, m - 1)
    roots = []
    
    def update(prev_node, l, r, idx):
        node = Node(prev_node.count + 1, prev_node.left, prev_node.right)
        if l == r:
            return node
        mid = (l + r) // 2
        if idx <= mid:
            node.left = update(prev_node.left, l, mid, idx)
        else:
            node.right = update(prev_node.right, mid + 1, r, idx)
        return node

    prev = null_root
    for x in arr:
        idx = val_map[x]
        new_root = update(prev, 0, m - 1, idx)
        roots.append(new_root)
        prev = new_root
        
    def query(node, l, r, k):
        if l == r:
            return l
        mid = (l + r) // 2
        left_count = node.left.count
        if k <= left_count:
            return query(node.left, l, mid, k)
        else:
            return query(node.right, mid + 1, r, k - left_count)
            
    results = []
    for r, k in queries:
        idx = query(roots[r], 0, m - 1, k)
        results.append(unique[idx])
        
    return results

def main():
    import sys
    # Increase recursion depth for deep trees
    sys.setrecursionlimit(300000)
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    queries = []
    for _ in range(q):
        type = next(it) # PREFIX
        queries.append((int(next(it)), int(next(it))))
    
    results = kth_prefix(arr, queries)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
