import sys
import heapq

def k_shortest_paths(n: int, adj: list[list[tuple[int, int]]], s: int, t: int, k: int) -> list[int]:
    
    def get_shortest_path(start_node, end_node, forbidden_nodes, forbidden_edges):
        dist = {i: float('inf') for i in range(n)}
        parent = {i: -1 for i in range(n)}
        dist[start_node] = 0
        pq = [(0, start_node)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]: continue
            if u == end_node: break
            
            for v, w in adj[u]:
                if v in forbidden_nodes: continue
                if (u, v) in forbidden_edges: continue
                
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
                    
        if dist[end_node] == float('inf'):
            return None, float('inf')
            
        path = []
        curr = end_node
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        return path[::-1], dist[end_node]

    A = [] # List of (cost, path)
    B = [] # Heap of (cost, path)
    
    # 1. First shortest path
    path0, cost0 = get_shortest_path(s, t, set(), set())
    if not path0:
        return []
    A.append((cost0, path0))
    
    # 2. Find k-1 more
    for k_idx in range(1, k):
        prev_path = A[-1][1]
        
        for i in range(len(prev_path) - 1):
            spur_node = prev_path[i]
            root_path = prev_path[:i+1]
            
            # Calculate root path cost
            root_cost = 0
            for j in range(i):
                u, v = root_path[j], root_path[j+1]
                for neighbor, weight in adj[u]:
                    if neighbor == v:
                        root_cost += weight
                        break
            
            forbidden_nodes = set(root_path)
            forbidden_nodes.remove(spur_node)
            
            forbidden_edges = set()
            for cost, path in A:
                if len(path) > i and path[:i+1] == root_path:
                    forbidden_edges.add((path[i], path[i+1]))
            
            spur_path, spur_cost = get_shortest_path(spur_node, t, forbidden_nodes, forbidden_edges)
            
            if spur_path:
                total_path = root_path[:-1] + spur_path
                total_cost = root_cost + spur_cost
                
                # Check duplicates (inefficient but simple for small K)
                is_duplicate = False
                for cost, path in B:
                    if path == total_path:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    heapq.heappush(B, (total_cost, total_path))
                    
        if not B:
            break
            
        # Extract best from B
        # Note: B can contain duplicates if we pushed same path from different spur nodes
        # We handled check before push, but let's be safe.
        
        while B:
            cost, path = heapq.heappop(B)
            # Check if already in A
            in_A = False
            for ac, ap in A:
                if ap == path:
                    in_A = True
                    break
            if not in_A:
                A.append((cost, path))
                break
        
        if len(A) <= k_idx: # Could not find new path
            break
            
    return [cost for cost, path in A]

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
        t = int(next(iterator))
        k = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        paths = k_shortest_paths(n, adj, s, t, k)
        print(len(paths))
        print(" ".join(map(str, paths)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
