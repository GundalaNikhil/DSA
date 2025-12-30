import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def critical_edges(n: int, edges: list[tuple[int, int, int]], T: int) -> list[tuple[int, int]]:
    adj = [[] for _ in range(n)]
    for i, (u, v, c) in enumerate(edges):
        adj[u].append((v, c, i))
        adj[v].append((u, c, i))
        
    disc = [-1] * n
    low = [-1] * n
    timer = 0
    critical_indices = []
    
    def dfs(u, parent_edge_idx):
        nonlocal timer
        timer += 1
        disc[u] = low[u] = timer
        
        for v, cap, idx in adj[u]:
            if idx == parent_edge_idx:
                continue
            
            if disc[v] != -1:
                low[u] = min(low[u], disc[v])
            else:
                dfs(v, idx)
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    if cap < T:
                        critical_indices.append(idx)
                        
    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
            
    critical_indices.sort()
    return [(edges[i][0], edges[i][1]) for i in critical_indices]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
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
        out += [f"{u} {v}" for (u, v) in ans]
        print("\n".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
