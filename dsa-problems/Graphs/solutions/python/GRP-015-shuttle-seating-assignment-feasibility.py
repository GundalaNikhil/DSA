import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List, Tuple

def check_feasibility(n: int, edges: List[Tuple[int, int]]) -> Tuple[int, ...]:
    indegree = [0] * n
    adj = [[] for _ in range(n)]
    
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    
    # Sorting adj for deterministic behavior not strictly needed for topological check 
    # but good for consistent processing
    for neighbors in adj:
        neighbors.sort()

    initial_zeros = 0
    for i in range(n):
        if indegree[i] == 0:
            initial_zeros += 1
            
    queue = deque([i for i in range(n) if indegree[i] == 0])
    processed = 0
    
    while queue:
        u = queue.popleft()
        processed += 1
        
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    if processed == n:
        return (1, initial_zeros)
    else:
        return (-1,)

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
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        result = check_feasibility(n, edges)
        
        if len(result) == 1:
            print(result[0])
        else:
            print(f"{result[0]} {result[1]}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
