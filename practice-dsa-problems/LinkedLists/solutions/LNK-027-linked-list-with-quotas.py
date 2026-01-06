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
        
    quotas = {}
    for s in range(1, num_segments + 1):
        iq = int(input_data[ptr])
        ptr += 1
        dq = int(input_data[ptr])
        ptr += 1
        quotas[s] = [iq, dq]
        
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
            
            if quotas[s][0] > 0:
                L, R = split(segment_roots[s], pos - 1)
                new_n = Node(x, s)
                segment_roots[s] = merge(merge(L, new_n), R)
                quotas[s][0] -= 1
                
        elif op == 'DEL':
            s = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            
            if quotas[s][1] > 0 and segment_roots[s] and pos <= segment_roots[s].size:
                L, R = split(segment_roots[s], pos)
                L1, L2 = split(L, pos - 1)
                segment_roots[s] = merge(L1, R)
                quotas[s][1] -= 1
                
        elif op == 'COUNT':
            s = int(input_data[ptr])
            ptr += 1
            print(segment_roots[s].size if segment_roots[s] else 0)
if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()