import random
import sys
class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.is_deleted = False
    def update(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
            if self.right:
                self.size += self.right.size
def split(root, k):
    if not root:
        return None, None
    left_size = (root.left.size if root.left else 0) + 1
    if left_size <= k:
        root.right, r = split(root.right, k - left_size)
        if root.right:
            root.right.parent = root
            if r:
                r.parent = None
                root.update()
                return root, r
        else:
            l, root.left = split(root.left, k)
            if root.left:
                root.left.parent = root
                if l:
                    l.parent = None
                    root.update()
                    return l, root
def merge(l, r):
    if not l or not r:
        if l:
            l.parent = None
            if r:
                r.parent = None
                return l or r
            if l.priority > r.priority:
                l.right = merge(l.right, r)
                if l.right:
                    l.right.parent = l
                    l.update()
                    return l
            else:
                r.left = merge(l, r.left)
                if r.left:
                    r.left.parent = r
                    r.update()
                    return r
def get_node_at_pos(root, k):
    if not root or k > root.size or k < 1:
        return None
    l_size = root.left.size if root.left else 0
    if l_size + 1 == k:
        return root
    if k <= l_size:
        return get_node_at_pos(root.left, k)
    return get_node_at_pos(root.right, k - l_size - 1)
def get_next_node(node):
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
            return curr
        curr = node
        while curr.parent and curr.parent.right == curr:
            curr = curr.parent
            return curr.parent
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    h_count = int(input_data[ptr])
    ptr += 1
    root = None
    for _ in range(n):
        val = int(input_data[ptr])
        ptr += 1
        root = merge(root, Node(val, random.random()))
        
    heads = [None] * (h_count + 1)
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == "HEAD":
            i = int(input_data[ptr])
            ptr += 1
            p = int(input_data[ptr])
            ptr += 1
            heads[i] = get_node_at_pos(root, p)
            
        elif op == "DEL":
            i = int(input_data[ptr])
            ptr += 1
            node = heads[i]
            if not node:
                continue
                
            r = get_rank(node)
            next_node = get_next_node(node)
            
            L, R = split(root, r)
            L1, L2 = split(L, r - 1)
            # L2 is the node to delete
            if L2:
                L2.is_deleted = True
            
            # Re-merge L1 and R, dropping L2
            root = merge(L1, R)
            
            # Update heads pointing to deleted node?
            # Code: `if heads[h] == node: heads[h] = next_node`
            for h in range(1, h_count + 1):
                if heads[h] == node:
                    heads[h] = next_node
                    
        elif op == "INS":
            i = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            
            node = heads[i]
            if not node:
                # Insert at end? Or start? 
                # If head undefined, maybe treat rank as 0?
                # Code: `if not node: continue`. So implies skipping.
                continue
                
            r = get_rank(node)
            # Insert AFTER node? Code: `split(root, r - 1)`.
            # L (0..r-1), R (r..n).
            # `merge(merge(L, new_node), R)`.
            # This inserts at index `r`. Original was at `r` (1-based)?
            # If `r` is rank of node `heads[i]`. `L` has `r-1` nodes.
            # New node becomes rank `r`.
            # It seems to insert BEFORE heads[i].
            
            L, R = split(root, r - 1)
            new_node = Node(x, random.random())
            root = merge(merge(L, new_node), R)
            
        elif op == "PRINT":
            i = int(input_data[ptr])
            ptr += 1
            curr = heads[i]
            res = []
            if not curr:
                print("")
                continue
            
            # Traverse suffix starting from curr
            # Need strict order traversal.
            # Code used `get_suffix(curr)`?
            # Helper `get_suffix` seemed missing or empty.
            # Replaced with logic?
            # `traverse` function logic:
            # `r = get_rank(node_start)`
            # `L, R_part = split(root, r - 1)`
            # `traverse(R_part)` (inorder)
            # `root = merge(L, R_part)`
            
            r = get_rank(curr)
            L, R_part = split(root, r - 1)
            final_res = []
            inorder_collect(R_part, final_res)
            print(*(final_res))
            root = merge(L, R_part)

def inorder_collect(node, res):
    if not node:
        return
    # Push? Treap needs push? (Not in this file, simple BST logic?)
    # Lines 7-17 only show update, no push.
    inorder_collect(node.left, res)
    res.append(node.val)
    inorder_collect(node.right, res)
def get_rank(curr):
    rank = (curr.left.size if curr.left else 0) + 1
    while curr.parent:
        if curr.parent.right == curr:
            rank += (curr.parent.left.size if curr.parent.left else 0) + 1
        curr = curr.parent
    return rank

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    solve()