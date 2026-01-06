import random
import sys
class Node:
    __slots__ = ["val", "priority", "left", "right", "size"]
    def __init__(self, val, priority, left=None, right=None):
        self.val = val
        self.priority = priority
        self.left = left
        self.right = right
        self.size = 1
        if left:
            self.size += left.size
            if right:
                self.size += right.size
def split(node, k):
    if not node:
        return None, None
    left_size = node.left.size if node.left else 0
    if left_size + 1 <= k:
        l, r = split(node.right, k - left_size - 1)
        return Node(node.val, node.priority, node.left, l), r
    else:
        l, r = split(node.left, k)
        return l, Node(node.val, node.priority, r, node.right)

def merge(l, r):
    if not l or not r:
        return l or r
    if l.priority > r.priority:
        return Node(l.val, l.priority, l.left, merge(l.right, r))
    else:
        return Node(r.val, r.priority, merge(l, r.left), r.right)
def get_val(node, k):
    if not node or k > node.size or k < 1:
        return -1
    left_size = node.left.size if node.left else 0
    if left_size + 1 == k:
        return node.val
    if k <= left_size:
        return get_val(node.left, k)
    return get_val(node.right, k - left_size - 1)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    root0 = None
    root0 = None
    for _ in range(n):
        v = int(input_data[ptr])
        ptr += 1
        root0 = merge(root0, Node(v, random.random()))
        
    versions = [root0]
    q_str = input_data[ptr]
    ptr += 1
    q = int(q_str)
    
    output = []
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == "INS":
            v_idx = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            
            root = versions[v_idx]
            L, R = split(root, pos - 1)
            new_node = Node(x, random.random())
            new_root = merge(merge(L, new_node), R)
            versions.append(new_root)
            
        elif op == "DEL":
            v_idx = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            
            root = versions[v_idx]
            L, R = split(root, pos)
            L1, L2 = split(L, pos - 1)
            new_root = merge(L1, R)
            versions.append(new_root)
            
        elif op == "GET":
            v_idx = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            
            root = versions[v_idx]
            output.append(str(get_val(root, pos)))
            
    if output:
        sys.stdout.write("\n".join(output) + "\n")
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    solve()