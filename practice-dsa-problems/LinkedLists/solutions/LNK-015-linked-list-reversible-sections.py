import sys
import random
class TreapNode:
    def __init__(self, val, reversible):
        self.val = val
        self.reversible = reversible
        self.priority = random.random()
        self.left = None
        self.right = None
        self.size = 1
        self.min_reversible = reversible
        self.rev = False
    def push(self):
        if self.rev:
            self.left, self.right = self.right, self.left
            if self.left:
                self.left.rev = not self.left.rev
                if self.right:
                    self.right.rev = not self.right.rev
                    self.rev = False
    def update(self):
        self.size = 1
        self.min_reversible = self.reversible
        if self.left:
            self.size += self.left.size
            self.min_reversible = min(self.min_reversible, self.left.min_reversible)
            if self.right:
                self.size += self.right.size
                self.min_reversible = min(self.min_reversible, self.right.min_reversible)
def split(node, k):
    if not node:
        return None, None
    node.push()
    l_size = (node.left.size if node.left else 0) + 1
    if l_size <= k:
        node.right, r = split(node.right, k - l_size)
        node.update()
        return node, r
    else:
        l, node.left = split(node.left, k)
        node.update()
        return l, node

def merge(l, r):
    if not l or not r:
        return l or r
    l.push()
    r.push()
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
    vals = []
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    flags = []
    for _ in range(n):
        flags.append(int(input_data[ptr]))
        ptr += 1
        
    root = None
    for i in range(n):
        root = merge(root, TreapNode(vals[i], flags[i]))
        
    q = int(input_data[ptr])
    ptr += 1
    
    invalid_count = 0
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == 'REVERSE': # Assuming op is implicitly reverse given usage, or part of op check
             pass
        # Actually code reads `op` then `l_pos`, `r_pos`. But logical structure implies just checking if mid is reversible.
        
        # Checking logic: `op = input_data[ptr]` might be 'REVERSE' or always same?
        # The code just blindly reads op, then l_pos, r_pos.
        # It doesn't check if op == 'REVERSE'.
        # Assuming op is just consumed.
        
        l_pos = int(input_data[ptr])
        ptr += 1
        r_pos = int(input_data[ptr])
        ptr += 1
        
        L, R = split(root, r_pos)
        L1, mid = split(L, l_pos - 1)
        
        if mid and mid.min_reversible == 1:
            mid.rev = not mid.rev
            root = merge(merge(L1, mid), R)
        else:
            invalid_count += 1
            root = merge(merge(L1, mid), R)
            
    print(invalid_count)
    res = []
    inorder(root, res)
    print(*(res))

def inorder(node, res):
    if not node:
        return
    node.push()
    inorder(node.left, res)
    res.append(node.val)
    inorder(node.right, res)
if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()