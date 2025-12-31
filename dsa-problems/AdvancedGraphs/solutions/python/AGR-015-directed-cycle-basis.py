import sys
from collections import deque

def cycle_basis(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    m = len(edges)
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        
    # Calc basis size
    undir_adj = [[] for _ in range(n)]
    for u, v in edges:
        undir_adj[u].append(v)
        undir_adj[v].append(u)
        
    visited = [False] * n
    c = 0
    for i in range(n):
        if not visited[i]:
            c += 1
            q = [i]
            visited[i] = True
            while q:
                u = q.pop()
                for v in undir_adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
    
    D = m - n + c
    
    basis = [None] * m
    result = []
    
    def get_path(start, target):
        if start == target: return []
        parent = [-1] * n
        parent_edge = [-1] * n
        q = deque([start])
        parent[start] = start
        
        while q:
            u = q.popleft()
            if u == target: break
            for v, idx in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    parent_edge[v] = idx
                    q.append(v)
        
        if parent[target] == -1: return None
        
        path = []
        curr = target
        while curr != start:
            path.append(parent_edge[curr])
            curr = parent[curr]
        return path[::-1]

    for i in range(m):
        if len(result) == D: break
        
        u, v = edges[i]
        path = get_path(v, u)
        if path is None: continue
        
        # Vector
        vec = 0
        vec |= (1 << i)
        for idx in path:
            vec |= (1 << idx)
            
        # Insert
        temp_vec = vec
        inserted = False
        # Find pivot
        # We iterate bits from low to high or high to low?
        # Use low to high (0 to m-1)
        for bit in range(m):
            if (temp_vec >> bit) & 1:
                if basis[bit] is None:
                    basis[bit] = temp_vec
                    inserted = True
                    break
                else:
                    temp_vec ^= basis[bit]
        
        if inserted:
            cycle = [u, v]
            curr = v
            for idx in path:
                # Edge idx is x->y. curr is x.
                # We need y.
                next_node = edges[idx][1]
                cycle.append(next_node)
                curr = next_node
            result.append(cycle)
            
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
            edges.append((u, v))
            
        cycles = cycle_basis(n, edges)
        out = [str(len(cycles))]
        for cyc in cycles:
            out.append(str(len(cyc)) + " " + " ".join(map(str, cyc)))
        sys.stdout.write("\n".join(out).strip())
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
