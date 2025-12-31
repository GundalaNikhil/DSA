import sys

def bellman_ford(n: int, s: int, edges: list[tuple[int, int, int]]):
    INF = float('inf')
    dist = [INF] * n
    dist[s] = 0
    
    # Relax edges N-1 times
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
            
    # Check for negative cycle
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None # Negative cycle detected
            
    # Convert INF to -1
    return [-1 if d == INF else d for d in dist]

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
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
            
        dist = bellman_ford(n, s, edges)
        if dist is None:
            print("NEGATIVE CYCLE")
        else:
            print(" ".join(map(str, dist)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
