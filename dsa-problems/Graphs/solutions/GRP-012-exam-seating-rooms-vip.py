import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
            return True
        return False

def max_component_size(n: int, edges: list[tuple[int, int]], vips: set[int]) -> int:
    dsu = DSU(n)
    
    # 1. Union Non-VIP to Non-VIP
    for u, v in edges:
        if u not in vips and v not in vips:
            dsu.union(u, v)
            
    max_comp = 0
    # 2. Check purely neutral components
    for i in range(n):
        if i not in vips and dsu.parent[i] == i:
            max_comp = max(max_comp, dsu.size[i])
            
    if not vips:
        return max_comp
        
    # 3. Check VIP augmented components
    vip_neighbors = {v: set() for v in vips}
    
    for u, v in edges:
        u_vip = u in vips
        v_vip = v in vips
        
        if u_vip and not v_vip:
            vip_neighbors[u].add(dsu.find(v))
        elif not u_vip and v_vip:
            vip_neighbors[v].add(dsu.find(u))
            
    for vip in vips:
        current_size = 1
        for root in vip_neighbors[vip]:
            current_size += dsu.size[root]
        max_comp = max(max_comp, current_size)
        
    return max_comp

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
            
        vips = set()
        # Remaining tokens are VIPs
        for token in iterator:
            vips.add(int(token))
            
        print(max_component_size(n, edges, vips))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
