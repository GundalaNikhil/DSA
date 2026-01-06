import sys


class Node:
    def __init__(self, val, nid):
        self.val = val
        self.id = nid
        self.prev = 0
        self.next = 0


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    node_map = {}
    last = 0
    for i in range(1, n + 1):
        val = int(input_data[ptr])
        ptr += 1
        node = Node(val, i)
        node_map[i] = node
        if last != 0:
            node_map[last].next = i
            node.prev = last
        last = i
        
    for op_idx in range(1, q + 1):
        op_type = input_data[ptr]
        ptr += 1
        
        if op_type == "DEL":
            u = int(input_data[ptr])
            ptr += 1
            exp_p = int(input_data[ptr])
            ptr += 1
            exp_n = int(input_data[ptr])
            ptr += 1
            
            if u not in node_map:
                print(op_idx)
                return
            
            node = node_map[u]
            if node.prev != exp_p or node.next != exp_n:
                print(op_idx)
                return
            
            p = node.prev
            n_next = node.next
            
            if p != 0:
                node_map[p].next = n_next
            if n_next != 0:
                node_map[n_next].prev = p
            
            del node_map[u]
        
        elif op_type == "INS":
            u = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            exp_p = int(input_data[ptr])
            ptr += 1
            exp_n = int(input_data[ptr])
            ptr += 1
            
            # Validation logic
            # Previous must point to next?
            # Or insertion between p and n?
            # Check p.next == n and n.prev == p?
            # Check if exp_p -> exp_n
            
            # Check if p exists and points to n
            if exp_p != 0:
                if exp_p not in node_map or node_map[exp_p].next != exp_n:
                    print(op_idx)
                    return
            else:
                # If p is 0 (start), n must be current start (prev=0)
                if exp_n != 0:
                    if exp_n not in node_map or node_map[exp_n].prev != 0:
                        print(op_idx)
                        return
                    
            # Check if n exists and points back to p 
            if exp_n != 0:
                if exp_n not in node_map or node_map[exp_n].prev != exp_p:
                    print(op_idx)
                    return
            else:
                 # If n is 0 (end), p must be current end (next=0)
                 if exp_p != 0:
                    if exp_p not in node_map or node_map[exp_p].next != 0:
                        print(op_idx)
                        return
                        
            # All valid, perform insert
            new_node = Node(x, u)
            new_node.prev = exp_p
            new_node.next = exp_n
            node_map[u] = new_node
            
            if exp_p != 0:
                node_map[exp_p].next = u
            if exp_n != 0:
                node_map[exp_n].prev = u
                
    print(0)

if __name__ == "__main__":
    solve()
