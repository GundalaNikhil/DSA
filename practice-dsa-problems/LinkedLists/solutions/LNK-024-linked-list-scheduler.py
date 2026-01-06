import sys
from bisect import bisect_left, bisect_right
class Node:
    def __init__(self, count, left=None, right=None):
        self.count = count
        self.left = left
        self.right = right

class PersistentSegmentTree:
    def __init__(self, n):
        self.n = n
        self.roots = [self._build(1, n)]
        
    def _build(self, l, r):
        node = Node(0)
        if l < r:
            mid = (l + r) // 2
            node.left = self._build(l, mid)
            node.right = self._build(mid + 1, r)
        return node
        
    def update(self, pos):
        self.roots.append(self._update(self.roots[-1], 1, self.n, pos))
        
    def _update(self, prev, l, r, pos):
        node = Node(prev.count + 1, prev.left, prev.right)
        if l < r:
            mid = (l + r) // 2
            if pos <= mid:
                node.left = self._update(prev.left, l, mid, pos)
            else:
                node.right = self._update(prev.right, mid + 1, r, pos)
        return node
        
    def query(self, root, ql, qr, l, r):
        if ql <= l and r <= qr:
            return root.count
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res += self.query(root.left, ql, qr, l, mid)
        if qr > mid:
            res += self.query(root.right, ql, qr, mid + 1, r)
        return res

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    
    starts = []
    ends = []
    for i in range(1, n + 1):
        s = int(input_data[ptr])
        ptr += 1
        d = int(input_data[ptr])
        ptr += 1
        starts.append((s, i))
        ends.append((s + d, i))
        
    starts.sort()
    ends.sort()
    
    pst_start = PersistentSegmentTree(n)
    for s_time, pos in starts:
        pst_start.update(pos)
        
    pst_end = PersistentSegmentTree(n)
    for e_time, pos in ends:
        pst_end.update(pos)
        
    s_times = [x[0] for x in starts]
    e_times = [x[0] for x in ends]
    
    q = int(input_data[ptr])
    ptr += 1
    
    results = []
    for _ in range(q):
        l = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        t = int(input_data[ptr])
        ptr += 1
        
        idx_s = bisect_right(s_times, t)
        count_s = pst_start.query(pst_start.roots[idx_s], l, r, 1, n)
        
        # End events: if end_time <= t, it expired?
        # Logic: active at time t.
        # Active if start <= t AND end > t? Or end >= t?
        # Original logic: count_s - count_e.
        # count_s: starts <= t.
        # count_e: ends <= t.
        # Active = starts <= t - ends <= t.
        
        idx_e = bisect_right(e_times, t)
        count_e = pst_end.query(pst_end.roots[idx_e], l, r, 1, n)
        
        results.append(str(count_s - count_e))
        
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == '__main__':
    solve()