import sys
import heapq

def dijkstra(n: int, adj: list[list[tuple[int, int]]], s: int) -> list[int]:
    dist = [-1] * n
    dist[s] = 0
    
    # Min-heap stores (distance, node)
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Lazy deletion check
        if dist[u] != -1 and d > dist[u]:
            continue
        
        for v, w in adj[u]:
            if dist[v] == -1 or dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        dist = dijkstra(n, adj, s)
        print(" ".join(map(str, dist)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
