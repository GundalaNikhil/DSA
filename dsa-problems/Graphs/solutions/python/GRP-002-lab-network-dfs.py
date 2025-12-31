import sys
sys.setrecursionlimit(200000)
from typing import List

def dfs_traversal(n: int, adj: List[List[int]]) -> List[int]:
    """
    Perform DFS traversal starting from node 0.
    
    Args:
        n: Number of nodes
        adj: Adjacency list representation
    
    Returns:
        List of nodes in preorder DFS visitation order
    """
    result = []

    # Sort neighbors for deterministic traversal
    for neighbors in adj:
        neighbors.sort()

    visited = [False] * n
    
    def dfs(node):
        # Mark as visited and add to result (preorder)
        visited[node] = True
        result.append(node)
        
        # Recursively visit all unvisited neighbors
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    # Start DFS from node 0
    dfs(0)
    
    return result

def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    result = dfs_traversal(n, adj)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
