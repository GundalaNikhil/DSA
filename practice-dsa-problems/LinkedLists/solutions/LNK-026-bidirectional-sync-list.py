import sys
import random
class Node:
    def __init__(self, val):
        self.val = val
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
def get_val(root, k):
    if not root or k < 1 or k > root.size:
        return -1
    l_size = root.left.size if root.left else 0
    if l_size + 1 == k:
        return root.val
    if k <= l_size:
        return get_val(root.left, k)
    return get_val(root.right, k - l_size - 1)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    d = int(input_data[ptr])
    ptr += 1
    root_a = None
    root_a = None
    for _ in range(n):
        v = int(input_data[ptr])
        ptr += 1
        root_a = merge(root_a, Node(v))
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op_type = input_data[ptr]
        ptr += 1
        target = input_data[ptr]
        ptr += 1
        
        if op_type == "INS":
            pos = int(input_data[ptr])
            ptr += 1
            val = int(input_data[ptr])
            ptr += 1
            val_a = val if target == "A" else val - d
            L, R = split(root_a, pos - 1)
            root_a = merge(merge(L, Node(val_a)), R)
        elif op_type == "DEL":
            pos = int(input_data[ptr])
            ptr += 1
            if root_a and 1 <= pos <= root_a.size:
                L, R = split(root_a, pos)
                L1, L2 = split(L, pos - 1)
                root_a = merge(L1, R)
        elif op_type == "GET":
            pos = int(input_data[ptr])
            ptr += 1
            val_a = get_val(root_a, pos)
            if val_a == -1:
                print(-1)
            else:
                print(val_a if target == "A" else val_a + d)
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    solve()