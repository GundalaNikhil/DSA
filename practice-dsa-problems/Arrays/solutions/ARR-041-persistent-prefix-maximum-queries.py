import sys

class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

class PersistentSegmentTree:
    def __init__(self, n):
        self.n = n
        self.roots = []

    def build(self, arr, l, r):
        if l == r:
            return Node(arr[l - 1])
        mid = (l + r) // 2
        lc = self.build(arr, l, mid)
        rc = self.build(arr, mid + 1, r)
        return Node(max(lc.val, rc.val), lc, rc)

    def update(self, old_node, l, r, i, x):
        if l == r:
            return Node(x)
        mid = (l + r) // 2
        if i <= mid:
            lc = self.update(old_node.l, l, mid, i, x)
            rc = old_node.r
        else:
            lc = old_node.l
            rc = self.update(old_node.r, mid + 1, r, i, x)
        return Node(max(lc.val, rc.val), lc, rc)

    def query(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return node.val
        mid = (l + r) // 2
        res = -float('inf')
        if ql <= mid:
            res = max(res, self.query(node.l, l, mid, ql, qr))
        if qr > mid:
            res = max(res, self.query(node.r, mid + 1, r, ql, qr))
        return res

def solve():
    sys.setrecursionlimit(300000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
            
        pst = PersistentSegmentTree(n)
        init_root = pst.build(a, 1, n)
        version_map = {0: init_root}
        next_ver = 1
        
        for _ in range(q):
            op = next(iterator)
            if op == 'U':
                v = int(next(iterator))
                i = int(next(iterator))
                x = int(next(iterator))
                # Update version v, create new version
                new_root = pst.update(version_map[v], 1, n, i, x)
                version_map[next_ver] = new_root
                next_ver += 1
            else:
                # Query version v range [1, r]
                v = int(next(iterator))
                r = int(next(iterator))
                # Max in [1, r]? Standard prefix max.
                print(pst.query(version_map[v], 1, n, 1, r))
                
    except StopIteration:
        return

if __name__ == '__main__':
    solve()