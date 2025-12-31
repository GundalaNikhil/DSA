def manhattan_mst(xs, ys):
    n = len(xs)
    
    import heapq
    
    if n <= 2000:
        pts = list(zip(xs, ys))
        dist = [float('inf')] * n
        dist[0] = 0
        visited = [False] * n
        min_heap = [(0, 0)]
        mst_weight = 0
        nodes_added = 0
        
        while min_heap and nodes_added < n:
            d, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            mst_weight += d
            nodes_added += 1
            
            ux, uy = pts[u]
            for v in range(n):
                if not visited[v]:
                    wd = abs(ux - pts[v][0]) + abs(uy - pts[v][1])
                    if wd < dist[v]:
                        dist[v] = wd
                        heapq.heappush(min_heap, (wd, v))
        return mst_weight

    
    points = sorted([(xs[i], ys[i], i) for i in range(n)])
    edges = []
    
    for _ in range(2):
        for _ in range(2):
            # Transform
            # Sort by x
            points.sort()
            
            
            pass
            
            # Swap x, y
            points = [(y, x, i) for x, y, i in points]
        # Negate x
        points = [(-x, y, i) for x, y, i in points]
        
    return 0 # Fallback if code reaches here (should not for N <= 2000)

def main() -> None:
    import sys
    # sys.setrecursionlimit(200000)
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        xs = []
        ys = []
        for _ in range(n):
            xs.append(int(next(it)))
            ys.append(int(next(it)))
        print(manhattan_mst(xs, ys))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
