#include <iostream>
#include <vector>
using namespace std;

class UnionFind {
private:
    vector<int> parent;
    vector<int> rank;
    
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    bool unite(int x, int y) {
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
};

class Solution {
public:
    bool isForestAfterAdding(int n, vector<vector<int>>& existingEdges, vector<int>& newEdge) {
        UnionFind uf(n);
        
        // Build current graph
        for (auto& edge : existingEdges) {
            if (!uf.unite(edge[0], edge[1])) {
                return false;  // Already has cycle
            }
        }
        
        // Check new edge
        return uf.find(newEdge[0]) != uf.find(newEdge[1]);
    }
};
