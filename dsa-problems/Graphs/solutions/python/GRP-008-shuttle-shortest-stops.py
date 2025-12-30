import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List

def shortest_distances(n: int, adj: List[List[int]], source: int) -> List[int]:
    dist = [-1] * n
    dist[source] = 0
    queue = deque([source])
    
    while queue:
        node = queue.popleft()
        # Sort neighbors for deterministic traversal
        adj[node].sort()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    return dist

def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
            
        try:
            source = int(next(iterator))
        except StopIteration:
            source = 0
            
        result = shortest_distances(n, adj, source)
        print(' '.join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
