class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = Array(n).fill(0);
  }
  
  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }
  
  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);
    
    if (rootX === rootY) {
      return false;  // Already in same set (would create cycle)
    }
    
    if (this.rank[rootX] < this.rank[rootY]) {
      this.parent[rootX] = rootY;
    } else if (this.rank[rootX] > this.rank[rootY]) {
      this.parent[rootY] = rootX;
    } else {
      this.parent[rootY] = rootX;
      this.rank[rootX]++;
    }
    
    return true;
  }
}

class Solution {
  isForestAfterAdding(n, existingEdges, newEdge) {
    const uf = new UnionFind(n);
    
    // Build current graph
    for (const [u, v] of existingEdges) {
      if (!uf.union(u, v)) {
        return false;  // Already has cycle
      }
    }
    
    // Check new edge
    return uf.find(newEdge[0]) !== uf.find(newEdge[1]);
  }
}
