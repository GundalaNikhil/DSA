import sys
sys.setrecursionlimit(200000)
from typing import List

def has_cycle(n: int, adj: List[List[int]]) -> bool:
    visited = [False] * n
    
    def dfs(node, parent):
        visited[node] = True
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # Cycle detected
        
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    
    return False


def main():
    n = int(input())
    m = int(input())

    adj = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    result = has_cycle(n, adj)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
