import sys
class Node:
    def __init__(self, sum=0, left=None, right=None):
        self.sum = sum
        self.left = left
        self.right = right
def build(l, r, a):
    if l == r:
        return Node(a[l - 1])
    mid = (l + r) // 2
    left_child = build(l, mid, a)
    right_child = build(mid + 1, r, a)
    return Node(left_child.sum + right_child.sum, left_child, right_child)
def update(node, l, r, idx, val):
    if l == r:
        return Node(val)
    mid = (l + r) // 2
    if idx <= mid:
        new_left = update(node.left, l, mid, idx, val)
        return Node(new_left.sum + node.right.sum, new_left, node.right)
    else:
        new_right = update(node.right, mid + 1, r, idx, val)
        return Node(node.left.sum + new_right.sum, node.left, new_right)

def query(node, l, r, ql, qr):
    if ql <= l and r <= qr:
        return node.sum
    mid = (l + r) // 2
    res = 0
    if ql <= mid:
        res += query(node.left, l, mid, ql, qr)
    if qr > mid:
        res += query(node.right, mid + 1, r, ql, qr)
    return res

# Array-based implementation helpers (Persistent Segment Tree usually uses pointers/objects, 
# or arrays. The file has BOTH Node class AND array-based functions `build_arr` nested inside `solve`.
# I will lift the array-based ones out and use them correctly, or stick to Node class if that's "Persistent".
# Actually, the file uses `roots` (array of Nodes?) in the query loop.
# But it calls `update_arr` and `query_arr`.
# `update_arr` returns `curr` (int index).
# `query` uses `node` (Node object) but `query_arr` uses `node` (int index).
# The code mixes two implementations?
# Lines 2-23 defines `Node` and `update` (object based).
# Lines 52-89 defines `build_arr`, `update_arr` (array based).
# `solve` builds `roots = [build_arr(1, n)]`.
# So it uses the Array-based implementation.
# The Object-based implementation is dead code or vestigial.
# I will remove the Object-based one to clean up, OR I will just fix the array-based one.
# Given "Persistent Segment Tree", array-based often saves memory overhead of objects in Python.
# I will use the array-based one, move it to global scope.

MAX_NODES = 200000 * 25 # Heuristic size? n, q ~ 2e5?
L = [0] * MAX_NODES
R = [0] * MAX_NODES
S = [0] * MAX_NODES
node_ptr = 1

def build_arr(l, r, a):
    global node_ptr
    curr = node_ptr
    node_ptr += 1
    if l == r:
        S[curr] = a[l - 1]
        return curr
    mid = (l + r) // 2
    L[curr] = build_arr(l, mid, a)
    R[curr] = build_arr(mid + 1, r, a)
    S[curr] = S[L[curr]] + S[R[curr]]
    return curr

def update_arr(prev_node, l, r, idx, val):
    global node_ptr
    curr = node_ptr
    node_ptr += 1
    if l == r:
        S[curr] = val
        return curr
    mid = (l + r) // 2
    L[curr] = L[prev_node]
    R[curr] = R[prev_node]
    if idx <= mid:
        L[curr] = update_arr(L[prev_node], l, mid, idx, val)
    else:
        R[curr] = update_arr(R[prev_node], mid + 1, r, idx, val)
    S[curr] = S[L[curr]] + S[R[curr]]
    return curr

def query_arr(node, l, r, ql, qr):
    if ql <= l and r <= qr:
        return S[node]
    mid = (l + r) // 2
    res = 0
    if ql <= mid:
        res += query_arr(L[node], l, mid, ql, qr)
    if qr > mid:
        res += query_arr(R[node], mid + 1, r, ql, qr)
    return res

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        a.append(int(input_data[ptr]))
        ptr += 1
        
    # Standardize Global Arrays size based on n+q if needed
    # (Global variables declared above)
    
    roots = [build_arr(1, n, a)]
    out = []
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == "U":
            v = int(input_data[ptr])
            ptr += 1
            idx = int(input_data[ptr])
            ptr += 1
            val = int(input_data[ptr])
            ptr += 1
            # Update version `v` to create new version
            # Problem says "Persistent Segment Tree Historical Queries".
            # Usually creates a new version from `v`. If we append to roots,
            # new version ID is `len(roots)`.
            roots.append(update_arr(roots[v], 1, n, idx, val))
        else: # Q
            v = int(input_data[ptr])
            ptr += 1
            ql = int(input_data[ptr])
            ptr += 1
            qr = int(input_data[ptr])
            ptr += 1
            out.append(str(query_arr(roots[v], 1, n, ql, qr)))
            
    sys.stdout.write("\n".join(out) + "\n")
if __name__ == "__main__":
    solve()