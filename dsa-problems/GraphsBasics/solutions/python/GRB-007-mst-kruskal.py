import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def mst_kruskal(n: int, edges: list[tuple[int, int, int]]) -> int:
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    dsu = DSU(n)
    mst_weight = 0
    edges_count = 0
    
    for u, v, w in edges:
        if dsu.union(u, v):
            mst_weight += w
            edges_count += 1
            if edges_count == n - 1:
                break
                
    return mst_weight

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
            
        print(mst_kruskal(n, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
