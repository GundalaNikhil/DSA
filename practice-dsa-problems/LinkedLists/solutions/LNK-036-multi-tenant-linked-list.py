import sys
import random
class Node:
    def __init__(self, val, tenant_id):
        self.val = val
        self.tenant_id = tenant_id
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
def get_tenant_id(root, k):
    if not root or k < 1 or k > root.size:
        return -1
    l_size = (root.left.size if root.left else 0) + 1
    if l_size == k:
        return root.tenant_id
    if k < l_size:
        return get_tenant_id(root.left, k)
    return get_tenant_id(root.right, k - l_size)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    T = int(input_data[ptr])
    ptr += 1
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    tids = []
    for _ in range(n):
        tids.append(int(input_data[ptr]))
        ptr += 1
        
    limits = {}
    for t in range(1, T + 1):
        limits[t] = int(input_data[ptr])
        ptr += 1
        
    counts = {}
    root = None
    for i in range(n):
        tid = tids[i]
        counts[tid] = counts.get(tid, 0) + 1
        root = merge(root, Node(vals[i], tid))
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == "INS":
            tid = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            if counts.get(tid, 0) < limits[tid]:
                L, R = split(root, pos - 1)
                root = merge(merge(L, Node(x, tid)), R)
                counts[tid] = counts.get(tid, 0) + 1
                
        elif op == "DEL":
            tid = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            if root and 1 <= pos <= root.size:
                target_tid = get_tenant_id(root, pos)
                if target_tid == tid:
                    L, R = split(root, pos)
                    L1, L2 = split(L, pos - 1)
                    root = merge(L1, R)
                    counts[tid] -= 1
                    
        elif op == "COUNT":
            tid = int(input_data[ptr])
            ptr += 1
            print(counts.get(tid, 0))
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    solve()