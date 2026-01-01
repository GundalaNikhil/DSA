const readline = require("readline");

class Solution {
  shortestDistances(n, adj, source) {
    const dist = new Array(n).fill(-1);
    dist[source] = 0;
    const queue = [source];
    
    while (queue.length > 0) {
      const node = queue.shift();
      
      for (const neighbor of adj[node]) {
        if (dist[neighbor] === -1) {
          dist[neighbor] = dist[node] + 1;
          queue.push(neighbor);
        }
      }
    }
    
    return dist;
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
    adj[v].push(u);
  }

  // Sort neighbors for deterministic traversal
  for (let i = 0; i < n; i++) {
    adj[i].sort((a, b) => a - b);
  }

  let source = 0;
  if (ptr < tokens.length) {
    source = Number(tokens[ptr++]);
  }

  const solution = new Solution();
  const result = solution.shortestDistances(n, adj, source);
  console.log(result.join(" "));
});
