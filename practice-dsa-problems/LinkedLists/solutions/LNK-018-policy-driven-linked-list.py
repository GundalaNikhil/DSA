import sys
import random
class Node:
    def __init__(self, val, segment_id):
        self.val = val
        self.segment_id = segment_id
        self.priority = random.random()
        self.left = None
        self.right = None
        self.size = 1
    def update(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
            if self.right:
                self.size += self.right.size
def split(root, k):
    if not root:
        return None, None
    l_size = (root.left.size if root.left else 0) + 1
    if l_size <= k:
        root.right, r = split(root.right, k - l_size)
        root.update()
        return root, r
    else:
        l, root.left = split(root.left, k)
        root.update()
        return l, root

def merge(l, r):
    if not l or not r:
        return l or r
    if l.priority > r.priority:
        l.right = merge(l.right, r)
        l.update()
        return l
    else:
        r.left = merge(l, r.left)
        r.update()
        return r
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    num_segments = int(input_data[ptr])
    ptr += 1
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    segs = []
    for _ in range(n):
        segs.append(int(input_data[ptr]))
        ptr += 1
        
    limits = {}
    for s in range(1, num_segments + 1):
        mi = int(input_data[ptr])
        ptr += 1
        md = int(input_data[ptr])
        ptr += 1
        limits[s] = [mi, md]
        
    stats = {s: [0, 0] for s in range(1, num_segments + 1)}
    sizes = {s: 0 for s in range(1, num_segments + 1)}
    for s in segs:
        sizes[s] += 1
        
    segment_roots = {s: None for s in range(1, num_segments + 1)}
    for i in range(n):
        s = segs[i]
        node = Node(vals[i], s)
        segment_roots[s] = merge(segment_roots[s], node)
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'INS':
            s = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            
            if stats[s][0] < limits[s][0]:
                L, R = split(segment_roots[s], pos - 1)
                new_node = Node(x, s)
                segment_roots[s] = merge(merge(L, new_node), R)
                stats[s][0] += 1
                sizes[s] += 1
                
        elif op == 'DEL':
            s = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            
            if stats[s][1] < limits[s][1] and sizes[s] >= pos:
                L, R = split(segment_roots[s], pos)
                L1, L2 = split(L, pos - 1)
                segment_roots[s] = merge(L1, R)
                stats[s][1] += 1
                sizes[s] -= 1
                
        elif op == 'COUNT':
            s = int(input_data[ptr])
            ptr += 1
            print(sizes[s])
if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()