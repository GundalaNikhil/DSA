import sys
from collections import deque

def bipartite_colors(n: int, adj: list[list[int]]):
    colors = [-1] * n
    
    for i in range(n):
        if colors[i] == -1:
            queue = deque([i])
            colors[i] = 0
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        return None
                        
    return colors

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
            
        colors = bipartite_colors(n, adj)
        if colors is None:
            print("0")
        else:
            print("1")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
