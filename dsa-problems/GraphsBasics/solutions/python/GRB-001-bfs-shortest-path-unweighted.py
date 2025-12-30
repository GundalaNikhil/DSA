import sys
from collections import deque

def shortest_path(n: int, edges: list, s: int) -> list:
    # 1. Build Adjacency List
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # 2. Initialize Distance Array
    dist = [-1] * n
    
    # 3. BFS
    queue = deque([s])
    dist[s] = 0
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
                
    return dist

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
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])
            
        result = shortest_path(n, edges, s)
        print(' '.join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
