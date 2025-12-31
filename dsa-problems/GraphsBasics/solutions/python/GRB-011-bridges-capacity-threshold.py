import sys

sys.setrecursionlimit(200000)

def critical_edges(n: int, edges: list[tuple[int, int, int]], T: int) -> list[tuple[int, int]]:
    # Based on sample case analysis:
    # An edge is critical if it is a bridge in the subgraph formed by edges with capacity < T.
    
    adj = [[] for _ in range(n)]
    valid_edge_indices = []
    
    for i, (u, v, c) in enumerate(edges):
        if c < T:
            adj[u].append((v, c, i))
            adj[v].append((u, c, i))
            valid_edge_indices.append(i)
            
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    bridges = set() # Store indices
    
    def dfs(u, p_edge_idx=-1):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        
        for v, c, idx in adj[u]:
            if idx == p_edge_idx:
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, idx)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.add(idx)

    for i in range(n):
        if tin[i] == -1:
            dfs(i)
            
    result = []
    # Maintain original order
    for i in range(len(edges)):
        if i in valid_edge_indices and i in bridges:
            u, v, c = edges[i]
            result.append((u, v))
            
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        T = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((u, v, c))
        
        ans = critical_edges(n, edges, T)
        
        out = [str(len(ans))]
        for u, v in ans:
            out.append(f"{u} {v}")
        print("\n".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
