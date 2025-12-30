import sys
import heapq

def mst_prim(n: int, adj: list[list[tuple[int, int]]]) -> int:
    mst_weight = 0
    visited = [False] * n
    pq = [(0, 0)] # (weight, node)
    nodes_count = 0
    
    while pq:
        w, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
            
        visited[u] = True
        mst_weight += w
        nodes_count += 1
        
        if nodes_count == n:
            break
            
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))
                
    return mst_weight

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
            w = int(next(iterator))
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        print(mst_prim(n, adj))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
