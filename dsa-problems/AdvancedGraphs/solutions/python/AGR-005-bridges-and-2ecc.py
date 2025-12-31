import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def bridges_and_components(n: int, edges: list[tuple[int, int]]):
    m = len(edges)
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
        
    tin = [-1] * n
    low = [-1] * n
    bridge_flags = [0] * m
    timer = 0
    
    def dfs_bridges(u, p_edge_idx):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        
        for v, idx in adj[u]:
            if idx == p_edge_idx:
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs_bridges(v, idx)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridge_flags[idx] = 1
                    
    for i in range(n):
        if tin[i] == -1:
            dfs_bridges(i, -1)
            
    # Find components
    comp = [0] * n
    comp_count = 0
    visited = [False] * n
    
    def dfs_comp(u, c):
        visited[u] = True
        comp[u] = c
        for v, idx in adj[u]:
            if bridge_flags[idx]:
                continue
            if not visited[v]:
                dfs_comp(v, c)
                
    for i in range(n):
        if not visited[i]:
            comp_count += 1
            dfs_comp(i, comp_count)
            
    return bridge_flags, comp

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
            edges.append((u, v))
            
        bridge_flags, comp = bridges_and_components(n, edges)
        
        out = [str(sum(bridge_flags))]
        for i, f in enumerate(bridge_flags):
            if f:
                out.append(f"{edges[i][0]} {edges[i][1]}")
        out.append(" ".join(map(str, comp)))
        sys.stdout.write("\n".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
