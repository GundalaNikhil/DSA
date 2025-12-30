from collections import deque
from typing import List

def is_feasible(n: int, edges: List[List[int]]) -> bool:
    indegree = [0] * n
    adj = [[] for _ in range(n)]
    
    # Build graph
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    
    # Initialize queue with indegree 0 nodes
    queue = deque([i for i in range(n) if indegree[i] == 0])
    processed = 0
    
    while queue:
        u = queue.popleft()
        processed += 1
        
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return processed == n


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
