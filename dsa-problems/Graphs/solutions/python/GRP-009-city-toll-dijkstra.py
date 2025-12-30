import sys
sys.setrecursionlimit(200000)
import heapq
from typing import List

def dijkstra(n: int, adj: List[List[tuple]], source: int) -> List[int]:
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        d, node = heapq.heappop(pq)
        
        if d > dist[node]:
            continue
        
        # Sort neighbors by weight then index for deterministic behavior if equal weights
        adj[node].sort(key=lambda x: (x[1], x[0]))
        
        for neighbor, weight in adj[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    # Format infinity as -1 or keep large? Problem implies reachable. 
    # Usually standard is -1 or INF. Let's keep int, maybe replace inf with -1 if required.
    # Based on failures, let's output raw integers, assuming connectivity or large val.
    return [d if d != float('inf') else -1 for d in dist]

def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        try:
            source = int(next(iterator))
        except StopIteration:
            source = 0
            
        result = dijkstra(n, adj, source)
        print(' '.join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
