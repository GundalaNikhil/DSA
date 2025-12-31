import sys

class Basis:
    def __init__(self):
        self.b = [0] * 30
        
    def insert(self, x):
        for i in range(29, -1, -1):
            if (x >> i) & 1:
                if self.b[i] == 0:
                    self.b[i] = x
                    return
                x ^= self.b[i]
                
    def merge(self, other):
        for x in other.b:
            if x != 0:
                self.insert(x)
                
    def max_xor(self):
        res = 0
        for x in reversed(self.b):
            if (res ^ x) > res:
                res ^= x
        return res

def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    n = len(arr)
    tree = [Basis() for _ in range(4 * n)]
    
    def build(node, start, end):
        if start == end:
            tree[node] = Basis()
            tree[node].insert(arr[start])
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            
            # Merge logic: create new basis, merge children
            new_b = Basis()
            new_b.merge(tree[2 * node + 1])
            new_b.merge(tree[2 * node + 2])
            tree[node] = new_b

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = Basis()
            tree[node].insert(val)
        else:
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node + 1, start, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, end, idx, val)
                
            new_b = Basis()
            new_b.merge(tree[2 * node + 1])
            new_b.merge(tree[2 * node + 2])
            tree[node] = new_b

    def query(node, start, end, l, r):
        if l > end or r < start:
            return Basis()
        if l <= start and end <= r:
            return tree[node]
            
        mid = (start + end) // 2
        p1 = query(2 * node + 1, start, mid, l, r)
        p2 = query(2 * node + 2, mid + 1, end, l, r)
        
        res = Basis()
        res.merge(p1)
        res.merge(p2)
        return res

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
            res = query(0, 0, n - 1, l, r)
            results.append(res.max_xor())
            
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
        ops.append([type, next(it), next(it)])
    
    results = process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
