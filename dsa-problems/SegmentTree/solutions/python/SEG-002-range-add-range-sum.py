def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    n = len(arr)
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def push(node, start, end):
        if lazy[node] != 0:
            mid = (start + end) // 2
            
            # Left child
            tree[2 * node + 1] += lazy[node] * (mid - start + 1)
            lazy[2 * node + 1] += lazy[node]
            
            # Right child
            tree[2 * node + 2] += lazy[node] * (end - mid)
            lazy[2 * node + 2] += lazy[node]
            
            lazy[node] = 0

    def update(node, start, end, l, r, val):
        if l > end or r < start:
            return
        
        if l <= start and end <= r:
            tree[node] += val * (end - start + 1)
            lazy[node] += val
            return

        push(node, start, end)
        mid = (start + end) // 2
        update(2 * node + 1, start, mid, l, r, val)
        update(2 * node + 2, mid + 1, end, l, r, val)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def query(node, start, end, l, r):
        if l > end or r < start:
            return 0
        
        if l <= start and end <= r:
            return tree[node]
        
        push(node, start, end)
        mid = (start + end) // 2
        return query(2 * node + 1, start, mid, l, r) + \
               query(2 * node + 2, mid + 1, end, l, r)

    build(0, 0, n - 1)
    results = []
    
    for op in ops:
        if op[0] == "ADD":
            l, r, x = int(op[1]), int(op[2]), int(op[3])
            update(0, 0, n - 1, l, r, x)
        else:
            l, r = int(op[1]), int(op[2])
            results.append(query(0, 0, n - 1, l, r))
            
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
    ops = []
    for _ in range(q):
        type = next(it)
        if type == "ADD":
            ops.append([type, next(it), next(it), next(it)])
        else:
            ops.append([type, next(it), next(it)])
    
    results = process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
