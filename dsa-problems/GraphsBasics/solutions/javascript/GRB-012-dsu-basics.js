const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = new Int32Array(n);
    this.rank = new Int32Array(n);
    for (let i = 0; i < n; i++) this.parent[i] = i;
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
      if (this.rank[rootI] < this.rank[rootJ]) {
        this.parent[rootI] = rootJ;
      } else if (this.rank[rootI] > this.rank[rootJ]) {
        this.parent[rootJ] = rootI;
      } else {
        this.parent[rootI] = rootJ;
        this.rank[rootJ]++;
      }
    }
  }
}

class Solution {
  processQueries(n, queries) {
    const dsu = new DSU(n);
    const results = [];
    for (const [t, u, v] of queries) {
      if (t === "union") {
        dsu.union(u, v);
      } else {
        results.push(dsu.find(u) === dsu.find(v));
      }
    }
    return results;
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
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const queries = [];
  for (let i = 0; i < q; i++) {
    const t = data[idx++];
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    queries.push([t, u, v]);
  }

  const solution = new Solution();
  const ans = solution.processQueries(n, queries);
  console.log(ans.map((x) => (x ? "true" : "false")).join("\n"));
});
