import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            return True
        return False

def min_cost(n: int, heights: list, existing_cables: list) -> int:
    dsu = DSU(n)
    
    # Union existing cables
    for u, v in existing_cables:
        dsu.union(u, v)
        
    # Create sorted list of (height, original_index)
    buildings = []
    for i in range(n):
        buildings.append((heights[i], i))
    
    buildings.sort()
    
    # Generate edges between adjacent sorted buildings
    edges = []
    for i in range(n - 1):
        h1, idx1 = buildings[i]
        h2, idx2 = buildings[i+1]
        cost = h2 - h1
        edges.append((cost, idx1, idx2))
        
    edges.sort()
    
    total_cost = 0
    for cost, u, v in edges:
        if dsu.union(u, v):
            total_cost += cost
            
    return total_cost

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    
    heights = []
    for _ in range(n):
        heights.append(int(next(iterator)))
        
    m = int(next(iterator))
    existing_cables = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        existing_cables.append([u, v])
        
    print(min_cost(n, heights, existing_cables))

if __name__ == "__main__":
    main()
