import sys
import random
class TreapNode:
    def __init__(self, val, locked):
        self.val = val
        self.locked = locked
        self.priority = random.random()
        self.left = None
        self.right = None
        self.size = 1
        self.locked_count = 1 if locked else 0
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
        self.locked_count = 1 if self.locked else 0
        if self.left:
            self.size += self.left.size
            self.locked_count += self.left.locked_count
            if self.right:
                self.size += self.right.size
                self.locked_count += self.right.locked_count
def split(node, k):
    if not node:
        return None, None
    node.push()
    left_size = (node.left.size if node.left else 0) + 1
    if left_size <= k:
        node.right, r = split(node.right, k - left_size)
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
def get_node_by_pos(root, k):
    l, r = split(root, k)
    l1, l2 = split(l, k - 1)
    res = l2
    root = merge(merge(l1, l2), r)
    return res, root
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    initial_vals = []
    for _ in range(n):
        initial_vals.append(int(input_data[ptr]))
        ptr += 1
        
    k_locked = int(input_data[ptr])
    ptr += 1
    
    locked_indices = set()
    for _ in range(k_locked):
        locked_indices.add(int(input_data[ptr]))
        ptr += 1
        
    root = None
    for i in range(n):
        node = TreapNode(initial_vals[i], (i + 1) in locked_indices)
        root = merge(root, node)
        
    q = int(input_data[ptr])
    ptr += 1
    
    invalid_count = 0
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'INS':
            u_pos = int(input_data[ptr])
            ptr += 1
            x_val = int(input_data[ptr])
            ptr += 1
            l, r = split(root, u_pos)
            l1, l2 = split(l, u_pos - 1)
            # Check lock
            # l2 is the node at u_pos (1-based)? No, split at u_pos gives l (size u_pos), r.
            # split(l, u_pos-1) gives l1 (size u_pos-1), l2 (size 1). l2 is the u_pos-th node.
            
            if l2 and l2.locked:
                invalid_count += 1
                root = merge(merge(l1, l2), r)
            else:
                new_node = TreapNode(x_val, False)
                # Where to insert? Original: merge(l1, l2) then merge new_node?
                # Actually insertion AT u_pos.
                # If we insert AT u_pos, we shift existing u_pos to right?
                # Code logic: `merge(merge(l1, l2), merge(new_node, r))` implies inserting AFTER u_pos?
                # Or wait. `l` is split at `u_pos`. `l` has `u_pos` elements.
                # `l2` is the last element of `l` (the `u_pos`-th element).
                # Inserting `new_node` after `l2` and before `r`.
                # So inserting AFTER u_pos.
                root = merge(merge(l1, l2), merge(new_node, r))
                
        elif op == 'DEL':
            u_pos = int(input_data[ptr])
            ptr += 1
            l, r = split(root, u_pos)
            l1, l2 = split(l, u_pos - 1)
            if l2 and l2.locked:
                invalid_count += 1
                root = merge(merge(l1, l2), r)
            else:
                root = merge(l1, r)
                
        elif op == 'REVERSE':
            l_pos = int(input_data[ptr])
            ptr += 1
            r_pos = int(input_data[ptr])
            ptr += 1
            
            # Split: [1..l-1], [l..r], [r+1..n]
            # split(root, r_pos) -> L (1..r), R (r+1..n)
            # split(L, l_pos - 1) -> L1 (1..l-1), mid (l..r)
            
            L, R = split(root, r_pos)
            L1, mid = split(L, l_pos - 1)
            # Check locks in mid?
            # Original: `if mid and mid.locked_count > 0:`
            if mid and mid.locked_count > 0:
                invalid_count += 1
                root = merge(merge(L1, mid), R)
            else:
                if mid:
                    mid.rev = not mid.rev
                root = merge(merge(L1, mid), R)
                
    print(invalid_count)
    
    final_output = []
    inorder(root, final_output)
    print(*(final_output))

def inorder(node, out):
    if not node:
        return
    node.push()
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)

if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()