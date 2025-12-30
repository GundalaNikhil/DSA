import sys
import heapq

def all_pairs_shortest_paths(n: int, edges: list[tuple[int, int, int]]) -> list[list[int]]:
    INF = 10**18
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        
    # 1. Bellman-Ford for potentials h
    # Virtual source n connected to 0..n-1 with weight 0
    h = [INF] * (n + 1)
    h[n] = 0
    
    # We run n iterations (since V=n+1)
    # Edges: original + (n->i w=0)
    # Optimization: first iteration sets h[0..n-1] = 0.
    # So we can just init h[0..n-1] = 0 and run Bellman-Ford on original graph for n-1 times?
    # Yes, because dist(n, u) <= 0.
    # But we must ensure h[u] is correct shortest path from virtual source.
    # If there are negative edges, h[u] can decrease below 0.
    
    h = [0] * (n + 1) # h[n]=0, others 0 initially (since n->i w=0)
    
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if h[u] + w < h[v]:
                h[v] = h[u] + w
                changed = True
        if not changed:
            break
            
    # 2. Dijkstra from each node
    result = [[INF] * n for _ in range(n)]
    
    for s in range(n):
        d = [INF] * n
        d[s] = 0
        pq = [(0, s)]
        
        while pq:
            dist_u, u = heapq.heappop(pq)
            if dist_u > d[u]: continue
            
            for v, w in adj[u]:
                new_w = w + h[u] - h[v]
                if d[u] + new_w < d[v]:
                    d[v] = d[u] + new_w
                    heapq.heappush(pq, (d[v], v))
                    
        for v in range(n):
            if d[v] != INF:
                result[s][v] = d[v] - h[s] + h[v]
                
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
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
            
        dist = all_pairs_shortest_paths(n, edges)
        INF = 10**18
        out = []
        for i in range(n):
            row = []
            for x in dist[i]:
                if x >= INF // 2:
                    row.append("INF")
                else:
                    row.append(str(x))
            out.append(" ".join(row))
        print("\n".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
