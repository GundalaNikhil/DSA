import sys
import random
class TreapNode:
    def __init__(self, e_type, val):
        self.e_type = e_type
        self.val = val if e_type == '+' else -val
        self.abs_val = val
        self.priority = random.random()
        self.left = None
        self.right = None
        self.size = 1
        self.subtree_sum = self.val
    def update(self):
        self.size = 1
        self.subtree_sum = self.val
        if self.left:
            self.size += self.left.size
            self.subtree_sum += self.left.subtree_sum
            if self.right:
                self.size += self.right.size
                self.subtree_sum += self.right.subtree_sum
def split(node, k):
    if not node:
        return None, None
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
    q = int(input_data[ptr])
    ptr += 1
    root = None
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'APPEND':
            t = input_data[ptr]
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            node = TreapNode(t, v)
            root = merge(root, node)
            
        elif op == 'COMPACT':
            if not root:
                continue
            
            nodes = []
            inorder(root, nodes)
            
            if not nodes:
                root = None
                continue
                
            compacted = []
            curr_type, curr_sum = nodes[0]
            
            for i in range(1, len(nodes)):
                t, v = nodes[i]
                if t == curr_type:
                    # check overflow? assuming python large int okay
                    # "sum" means + or -? 
                    # Code: `curr_sum += v`? 
                    # v is abs_val. 
                    # Wait, v stores absolute?
                    # Line 71: `nodes.append((node.e_type, abs(node.val)))`.
                    # Line 78: `curr_type, curr_sum = nodes[0]`.
                    # Line 82: `curr_sum += v`.
                    curr_sum += v
                else:
                    compacted.append((curr_type, curr_sum))
                    curr_type = t
                    curr_sum = v
                    
            compacted.append((curr_type, curr_sum))
            
            root = None
            for t, v in compacted:
                # Reconstruct treap
                root = merge(root, TreapNode(t, v))
                
        elif op == 'REPLAY':
            l_pos = int(input_data[ptr])
            ptr += 1
            r_pos = int(input_data[ptr])
            ptr += 1
            L, R = split(root, r_pos)
            L1, mid = split(L, l_pos - 1)
            print(mid.subtree_sum if mid else 0)
            root = merge(merge(L1, mid), R)

def inorder(node, nodes):
    if not node:
        return
    inorder(node.left, nodes)
    nodes.append((node.e_type, abs(node.val)))
    inorder(node.right, nodes)
if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()