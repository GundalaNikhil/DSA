const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.size = Array(n).fill(1);
  }
  
  find(i) {
    if (this.parent[i] !== i) {
      this.parent[i] = this.find(this.parent[i]);
    }
    return this.parent[i];
  }
  
  union(i, j) {
    const rootI = this.find(i);
    const rootJ = this.find(j);
    if (rootI !== rootJ) {
      this.parent[rootI] = rootJ;
      this.size[rootJ] += this.size[rootI];
    }
  }
}

class Solution {
  maxComponentSize(n, edges, vips) {
    const dsu = new DSU(n);
    const vipSet = new Set(vips);
    
    // 1. Union Non-VIP to Non-VIP
    for (const [u, v] of edges) {
      if (!vipSet.has(u) && !vipSet.has(v)) {
        dsu.union(u, v);
      }
    }
    
    let maxComp = 0;
    // 2. Purely neutral
    for (let i = 0; i < n; i++) {
      if (!vipSet.has(i) && dsu.parent[i] === i) {
        maxComp = Math.max(maxComp, dsu.size[i]);
      }
    }
    
    if (vipSet.size === 0) return maxComp;
    
    // 3. VIP augmented
    const vipNeighbors = new Map();
    for (const vip of vips) vipNeighbors.set(vip, new Set());
    
    for (const [u, v] of edges) {
      const uVip = vipSet.has(u);
      const vVip = vipSet.has(v);
      
      if (uVip && !vVip) {
        vipNeighbors.get(u).add(dsu.find(v));
      } else if (!uVip && vVip) {
        vipNeighbors.get(v).add(dsu.find(u));
      }
    }
    
    for (const [vip, roots] of vipNeighbors) {
      let currentSize = 1;
      for (const root of roots) {
        currentSize += dsu.size[root];
      }
      maxComp = Math.max(maxComp, currentSize);
    }
    
    return maxComp;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  const m = parseInt(data[ptr++], 10);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[ptr++], 10);
    const v = parseInt(data[ptr++], 10);
    edges.push([u, v]);
  }
  
  const vips = [];
  while (ptr < data.length) {
    vips.push(parseInt(data[ptr++], 10));
  }
  
  const solution = new Solution();
  console.log(solution.maxComponentSize(n, edges, vips));
});
