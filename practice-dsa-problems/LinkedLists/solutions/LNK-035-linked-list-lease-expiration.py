import sys
import random
import heapq

# Classes and Helper Functions at top level
class TreapNode:
    def __init__(self, val, expiry):
        self.val = val
        self.expiry = expiry
        self.priority = random.random()
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.alive = True

    def update(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size
        
        # Maintain parent pointers
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

def merge_t(l, r):
    if not l or not r:
        return l or r
    if l.priority > r.priority:
        l.right = merge_t(l.right, r)
        l.update()
        l.parent = None
        return l
    else:
        r.left = merge_t(l, r.left)
        r.update()
        r.parent = None
        return r

def split_t(root, k):
    if not root:
        return None, None
    l_size = (root.left.size if root.left else 0) + 1
    if l_size <= k:
        root.right, r = split_t(root.right, k - l_size)
        root.update()
        if root.right:
            root.right.parent = root
        if r:
            r.parent = None
        return root, r
    else:
        l, root.left = split_t(root.left, k)
        root.update()
        if root.left:
            root.left.parent = root
        if l:
            l.parent = None
        return l, root

def get_rank_t(node):
    rank = (node.left.size if node.left else 0) + 1
    curr = node
    while curr.parent:
        if curr.parent.right == curr:
            rank += (curr.parent.left.size if curr.parent.left else 0) + 1
        curr = curr.parent
    return rank

# Main solve function with cleaner structure
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
        
    initial_leases = []
    for _ in range(n):
        initial_leases.append(int(input_data[ptr]))
        ptr += 1
        
    root = None
    heap = []
    
    for i in range(n):
        node = TreapNode(initial_vals[i], initial_leases[i])
        root = merge_t(root, node)
        heapq.heappush(heap, (node.expiry, id(node), node))
        
    q = int(input_data[ptr])
    ptr += 1
    
    # Internal cleanup helper using closure variables
    def cleanup(t):
        nonlocal root
        while heap and heap[0][0] <= t:
            exp, _, node = heapq.heappop(heap)
            if node.alive:
                rank = get_rank_t(node)
                L, R = split_t(root, rank)
                L1, L2 = split_t(L, rank - 1)
                # Node removed (L2)
                root = merge_t(L1, R)
                node.alive = False

    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'INS':
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            lease = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            
            cleanup(t)
            
            new_node = TreapNode(x, t + lease)
            L, R = split_t(root, pos - 1)
            root = merge_t(merge_t(L, new_node), R)
            heapq.heappush(heap, (new_node.expiry, id(new_node), new_node))
            
        elif op == 'RENEW':
            pos = int(input_data[ptr])
            ptr += 1
            lease = int(input_data[ptr])
            ptr += 1
            t_curr = int(input_data[ptr])
            ptr += 1
            
            cleanup(t_curr)
            
            if not root or pos < 1 or pos > root.size:
                continue

            L, R = split_t(root, pos)
            L1, L2 = split_t(L, pos - 1)
            
            if L2:
                # Renew lease
                L2.expiry += lease
                heapq.heappush(heap, (L2.expiry, id(L2), L2))
                root = merge_t(merge_t(L1, L2), R)
            else:
                # Should not happen if pos is valid, but safe fallback
                root = merge_t(L1, R)
                
        elif op == 'GET':
            pos = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            
            cleanup(t)
            
            if not root or pos < 1 or pos > root.size:
                print("-1")
            else:
                L, R = split_t(root, pos)
                L1, L2 = split_t(L, pos - 1)
                print(L2.val if L2 else "-1")
                root = merge_t(merge_t(L1, L2), R)

if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    solve()