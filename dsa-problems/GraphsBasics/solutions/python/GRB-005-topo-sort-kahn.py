import sys
from collections import deque

def topo_sort(n: int, adj: list[list[int]]) -> list[int]:
    indegree = [0] * n
    for u in range(n):
        for v in adj[u]:
            indegree[v] += 1
            
    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
                
    return result

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
            
        order = topo_sort(n, adj)
        print(" ".join(map(str, order)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
