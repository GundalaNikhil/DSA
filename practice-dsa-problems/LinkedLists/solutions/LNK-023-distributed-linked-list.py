import sys
import random
class Node:
    def __init__(self, val, shard_id):
        self.val = val
        self.shard_id = shard_id
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
def get_shard(root, k):
    if k < 1 or k > (root.size if root else 0):
        return -1
    l_size = root.left.size if root.left else 0
    if l_size + 1 == k:
        return root.shard_id
    if k <= l_size:
        return get_shard(root.left, k)
    return get_shard(root.right, k - l_size - 1)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s_count = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    vals = []
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    shards = []
    for _ in range(n):
        shards.append(int(input_data[ptr]))
        ptr += 1
        
    root = None
    for i in range(n):
        root = merge(root, Node(vals[i], shards[i]))
        
    for op_idx in range(1, q + 1):
        op_type = input_data[ptr]
        ptr += 1
        
        if op_type == 'INS':
            pos = int(input_data[ptr])
            ptr += 1
            val = int(input_data[ptr])
            ptr += 1
            k = int(input_data[ptr])
            ptr += 1
            
            locks = set()
            for _ in range(k):
                locks.add(int(input_data[ptr]))
                ptr += 1
                
            required = set()
            shard_pos = get_shard(root, pos)
            shard_prev = get_shard(root, pos - 1)
            
            if shard_pos != -1:
                required.add(shard_pos)
            if shard_prev != -1:
                required.add(shard_prev)
                
            if not required.issubset(locks):
                print(op_idx)
                return
                
            assigned_shard = shard_pos if shard_pos != -1 else 1
            L, R = split(root, pos - 1)
            new_n = Node(val, assigned_shard)
            root = merge(merge(L, new_n), R)
            
        elif op_type == 'DEL':
            pos = int(input_data[ptr])
            ptr += 1
            k = int(input_data[ptr])
            ptr += 1
            
            locks = set()
            for _ in range(k):
                locks.add(int(input_data[ptr]))
                ptr += 1
                
            required = set()
            shard_pos = get_shard(root, pos)
            shard_prev = get_shard(root, pos - 1)
            
            if shard_pos != -1:
                required.add(shard_pos)
            if shard_prev != -1:
                required.add(shard_prev)
                
            if not required.issubset(locks):
                print(op_idx)
                return
                
            L, R = split(root, pos)
            L1, L2 = split(L, pos - 1)
            root = merge(L1, R)
            
    print(0)
if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()