import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def shortest_path_dag(n: int, adj: list[list[tuple[int, int]]], s: int) -> list[int]:
    visited = [False] * n
    stack = []
    
    def dfs(u):
        visited[u] = True
        for v, w in adj[u]:
            if not visited[v]:
                dfs(v)
        stack.append(u)
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            
    # Stack has reverse topological order (sink first)
    # We pop from stack to get topological order
    
    dist = [float('inf')] * n
    dist[s] = 0
    
    while stack:
        u = stack.pop()
        
        if dist[u] != float('inf'):
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
    return [d if d != float('inf') else -1 for d in dist]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        dist = shortest_path_dag(n, adj, s)
        print(" ".join(map(str, dist)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
