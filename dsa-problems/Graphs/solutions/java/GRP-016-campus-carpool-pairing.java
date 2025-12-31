import java.util.*;

class UnionFind {
    private int[] parent;
    private int[] rank;
    
    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    public boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX == rootY) {
            return false;  // Already in same set (would create cycle)
        }
        
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        
        return true;
    }
}

class Solution {
    public boolean isForestAfterAdding(int n, int[][] existingEdges, int[] newEdge) {
        UnionFind uf = new UnionFind(n);
        
        // Build current graph
        for (int[] edge : existingEdges) {
            if (!uf.union(edge[0], edge[1])) {
                return false;  // Already has cycle
            }
        }
        
        // Check new edge
        return uf.find(newEdge[0]) != uf.find(newEdge[1]);
    }
}
