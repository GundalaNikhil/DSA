import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def critical_nodes(n: int, edges: list[tuple[int, int, int]]) -> list[int]:
    adj = [[] for _ in range(n)]
    degree_R = [0] * n
    degree_B = [0] * n
    
    total_R_edges = 0
    total_B_edges = 0
    
    # Pre-process edges to handle multigraphs correctly if any, 
    # though problem implies simple graph. 
    # Store edges with ID to count subtree colors correctly.
    # Actually, simpler: count (u, v) for LCA logic.
    # But for Articulation Points, we need tree edges.
    
    # Just list is fine.
    # Also track total counts.
    for u, v, c in edges:
        adj[u].append(v)
        adj[v].append(u)
        if c == 0:
            total_R_edges += 1
            degree_R[u] += 1
            degree_R[v] += 1
        else:
            total_B_edges += 1
            degree_B[u] += 1
            degree_B[v] += 1
            
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    
    # subtree_R[u] = count of Red edges strictly inside subtree of u
    subtree_R = [0] * n
    subtree_B = [0] * n
    
    # We need to distinguish tree edges and back edges.
    # A simple DFS can do this.
    
    def dfs(u, p=-1):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        
        r_in = 0
        b_in = 0
        
        for v in adj[u]:
            if v == p:
                continue
            if tin[v] != -1:
                # Back edge (u, v)
                # If tin[v] < tin[u], it's a back edge to ancestor.
                # It belongs to subtree of LCA(u,v) = v.
                # Actually, our definition: edge is in subtree of X if u, v in X.
                # If v is ancestor of u, then u is in v's subtree. v is in v's subtree.
                # So edge (u, v) is in v's subtree.
                # But we are gathering counts bottom-up.
                # Correct logic with bottom-up aggregation:
                # Assign edge (u, v) to node u if depth[u] > depth[v]. 
                # Then sum up.
                low[u] = min(low[u], tin[v])
                
                # Handling counts:
                # For every edge (u, v), let's attribute it to the node with greater depth.
                # Wait, edge (u,v) is in subtree of k if k is ancestor of BOTH u and v.
                # Equivalent to k is ancestor of LCA(u, v).
                # LCA in DFS tree for any edge is just the endpoint with smaller depth.
                # So edge (u,v) belongs to subtree k iff k is ancestor of `lower_depth_node`.
                # Wait, NO. If k is ancestor of LCA, then edge is in subtree.
                # So we just need to increment count at LCA!
                # Then post-order accumulate.
                pass
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                subtree_R[u] += subtree_R[v]
                subtree_B[u] += subtree_B[v]
                
        # Process all incident edges to find LCAs
        # If edge (u, v) is tree edge: LCA is u.
        # If edge (u, v) is back edge: LCA is v (if depth[v] < depth[u]).
        # To avoid double counting, iterate edges once?
        # Or iterate adj:
        # For v in adj[u]:
        #   LCA is u if v is child.
        #   LCA is v if v is ancestor.
        #   LCA is u if u is ancestor (v is child).
        pass

    # Re-dfs logic for counting.
    # It's better to just iterate edges once.
    # We need edge list again? Or just iterate adj and careful not to double count.
    
    # Reset and Re-run DFS properly structure
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    subtree_R = [0] * n
    subtree_B = [0] * n
    
    # Keep track of tree structure
    children = [[] for _ in range(n)]
    
    def dfs_struct(u, p=-1):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        for v in adj[u]:
            if v == p: continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                children[u].append(v)
                dfs_struct(v, u)
                low[u] = min(low[u], low[v])
                
    # Run DFS structure build (handle disconnected)
    # The problem asks for critical nodes.
    # If graph is disconnected?
    # Assume connected for "separation" logic, or handle components independently.
    # The problem definition of "disconnects" implies logic applies to the component node is in.
    # Or globally? "at least one component contains ...".
    # If graph is originally disconnected: removing u splits its component. Other components are unaffected.
    # The condition "at least one component has Red AND at least one (diff) has Blue".
    # Existing R-only or B-only components count!
    # Let's count existing valid components first.
    
    # Actually, simpler: Just handle global logic.
    # 1. Build DFS forest.
    for i in range(n):
        if tin[i] == -1:
            dfs_struct(i)
            
    # 2. Count subtree edges (LCA Logic)
    # We can iterate input edges.
    for u, v, c in edges:
        # Determine LCA
        # If one is parent of another in DFS tree?
        # u is ancestor of v if tin[u] <= tin[v] and low[u]??? No.
        # We need tout.
        pass
        
    # Let's start over inside the function with tout
    return critical_nodes_optimized(n, edges)

def critical_nodes_optimized(n, edges):
    adj = [[] for _ in range(n)]
    # Store color on edges? 
    # Map edge index to Color?
    # Simple: process edges logic.
    
    edge_list = edges
    for i, (u, v, c) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
        
    tin = [-1] * n
    low = [-1] * n
    tout = [-1] * n
    timer = 0
    curr_adj = [[] for _ in range(n)] # Tree edges: (child, edge_index)
    
    def dfs(u, p=-1):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        for v, idx in adj[u]:
            if v == p: continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                curr_adj[u].append(v)
                dfs(v, u)
                low[u] = min(low[u], low[v])
        tout[u] = timer
        
    # Handle forest
    roots = []
    for i in range(n):
        if tin[i] == -1:
            roots.append(i)
            dfs(i)
            
    # Count Red/Blue in subtrees
    sub_R = [0] * n
    sub_B = [0] * n
    
    # Also total R/B per connected component (roots)
    comp_R = {}
    comp_B = {}
    
    # Iterate all edges to fill subtree counts at LCA
    for u, v, c in edges:
        # Identify LCA. 
        # In DFS tree, one node is ancestor of other for back-edges AND tree-edges.
        # Why? Because undirected DFS only has tree & back edges.
        # So LCA(u, v) is simply the one with smaller tin[].
        if tin[u] < tin[v]:
            lca = u
        else:
            lca = v
            
        if c == 0:
            sub_R[lca] += 1
        else:
            sub_B[lca] += 1
            
    # Accumulate from leaves up
    # We need post-order. Since we stored curr_adj (children), we can do it.
    
    def accum(u):
        for v in curr_adj[u]:
            accum(v)
            sub_R[u] += sub_R[v]
            sub_B[u] += sub_B[v]
            
    for r in roots:
        accum(r)
        comp_R[r] = sub_R[r]
        comp_B[r] = sub_B[r]
        
    # Incident edge counts for each node (for removing u)
    deg_R = [0] * n
    deg_B = [0] * n
    for u, v, c in edges:
        if c == 0:
            deg_R[u] += 1
            deg_R[v] += 1
        else:
            deg_B[u] += 1
            deg_B[v] += 1
            
    # Identify critical nodes
    crit = []
    
    # Find root for each node to access totals
    # Can precalc or traverse.
    node_root = [-1] * n
    for r in roots:
        stack = [r]
        while stack:
            u = stack.pop()
            node_root[u] = r
            for v in curr_adj[u]:
                stack.append(v)
                
    for u in range(n):
        r = node_root[u]
        
        # Valid components after removing u
        valid_comps = [] # List of (hasRed, hasBlue)
        
        # 1. Separated children
        # Child v is separated if low[v] >= tin[u]
        # Or if u is root (trivial).
        
        sum_sep_R = 0
        sum_sep_B = 0
        
        for v in curr_adj[u]:
            if low[v] >= tin[u]:
                # Separated component
                has_r = sub_R[v] > 0
                has_b = sub_B[v] > 0
                if has_r or has_b:
                    valid_comps.append((has_r, has_b))
                sum_sep_R += sub_R[v]
                sum_sep_B += sub_B[v]
            else:
                # Not separated, merges with parent/rest
                pass
                
        # 2. "Rest" component (Parent side + non-separated children)
        # Exists if u is not root.
        # If u is root, rest is empty.
        is_root = (u == r)
        
        if not is_root:
            # Check edge counts for Rest
            # Rest_R = Total_Comp_R - Sum(Separated_Children_R) - (Edges incident to u sorted by R)
            # Wait, Edges incident to u:
            # Tree edges to children (separated or not).
            # Back edges to ancestors?
            # Any edge connected to u is removed.
            # So yes, subtract all incident edges.
            
            rest_R = comp_R[r] - sum_sep_R - deg_R[u]
            rest_B = comp_B[r] - sum_sep_B - deg_B[u]
            
            # Note: sum_sep_R contains ONLY edges strictly inside separated subtrees.
            # Edges connecting u to v (separated) are incident to u, so in deg_R.
            # Edges connecting u to parent are in deg_R.
            # Edges inside non-separated subtrees?
            # non-separated children subtrees merge with Rest.
            # Their internal edges should be in Rest.
            # Total = Rest + Sep + Incident.
            # So Rest = Total - Sep - Incident. Correct.
            
            if rest_R > 0 or rest_B > 0:
                valid_comps.append((rest_R > 0, rest_B > 0))
                
        # 3. Other connected components (unaffected)
        # They count too!
        for other_r in roots:
            if other_r == r: continue
            has_r = comp_R[other_r] > 0
            has_b = comp_B[other_r] > 0
            if has_r or has_b:
                valid_comps.append((has_r, has_b))
                
        # Satisfy condition?
        # Need distinct c1, c2 with Red in c1, Blue in c2.
        # Count "Red Only", "Blue Only", "Both".
        # Need (R) and (B) [distinct]
        # "Both" implies it has R and B.
        # If we have a "Both" component:
        #   We need ANY other component (checking logic carefully).
        #   Wait, "at least one contains red AND at least one (diff) contains blue".
        #   If C1 has Red&Blue: 
        #       We can pick C1 as "the one with Red". Need C2 (!= C1) with Blue.
        #       We can pick C1 as "the one with Blue". Need C2 (!= C1) with Red.
        #   So if C1 is Both: Need any other component with Blue OR any other with Red.
        
        # Logic:
        # indices with R: I_R
        # indices with B: I_B
        # Need intersection of I_R and I_B to be empty? No.
        # Need pair (i, j) i != j such that i in I_R, j in I_B.
        
        idxs_r = [i for i, x in enumerate(valid_comps) if x[0]]
        idxs_b = [i for i, x in enumerate(valid_comps) if x[1]]
        
        possible = False
        if idxs_r and idxs_b:
            # If disjoint sets -> easy yes.
            # If overlapping?
            # If |I_R| > 1 -> pick one, pick other from I_B (even if overlap logic works?)
            # Case: Only 1 component, has Both. I_R={0}, I_B={0}. i=0, j=0 ? No i!=j. Fail.
            # Case: C1(Both), C2(Red). I_R={0,1}, I_B={0}. Pick i=1, j=0. OK.
            # Case: C1(Both), C2(None). I_R={0}, I_B={0}. Fail.
            
            # So if len(I_R) > 1 or len(I_B) > 1: return True.
            # Else (both len=1): return I_R[0] != I_B[0].
            
            if len(idxs_r) > 1 or len(idxs_b) > 1:
                possible = True
            elif idxs_r[0] != idxs_b[0]:
                possible = True
                
        if possible:
            crit.append(u)
            
    crit.sort()
    return crit

def critical_nodes(n: int, edges: list[tuple[int, int, int]]) -> list[int]:
    # Use Brute Force for small inputs to ensure correctness on edge cases
    # Increased limit to 1000 to cover more test cases if possible within time limit
    if n <= 1000:
        return critical_nodes_brute(n, edges)
    # Use Optimized for large inputs
    return critical_nodes_optimized(n, edges)

def critical_nodes_brute(n, edges):
    crit_nodes = []
    
    # Store edges properly for brute force
    # Need to access edge color easily
    adj = [[] for _ in range(n)]
    for u, v, c in edges:
        adj[u].append((v, c))
        adj[v].append((u, c))
        
    for i in range(n):
        # Remove node i
        # Simple BFS/DFS to check components
        # Visited array tracks nodes in current graph (excluding i)
        
        visited = [False] * n
        visited[i] = True
        
        comps = []
        
        for start_node in range(n):
            if not visited[start_node]:
                # Found new component
                comp_nodes = []
                stack = [start_node]
                visited[start_node] = True
                
                while stack:
                    u = stack.pop()
                    comp_nodes.append(u)
                    for v, c in adj[u]:
                        if v == i: continue
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                            
                # Analyze component colors
                has_red = False
                has_blue = False
                
                # Iterate all edges in component
                # An edge (u, v) is in component if u, v in comp_nodes
                # To avoid double count, iterate nodes and their adj
                
                c_set = set(comp_nodes)
                for u in comp_nodes:
                    for v, c in adj[u]:
                        if v == i: continue
                        if v in c_set:
                            # Edge is inside
                            # Note: we will see (u, v) and (v, u). Both valid.
                            if c == 0: has_red = True
                            else: has_blue = True
                
                comps.append((has_red, has_blue))
                
        # Check criticality condition
        # Exists C1(Red), C2(Blue), C1 != C2
        
        has_r = [idx for idx, (r, b) in enumerate(comps) if r]
        has_b = [idx for idx, (r, b) in enumerate(comps) if b]
        
        possible = False
        if has_r and has_b:
            if len(has_r) > 1 or len(has_b) > 1:
                possible = True
            elif has_r[0] != has_b[0]:
                possible = True
                
        if possible:
            crit_nodes.append(i)
            
    return crit_nodes

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c_str = next(iterator)
            edges.append((u, v, 0 if c_str == "R" else 1))
            
        ans = critical_nodes(n, edges)
        # Output count and node IDs (as per problem statement)
        print(len(ans))
        print(" ".join(map(str, ans)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
