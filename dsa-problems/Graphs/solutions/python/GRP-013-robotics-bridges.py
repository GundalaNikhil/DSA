import sys
sys.setrecursionlimit(200000)
from typing import List

def find_bridges(n: int, adj: List[List[int]]) -> List[tuple]:
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    bridges = []
    time = [0]
    
    def dfs(u):
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in adj[u]:
            if disc[v] == -1:
                parent[v] = u
                dfs(v)
                
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    bridges.append((u, v))
            
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if disc[i] == -1:
            dfs(i)
    
    return bridges


def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    bridges = find_bridges(n, adj)
    bridges.sort()
    
    print(len(bridges))
    for u, v in bridges:
        print(f"{u} {v}")

if __name__ == "__main__":
    main()
