import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List

def can_color_bipartite(n: int, adj: List[List[int]], locked: List[int]) -> bool:
    """
    Check if graph can be 2-colored respecting locked nodes.
    
    Args:
        n: Number of nodes
        adj: Adjacency list
        locked: Locked colors (0=unlocked, 1=group A, 2=group B)
    
    Returns:
        True if valid bipartite coloring exists
    """
    color = [-1] * n
    
    # Pre-color locked nodes
    for i in range(n):
        if locked[i] != 0:
            color[i] = locked[i]
    
    def bfs(start):
        queue = deque([start])
        if color[start] == -1:
            color[start] = 1 if locked[start] == 0 else locked[start]
        
        while queue:
            node = queue.popleft()
            required_neighbor_color = 3 - color[node]  # Toggle between 1 and 2
            
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    # Check if locked to wrong color
                    if locked[neighbor] != 0 and locked[neighbor] != required_neighbor_color:
                        return False
                    color[neighbor] = required_neighbor_color
                    queue.append(neighbor)
                elif color[neighbor] != required_neighbor_color:
                    return False  # Color conflict
        
        return True
    
    # Check each component
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                return False
    
    return True

def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    try:
        locked = list(map(int, input().split()))
    except EOFError:
        # Default to no locked nodes if input is missing
        locked = [0] * n
    
    result = can_color_bipartite(n, adj, locked)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
