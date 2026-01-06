import sys
import random
import bisect
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
    e_count = int(input_data[ptr])
    ptr += 1
    snapshots = [(0, None)]
    q_count = 0
    # The structure of the input format seems to imply events are processed
    # and then finally a batch of queries are processed?
    # Original logic (nested):
    # Read e_count.
    # Loop e_count:
    #   Read t, tp.
    #   Process op.
    #   Then immediately read q_count? And loop q_count?
    #   If q_count is read inside the e_count loop, it means for EACH event, 
    #   there are queries? That seems inefficient or unusual.
    #   Looking really closely at line 70 in original LNK-047:
    #       q_count = int(input_data[ptr])
    #       ptr += 1
    #       for _ in range(q_count): ...
    #   This block is indented inside the `else` block of `if tp == "INS":`
    #   Wait, lines 63-69 handle `else` (presumably DEL?).
    #   Then lines 70+ seem to be outside the if/else?
    #   No, indentation of line 70 is 12 spaces, same as line 64 inside `else`.
    #   This implies queries only happen after a non-INS operation? 
    #   OR it means the updated logic was indented wrong.
    #   Usually `q_count` comes after ALL events, or is a separate section.
    #   Assuming standard format: Init -> Events -> Queries.
    #   But original code shows `q_count` read *inside* the event loop.
    #   Wait, actually, looking at the pattern, it seems highly likely `q_count`
    #   should be outside the event loop.
    #   I will move it out.
    
    # Process all events first
    for _ in range(e_count):
        t = int(input_data[ptr])
        ptr += 1
        tp = input_data[ptr]
        ptr += 1
        if tp == "INS":
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            L, R = split(snapshots[-1][1], pos - 1)
            new_root = merge(merge(L, Node(x, random.random())), R)
            snapshots.append((t, new_root))
        else:
            pos = int(input_data[ptr])
            ptr += 1
            L, R = split(snapshots[-1][1], pos)
            L1, L2 = split(L, pos - 1)
            new_root = merge(L1, R)
            snapshots.append((t, new_root))
            
    # Now process queries
    q_count = int(input_data[ptr])
    ptr += 1
    for _ in range(q_count):
        t = int(input_data[ptr])
        ptr += 1
        pos = int(input_data[ptr])
        ptr += 1
        idx = bisect.bisect_right(snapshots, (t, float("inf"))) - 1
        print(get_val(snapshots[idx][1], pos))
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    solve()