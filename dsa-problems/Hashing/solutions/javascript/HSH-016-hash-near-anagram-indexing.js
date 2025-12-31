const readline = require("readline");

class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.count = n;
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
      this.count--;
    }
  }
}

class Solution {
  countNearAnagramGroups(words) {
    const n = words.length;
    const uf = new UnionFind(n);
    const groups = new Map();
    
    for (let i = 0; i < n; i++) {
      const chars = words[i].split('').sort();
      const sortedWord = chars.join('');
      const len = sortedWord.length;
      
      for (let j = 0; j < len; j++) {
        // Optimization: skip duplicates
        if (j > 0 && sortedWord[j] === sortedWord[j - 1]) continue;
        
        const reduced = sortedWord.substring(0, j) + sortedWord.substring(j + 1);
        if (!groups.has(reduced)) {
          groups.set(reduced, []);
        }
        groups.get(reduced).push(i);
      }
    }
    
    for (const indices of groups.values()) {
      const first = indices[0];
      for (let k = 1; k < indices.length; k++) {
        uf.union(first, indices[k]);
      }
    }
    
    return uf.count;
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
  
  const words = [];
  for (let i = 0; i < n; i++) {
    words.push(data[ptr++]);
  }
  
  const solution = new Solution();
  console.log(solution.countNearAnagramGroups(words));
});
