const readline = require("readline");

class Solution {
  constructor() {
    this.tree = [];
    this.values = [];
    this.subtreeSize = [];
    this.subtreeSum = [];
  }

  computeSubtreeMetrics(n, nodeValues, edges) {
    this.tree = Array.from({ length: n + 1 }, () => []);
    this.values = [0, ...nodeValues];
    this.subtreeSize = Array(n + 1).fill(0);
    this.subtreeSum = Array(n + 1).fill(0);

    for (const [u, v] of edges) {
      this.tree[u].push(v);
      this.tree[v].push(u);
    }

    this.dfs(1, -1);
  }

  dfs(node, parent) {
    this.subtreeSize[node] = 1;
    this.subtreeSum[node] = this.values[node];

    for (const child of this.tree[node]) {
      if (child === parent) continue;

      this.dfs(child, node);
      this.subtreeSize[node] += this.subtreeSize[child];
      this.subtreeSum[node] += this.subtreeSum[child];
    }
  }

  getSubtreeSums() {
    return this.subtreeSum.slice(1);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  const n = parseInt(lines[0]);
  const values = lines[1].split(" ").map(Number);

  const edges = [];
  for (let i = 2; i < n + 1; i++) {
    const [u, v] = lines[i].split(" ").map(Number);
    edges.push([u, v]);
  }

  const solution = new Solution();
  solution.computeSubtreeMetrics(n, values, edges);

  const sums = solution.getSubtreeSums();
  sums.forEach((s) => console.log(s));
});
