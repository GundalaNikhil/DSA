const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
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
    if (rootX !== rootY) {
      this.parent[rootX] = rootY;
      return true;
    }
    return false;
  }
}

class Solution {
  minCost(n, heights, existingCables) {
    const dsu = new DSU(n);
    
    for (const [u, v] of existingCables) {
      dsu.union(u, v);
    }
    
    const buildings = heights.map((h, i) => ({ h, i }));
    buildings.sort((a, b) => a.h - b.h);
    
    const edges = [];
    for (let i = 0; i < n - 1; i++) {
      const u = buildings[i].i;
      const v = buildings[i + 1].i;
      const cost = buildings[i + 1].h - buildings[i].h;
      edges.push({ u, v, cost });
    }
    
    edges.sort((a, b) => a.cost - b.cost);
    
    let totalCost = 0;
    for (const { u, v, cost } of edges) {
      if (dsu.union(u, v)) {
        totalCost += cost;
      }
    }
    
    return totalCost;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const heights = data[ptr++].split(" ").map(Number);
  const m = parseInt(data[ptr++]);
  
  const existingCables = [];
  for (let i = 0; i < m; i++) {
    const [u, v] = data[ptr++].split(" ").map(Number);
    existingCables.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.minCost(n, heights, existingCables));
});
