import sys

sys.setrecursionlimit(200000)

def critical_nodes(n: int, edges: list[tuple[int, int, int]]) -> int:
    """
    Find critical nodes where removal separates red and blue edges into different components.
    
    A node u is critical if removing it results in:
    - At least one component with only red edges
    - At least one component with only blue edges
    """
    if not edges:
        return 0
    
    adj = [[] for _ in range(n)]
    for u, v, c in edges:
        adj[u].append((v, c))
        adj[v].append((u, c))
    
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    timer = [0]
    critical = set()
    
    def dfs(u):
        children = 0
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        
        for v, color in adj[u]:
            if disc[v] == -1:  # Tree edge
                parent[v] = u
                children += 1
                dfs(v)
                low[u] = min(low[u], low[v])
                
                # Check if u is an articulation point for this subtree
                if (parent[u] == -1 and children > 1) or (parent[u] != -1 and low[v] >= disc[u]):
                    # u is an articulation point
                    # Now check if removing u separates red and blue edges
                    
                    # Check what colors exist in v's subtree (doesn't go through u)
                    subtree_has_red, subtree_has_blue = check_subtree_colors(v, u, adj, disc)
                    
                    # Check what colors exist outside v's subtree (rest of graph)
                    rest_has_red, rest_has_blue = check_rest_colors(u, v, adj, edges, disc)
                    
                    # u is critical if one part has only red and another has only blue
                    if (subtree_has_red and not subtree_has_blue and rest_has_blue and not rest_has_red) or \
                       (subtree_has_blue and not subtree_has_red and rest_has_red and not rest_has_blue):
                        critical.add(u)
            
            elif v != parent[u]:  # Back edge
                low[u] = min(low[u], disc[v])
    
    def check_subtree_colors(root, avoid, adj, disc):
        """Check what colors exist in subtree rooted at root, avoiding node avoid"""
        has_red = has_blue = False
        visited = set()
        
        def dfs_check(u):
            nonlocal has_red, has_blue
            visited.add(u)
            for v, color in adj[u]:
                if v == avoid or disc[v] < disc[root]:
                    continue
                if color == 0:
                    has_red = True
                else:
                    has_blue = True
                if v not in visited:
                    dfs_check(v)
        
        dfs_check(root)
        return has_red, has_blue
    
    def check_rest_colors(u, subtree_root, adj, edges, disc):
        """Check colors in rest of graph (not in subtree_root's subtree)"""
        has_red = has_blue = False
        for edge_u, edge_v, color in edges:
            # Skip edges in the subtree
            if (disc[edge_u] >= disc[subtree_root] and disc[edge_v] >= disc[subtree_root]):
                continue
            # Skip edges connected to u
            if edge_u == u or edge_v == u:
                continue
            
            if color == 0:
                has_red = True
            else:
                has_blue = True
        
        return has_red, has_blue
    
    # Find all connected components and run DFS
    for i in range(n):
        if disc[i] == -1:
            dfs(i)
    
    return len(critical)

def main():
    input = sys.stdin.read
    data = input().split()
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
        print(ans)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
