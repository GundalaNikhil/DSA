import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    f_count = int(input_data[ptr])
    ptr += 1
    injected = set()
    # If f_count > 0, we read injected nodes
    if f_count > 0:
        for _ in range(f_count):
            injected.add(int(input_data[ptr]))
            ptr += 1
            
    nodes = []
    adj = [[] for _ in range(n + 1)]
    root = -1
    
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        b = int(input_data[ptr])
        ptr += 1
        t = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        nodes.append((v, b, t))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    def evaluate(u):
        v_u, b_u, t_u = nodes[u - 1]
        is_injected = u in injected
        
        curr_val = b_u if is_injected else v_u
        curr_faulty = 1 if is_injected else 0
        
        total_val = curr_val
        total_faulty = curr_faulty
        
        for v_child in adj[u]:
            child_val, child_faulty = evaluate(v_child)
            total_val += child_val
            total_faulty += child_faulty
            
        if total_faulty > t_u:
            # Fault tolerance exceeded: Node fails completely?
            # Return (0, 0) effectively pruning this subtree's contribution?
            # Or propagating faultiness? Assuming pruning/failure.
            return (0, 0) 
        else:
            return (total_val, total_faulty)

    sys.setrecursionlimit(300000)
    if root != -1:
        res_val, _ = evaluate(root)
        print(res_val)
    else:
        print(0)


if __name__ == "__main__":
    solve()
