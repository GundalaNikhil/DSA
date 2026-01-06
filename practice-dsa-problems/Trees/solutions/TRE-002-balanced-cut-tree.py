import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        threshold = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    x_count = int(next(iterator))
    x_set = set()
    root_x = -1
    for _ in range(x_count):
        val = int(next(iterator))
        x_set.add(val)
        root_x = val
        
    y_count = int(next(iterator))
    y_set = set()
    for _ in range(y_count):
        val = int(next(iterator))
        y_set.add(val)
        
    # Logic:
    # We want to remove one edge (u, v) such that:
    # 1. one component contains all X, other contains all Y.
    # 2. Difference in size of components <= threshold.
    # 3. Edge weight is minimized.
    
    # We can root the tree arbitrarily, say at node 1.
    # However, 'root_x' was picked from input. Let's start DFS from root_x for convenience?
    # Or just root at 1. Let's root at 1.
    
    root = 1
    
    # We need to compute for each subtree (defined by edge to parent):
    # - size
    # - count of X nodes
    # - count of Y nodes
    
    # If we cut edge (u, parent[u]):
    # Subtree u contains `cnt_x[u]` X-nodes and `cnt_y[u]` Y-nodes.
    # The other component contains `total_x - cnt_x[u]` and `total_y - cnt_y[u]`.
    
    # Valid split condition:
    # (cnt_x[u] == total_x AND cnt_y[u] == 0)  => All X in subtree, All Y outside
    # OR
    # (cnt_x[u] == 0 AND cnt_y[u] == total_y)  => All Y in subtree, All X outside
    
    # Balance condition:
    # Size of subtree A: sz[u]
    # Size of component B: n - sz[u]
    # Diff: abs(sz[u] - (n - sz[u])) <= threshold
    
    inf = float("inf")
    min_w = inf
    
    # Iterative DFS to compute subtree info
    stack = [root]
    parent = {root: 0}
    weight_to_parent = {root: 0}
    
    # Build traverse order
    order = []
    stack = [root]
    visited = [False] * (n + 1)
    visited[root] = True
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                weight_to_parent[v] = w
                stack.append(v)
                
    sz = [0] * (n + 1)
    cnt_x = [0] * (n + 1)
    cnt_y = [0] * (n + 1)
    
    # Bottom-up processing
    for u in reversed(order):
        sz[u] = 1
        cnt_x[u] = 1 if u in x_set else 0
        cnt_y[u] = 1 if u in y_set else 0
        
        for v, w in adj[u]:
            if v != parent[u]: # v is child
                sz[u] += sz[v]
                cnt_x[u] += cnt_x[v]
                cnt_y[u] += cnt_y[v]
    
    # Check edges
    # The edge above u is (u, parent[u]) with weight weight_to_parent[u]
    for u in range(1, n + 1):
        if u == root:
            continue
            
        w = weight_to_parent[u]
        
        # Check simple split validity
        # Case 1: Subtree u has all X, no Y
        in_subtree_valid_1 = (cnt_x[u] == x_count) and (cnt_y[u] == 0)
        
        # Case 2: Subtree u has all Y, no X
        in_subtree_valid_2 = (cnt_x[u] == 0) and (cnt_y[u] == y_count)
        
        if in_subtree_valid_1 or in_subtree_valid_2:
            size_subtree = sz[u]
            size_other = n - sz[u]
            if abs(size_subtree - size_other) <= threshold:
                if w < min_w:
                    min_w = w
                    
    print(min_w if min_w != inf else -1)

if __name__ == "__main__":
    solve()
