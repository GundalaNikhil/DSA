import sys
sys.setrecursionlimit(200000)
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False

def is_forest(n: int, edges: List[tuple]) -> bool:
    if not edges:
        return True
        
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return False # Cycle detected
    return True

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
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        result = is_forest(n, edges)
        print("true" if result else "false")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
