import sys
import random
class Node:
    __slots__ = ['val', 'priority', 'left', 'right', 'size']
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
    l_size = node.left.size if node.left else 0
    if l_size + 1 <= k:
        l, r = split(node.right, k - l_size - 1)
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
    if not node or k < 1 or k > node.size:
        return -1
    l_size = node.left.size if node.left else 0
    if l_size + 1 == k:
        return node.val
    if k <= l_size:
        return get_val(node.left, k)
    return get_val(node.right, k - l_size - 1)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    root = None
    for _ in range(n):
        v = int(input_data[ptr])
        ptr += 1
        root = merge(root, Node(v, random.random()))
        
    versions = [root]
    curr_idx = 0
    
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'INS':
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            
            # Truncate future versions on modification
            versions = versions[:curr_idx + 1]
            L, R = split(versions[-1], pos - 1)
            new_root = merge(merge(L, Node(x, random.random())), R)
            versions.append(new_root)
            curr_idx += 1
            
        elif op == 'DEL':
            pos = int(input_data[ptr])
            ptr += 1
            
            if versions[curr_idx] and 1 <= pos <= versions[curr_idx].size:
                versions = versions[:curr_idx + 1]
                L, R = split(versions[-1], pos)
                L1, L2 = split(L, pos - 1)
                new_root = merge(L1, R)
                versions.append(new_root)
                curr_idx += 1
                
        elif op == 'UNDO':
            if curr_idx > 0:
                curr_idx -= 1
        elif op == 'REDO':
            if curr_idx < len(versions) - 1:
                curr_idx += 1
        elif op == 'GET':
            pos = int(input_data[ptr])
            ptr += 1
            print(get_val(versions[curr_idx], pos))
if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()