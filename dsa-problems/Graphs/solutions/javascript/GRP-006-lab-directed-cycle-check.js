const readline = require("readline");

class Solution {
  hasCycle(n, adj) {
    const visited = new Array(n).fill(false);
    const recStack = new Array(n).fill(false);

    const dfs = (node) => {
      visited[node] = true;
      recStack[node] = true;

      for (const neighbor of adj[node]) {
        if (!visited[neighbor]) {
          if (dfs(neighbor)) {
            return true;
          }
        } else if (recStack[neighbor]) {
          return true; // Back edge - cycle detected
        }
      }

      recStack[node] = false;
      return false;
    };

    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        if (dfs(i)) {
          return true;
        }
      }
    }

    return false;
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
  const m = Number(tokens[ptr++]);

  const adj = Array.from({ length: n }, () => []);

  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    adj[u].push(v);
  }

  // Sort neighbors for deterministic traversal
  for (let i = 0; i < n; i++) {
    adj[i].sort((a, b) => a - b);
  }

  const solution = new Solution();
  console.log(solution.hasCycle(n, adj) ? "true" : "false");
});
