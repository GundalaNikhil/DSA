import sys
class Node:
    def __init__(self, val, nid):
        self.val = val
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
    node_map = {}
    shadow = {}
    head = None
    tail = None
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        new_node = Node(v, i)
        node_map[i] = new_node
        if i == 1:
            head = tail = new_node
            shadow[i] = -1
        else:
            shadow[i] = tail.id
            new_node.prev = tail
            tail.next = new_node
            tail = new_node
            
    next_id = n + 1
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == 'INS':
            u_id = int(input_data[ptr])
            ptr += 1
            x_val = int(input_data[ptr])
            ptr += 1
            
            # Logic: insert x AFTER u?
            u_node = node_map[u_id]
            new_node = Node(x_val, next_id)
            node_map[next_id] = new_node
            shadow[next_id] = u_id
            
            after_u = u_node.next
            u_node.next = new_node
            new_node.prev = u_node
            new_node.next = after_u
            
            if after_u:
                after_u.prev = new_node
            else:
                tail = new_node
            next_id += 1
            
        elif op == 'DEL':
            u_id = int(input_data[ptr])
            ptr += 1
            u_node = node_map[u_id]
            p = u_node.prev
            n = u_node.next
            
            if p:
                p.next = n
            else:
                head = n
                
            if n:
                n.prev = p
            else:
                tail = p
                
            u_node.prev = u_node.next = None
            
        elif op == 'SHADOW':
            u_id = int(input_data[ptr])
            ptr += 1
            print(shadow.get(u_id, -1))
if __name__ == '__main__':
    solve()