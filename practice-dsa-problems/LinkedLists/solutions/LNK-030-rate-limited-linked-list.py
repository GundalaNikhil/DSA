import sys
import random
class Node:
    def __init__(self, val):
        self.val = val
        self.priority = random.random()
        self.left = None
        self.right = None
        self.size = 1
        self.last_mod = -float('inf')
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
def get_node(root, k):
    if not root or k < 1 or k > root.size:
        return None
    l_size = root.left.size if root.left else 0
    if l_size + 1 == k:
        return root
    if k <= l_size:
        return get_node(root.left, k)
    return get_node(root.right, k - l_size - 1)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    c_limit = int(input_data[ptr])
    ptr += 1
    root = None
    root = None
    for _ in range(n):
        v = int(input_data[ptr])
        ptr += 1
        root = merge(root, Node(v))
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'SET':
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            node = get_node(root, pos)
            if node and t - node.last_mod >= c_limit:
                node.val = x
                node.last_mod = t
                
        elif op == 'DEL':
            pos = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            node = get_node(root, pos)
            if node and t - node.last_mod >= c_limit:
                L, R = split(root, pos)
                L1, L2 = split(L, pos - 1)
                root = merge(L1, R)
                
        elif op == 'GET':
            pos = int(input_data[ptr])
            ptr += 1
            node = get_node(root, pos)
            print(node.val if node else -1)
if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()