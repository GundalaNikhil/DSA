import heapq
from typing import List

def dijkstra(n: int, adj: List[List[tuple]], source: int) -> List[int]:
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]  # (distance, node)
    
    while pq:
        d, node = heapq.heappop(pq)
        
        if d > dist[node]:
            continue
        
        for neighbor, weight in adj[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return dist


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
