import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def process(arr: list[int], forbidden: list[bool], ops: list[list[str]]) -> list[int]:
    n = len(arr)
    vals = list(arr)
    active = [not f for f in forbidden]
    tree = [0] * (4 * n)
    
    def build(node, start, end):
        if start == end:
            tree[node] = vals[start] if active[start] else 0
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2])

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node + 1, start, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, end, idx, val)
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2])

    def query(node, start, end, l, r):
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return tree[node]
        
        mid = (start + end) // 2
        p1 = query(2 * node + 1, start, mid, l, r)
        p2 = query(2 * node + 2, mid + 1, end, l, r)
        return gcd(p1, p2)

    build(0, 0, n - 1)
    results = []
    
    for op in ops:
        type = op[0]
        if type == "TOGGLE":
            idx = int(op[1])
            active[idx] = not active[idx]
            eff_val = vals[idx] if active[idx] else 0
            update(0, 0, n - 1, idx, eff_val)
        elif type == "SET":
            idx = int(op[1])
            val = int(op[2])
            vals[idx] = val
            eff_val = vals[idx] if active[idx] else 0
            update(0, 0, n - 1, idx, eff_val)
        else:
            l = int(op[1])
            r = int(op[2])
            results.append(query(0, 0, n - 1, l, r))
            
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
    f_count = int(next(it))
    forbidden = [False] * n
    for _ in range(f_count):
        forbidden[int(next(it))] = True
        
    ops = []
    for _ in range(q):
        type = next(it)
        if type == "TOGGLE":
            ops.append([type, next(it)])
        elif type == "SET":
            ops.append([type, next(it), next(it)])
        else:
            ops.append([type, next(it), next(it)])
            
    results = process(arr, forbidden, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
