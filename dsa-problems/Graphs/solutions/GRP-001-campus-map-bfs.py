from collections import deque
from typing import List

def bfs_traversal(n: int, adj: List[List[int]]) -> List[int]:
    """
    Perform BFS traversal starting from node 0.
    
    Args:
        n: Number of nodes in the graph
        adj: Adjacency list representation of the graph
    
    Returns:
        List of nodes in BFS visitation order
    """
    result = []
    visited = [False] * n
    queue = deque()
    
    # Start BFS from node 0
    queue.append(0)
    visited[0] = True
    
    while queue:
        curr = queue.popleft()
        result.append(curr)
        
        # Visit all unvisited neighbors
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    result = bfs_traversal(n, adj)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
