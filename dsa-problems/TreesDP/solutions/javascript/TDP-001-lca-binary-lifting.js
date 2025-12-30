const readline = require("readline");

class Solution {
  constructor() {
    this.LOG = 20;
    this.tree = [];
    this.up = [];
    this.depth = [];
    this.n = 0;
  }

  preprocess(root, n, edges) {
    this.n = n;
    this.tree = Array.from({ length: n + 1 }, () => []);
    this.up = Array.from({ length: n + 1 }, () => Array(this.LOG).fill(-1));
    this.depth = Array(n + 1).fill(0);

    // Build adjacency list
    for (const [u, v] of edges) {
      this.tree[u].push(v);
      this.tree[v].push(u);
    }

    // DFS to compute depths and immediate parents
    this.dfs(root, -1, 0);

    // Binary lifting preprocessing
    for (let j = 1; j < this.LOG; j++) {
      for (let i = 1; i <= n; i++) {
        if (this.up[i][j - 1] !== -1) {
          this.up[i][j] = this.up[this.up[i][j - 1]][j - 1];
        }
      }
    }
  }

  dfs(node, parent, d) {
    this.up[node][0] = parent;
    this.depth[node] = d;
    for (const child of this.tree[node]) {
      if (child !== parent) {
        this.dfs(child, node, d + 1);
      }
    }
  }

  lca(u, v) {
    // Make u deeper
    if (this.depth[u] < this.depth[v]) {
      [u, v] = [v, u];
    }

    // Lift u to same level as v
    let diff = this.depth[u] - this.depth[v];
    for (let j = 0; j < this.LOG; j++) {
      if ((diff >> j) & 1) {
        u = this.up[u][j];
      }
    }

    if (u === v) return u;

    // Lift both simultaneously
    for (let j = this.LOG - 1; j >= 0; j--) {
      if (this.up[u][j] !== -1 && this.up[u][j] !== this.up[v][j]) {
        u = this.up[u][j];
        v = this.up[v][j];
      }
    }

    return this.up[u][0];
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
  const [n, q] = lines[0].split(" ").map(Number);

  const edges = [];
  for (let i = 1; i < n; i++) {
    const [u, v] = lines[i].split(" ").map(Number);
    edges.push([u, v]);
  }

  const solution = new Solution();
  solution.preprocess(1, n, edges);

  const results = [];
  for (let i = n; i < n + q; i++) {
    const [u, v] = lines[i].split(" ").map(Number);
    results.push(solution.lca(u, v));
  }

  console.log(results.join("\n"));
});
