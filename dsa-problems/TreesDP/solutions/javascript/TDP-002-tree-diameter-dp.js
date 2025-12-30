const readline = require("readline");

class Solution {
  constructor() {
    this.tree = [];
    this.diameter = 0;
  }

  treeDiameter(n, edges) {
    this.tree = Array.from({ length: n + 1 }, () => []);
    this.diameter = 0;

    for (const [u, v] of edges) {
      this.tree[u].push(v);
      this.tree[v].push(u);
    }

    this.dfs(1, -1);
    return this.diameter;
  }

  dfs(node, parent) {
    let max1 = 0,
      max2 = 0;

    for (const child of this.tree[node]) {
      if (child === parent) continue;

      const childDepth = this.dfs(child, node);

      if (childDepth > max1) {
        max2 = max1;
        max1 = childDepth;
      } else if (childDepth > max2) {
        max2 = childDepth;
      }
    }

    this.diameter = Math.max(this.diameter, max1 + max2);
    return max1 + 1;
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

  const edges = [];
  for (let i = 1; i < n; i++) {
    const [u, v] = lines[i].split(" ").map(Number);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.treeDiameter(n, edges);

  console.log(result);
});
