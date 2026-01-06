import sys


class Node:
    def __init__(self, val, group_id, nid):
        self.val = val
        self.group_id = group_id
        self.id = nid
        self.prev = None
        self.next = None


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    group_ids = []
    for _ in range(n):
        group_ids.append(int(input_data[ptr]))
        ptr += 1
        
    node_map = {}
    group_counts = {}
    head = None
    last = None
    
    for i in range(1, n + 1):
        v = vals[i - 1]
        g = group_ids[i - 1]
        node = Node(v, g, i)
        node_map[i] = node
        group_counts[g] = group_counts.get(g, 0) + 1
        
        if not head:
            head = node
        else:
            last.next = node
            node.prev = last
        last = node
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == "COUNT":
            g = int(input_data[ptr])
            ptr += 1
            print(group_counts.get(g, 0))
        else:
            u_id = int(input_data[ptr])
            ptr += 1
            v_id = int(input_data[ptr])
            ptr += 1
            
            u = node_map[u_id]
            v = node_map[v_id]
            
            if u.group_id != v.group_id or u == v:
                continue
                
            if op == "SWAP":
                # Swap logic for doubly linked list nodes u and v
                # This is complex, need to handle adjacency and head references
                pass # Logic already existed, but was deeply nested. 
                # Re-implementing simplified swap for clarity is risky without full context of edge cases.
                # However, the provided structure was deeply intertwined.
                # I will preserve the logic but clean up the nesting.
                
                # Check adjacency
                if u.next == v: # u -> v
                    up, vn = u.prev, v.next
                    if up: up.next = v
                    else: head = v
                    v.prev = up
                    v.next = u
                    u.prev = v
                    u.next = vn
                    if vn: vn.prev = u
                elif v.next == u: # v -> u
                    vp, un = v.prev, u.next
                    if vp: vp.next = u
                    else: head = u
                    u.prev = vp
                    u.next = v
                    v.prev = u
                    v.next = un
                    if un: un.prev = v
                else:
                    # Non-adjacent swap
                    up, un = u.prev, u.next
                    vp, vn = v.prev, v.next
                    
                    if up: up.next = v
                    else: head = v
                    v.prev = up
                    v.next = un
                    if un: un.prev = v
                    
                    if vp: vp.next = u
                    else: head = u
                    u.prev = vp
                    u.next = vn
                    if vn: vn.prev = u

            elif op == "MOVE":
                # Move u after v
                # Remove u
                up, un = u.prev, u.next
                if up: up.next = un
                else: head = un
                if un: un.prev = up
                
                # Insert u after v
                vn = v.next
                v.next = u
                u.prev = v
                u.next = vn
                if vn: vn.prev = u

if __name__ == "__main__":
    solve()
