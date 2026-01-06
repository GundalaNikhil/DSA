from typing import List


class Edge:
    def __init__(self, u: int, v: int, w: int, p: int):
        self.u = u
        self.v = v
        self.w = w
        self.p = p


class DSU:
    """Standard Union-Find data structure"""
    
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, i):
        """Find with path compression"""
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        """Union by rank"""
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            return False
        
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        
        return True


class Solution:
    def minSpanningTreeCostWithPenalties(self, n: int, m: int, edges: List[Edge]) -> int:
        """
        Build MST using only base weights, then add penalties.
        
        Algorithm:
        1. Sort edges by (weight, penalty) - penalty for tie-breaking
        2. Run Kruskal's algorithm using DSU
        3. Sum up (weight + penalty) for selected edges
        4. Return total or -1 if graph is disconnected
        """
        # Sort edges by (weight, penalty)
        # Among same weight, prefer lower penalty for deterministic answer
        sorted_edges = sorted(edges, key=lambda e: (e.w, e.p))
        
        dsu = DSU(n)
        total_cost = 0
        edges_used = 0
        
        for edge in sorted_edges:
            if dsu.union(edge.u, edge.v):
                # Edge is added to MST
                total_cost += edge.w + edge.p
                edges_used += 1
                
                # Early termination when MST is complete
                if edges_used == n - 1:
                    break
        
        # Check if we have a spanning tree
        if edges_used == n - 1:
            return total_cost
        else:
            return -1
