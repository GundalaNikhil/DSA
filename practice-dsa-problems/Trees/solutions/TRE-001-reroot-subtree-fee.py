import sys

sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        c_fee = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    sz = [0] * (n + 1)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    up = [[0] * 20 for _ in range(n + 1)]
    
    timer = 0
    
    
    stack = [(1, 0, 0)]
   
    
    traversal_order = []
    
   
    call_stack = [1]
    parent[1] = 0
    depth[1] = 0
    
    
    stack = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    
    
    
    node_state = [0] * (n + 1)  
    stack = [1]
    
    while stack:
        u = stack[-1]
        if node_state[u] == 0:
            # Entry
            timer += 1
            tin[u] = timer
            node_state[u] = 1
            up[u][0] = parent[u]
            # Add children to stack
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)
        elif node_state[u] == 1:
            # After children processed
            node_state[u] = 2
            stack.pop()
            timer += 1
            tout[u] = timer
            # Compute size
            current_size = 1
            for v in adj[u]:
                if v != parent[u]:
                    current_size += sz[v]
            sz[u] = current_size
        else:
            stack.pop()

    # Binary Lifting Precomputation
    for j in range(1, 20):
        for i in range(1, n + 1):
            if up[i][j-1] != 0:
                up[i][j] = up[up[i][j-1]][j-1]
            else:
                up[i][j] = 0

    def check_ancestor(u, v):
        # Returns True if u is ancestor of v (or u == v)
        return tin[u] <= tin[v] and tout[u] >= tout[v]

    def get_child_on_path(r, x):
        curr = r
        for j in range(19, -1, -1):
            if depth[curr] - (1 << j) > depth[x]:
                curr = up[curr][j]
        
        target_depth = depth[x] + 1
        if depth[curr] < target_depth:
            return -1
        
        for j in range(19, -1, -1):
            if depth[curr] - (1 << j) >= target_depth:
                curr = up[curr][j]
        
        return curr

    prev_root = -1
    output = []
    
    for _ in range(q):
        try:
            r = int(next(iterator))
            x = int(next(iterator))
        except StopIteration:
            break
            
        fee = 0
        if prev_root != -1 and r != prev_root:
            fee = c_fee
        prev_root = r
        
        ans = 0
        if r == x:
            ans = n
        elif check_ancestor(x, r):
            child = get_child_on_path(r, x)
            ans = n - sz[child]
        else:
            ans = sz[x]
            
        output.append(str(ans + fee))
        
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()
