import heapq
import sys
sys.setrecursionlimit(200000)

def shortest_path_with_battery(n: int, edges: list[tuple[int, int, int]], 
                                source: int, dest: int, battery: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    dist = [float('inf')] * n
    dist[source] = 0
    
    pq = [(0, source)] # (cost, u)
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        if u == dest:
            return d
            
        for v, w in adj[u]:
            if w <= battery: # Constraint Check
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
                    
    return -1 if dist[dest] == float('inf') else dist[dest]

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
            
        source = int(next(iterator))
        dest = int(next(iterator))
        battery = int(next(iterator))
        
        print(shortest_path_with_battery(n, edges, source, dest, battery))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
