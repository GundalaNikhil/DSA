const readline = require("readline");

class Solution {
  countReachable(n, edges, threshold) {
    const adj = Array.from({ length: n }, () => []);

    // Build adjacency list with weight filter
    for (const [u, v, w] of edges) {
      if (w <= threshold) {
        adj[u].push(v);
        adj[v].push(u);
      }
    }

    const visited = new Set();
    const queue = [0];
    visited.add(0);

    while (queue.length > 0) {
      const node = queue.shift();

      // Sort for deterministic traversal
      adj[node].sort((a, b) => a - b);

      for (const neighbor of adj[node]) {
        if (!visited.has(neighbor)) {
          visited.add(neighbor);
          queue.push(neighbor);
        }
      }
    }

    return visited.size;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const tokens = data.join(" ").split(/\s+/);
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const threshold = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    const w = Number(tokens[ptr++]);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  console.log(solution.countReachable(n, edges, threshold));
});
