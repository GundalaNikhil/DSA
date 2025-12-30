import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List

def count_components(n: int, adj: List[List[int]]) -> int:
    """
    Count connected components using BFS.
    
    Args:
        n: Number of nodes
        adj: Adjacency list
    
    Returns:
        Number of connected components
    """
    visited = [False] * n
    components = 0
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    for i in range(n):
        if not visited[i]:
            components += 1
            bfs(i)
    
    return components

def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    result = count_components(n, adj)
    print(result)

if __name__ == "__main__":
    main()
