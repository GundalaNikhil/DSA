import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List

def count_reachable(n: int, edges: List[tuple], threshold: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        if w <= threshold:
            adj[u].append(v)
            adj[v].append(u)
            
    visited = set()
    queue = deque([0])
    visited.add(0)
    
    while queue:
        node = queue.popleft()
        # Sort for deterministic
        adj[node].sort() 
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return len(visited)

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
        threshold = int(next(iterator))
        m = int(next(iterator))
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
            
        result = count_reachable(n, edges, threshold)
        print(result)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
