import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    l0 = int(input_data[ptr])
    ptr += 1
    r0 = int(input_data[ptr])
    ptr += 1
    nodes = []
    adj = [[] for _ in range(n + 1)]
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        lo = int(input_data[ptr])
        ptr += 1
        hi = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        nodes.append((v, lo, hi))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    if root == -1:
        print("YES") # Empty tree trivially valid?
        return

    # BFS/DFS check
    stack = [(root, None)]
    is_valid = True
    
    while stack:
        u, p_val = stack.pop()
        v_u, lo_u, hi_u = nodes[u - 1]
        
        # Check global bounds
        if not (l0 <= v_u <= r0):
            is_valid = False
            break
            
        # Check parent constraint
        if p_val is not None:
             # Waterfall constraint: v_u must be within [p_val + lo_u, p_val + hi_u]
             # Assuming lo_u, hi_u are relative bounds from parent value
             if not (p_val + lo_u <= v_u <= p_val + hi_u):
                 is_valid = False
                 break
                 
        for child in adj[u]:
            stack.append((child, v_u))
            
    if is_valid:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
