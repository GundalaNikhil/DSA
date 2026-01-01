const readline = require("readline");

class Solution {
  canColorBipartite(n, adj, locked) {
    const color = new Array(n).fill(-1);
    
    // Pre-color locked nodes
    for (let i = 0; i < n; i++) {
      if (locked[i] !== 0) {
        color[i] = locked[i];
      }
    }
    
    const bfs = (start) => {
      const queue = [start];
      if (color[start] === -1) {
        color[start] = locked[start] === 0 ? 1 : locked[start];
      }
      
      while (queue.length > 0) {
        const node = queue.shift();
        const requiredNeighborColor = 3 - color[node];
        
        for (const neighbor of adj[node]) {
          if (color[neighbor] === -1) {
            if (locked[neighbor] !== 0 && locked[neighbor] !== requiredNeighborColor) {
              return false;
            }
            color[neighbor] = requiredNeighborColor;
            queue.push(neighbor);
          } else if (color[neighbor] !== requiredNeighborColor) {
            return false;
          }
        }
      }
      
      return true;
    };
    
    // Check each component
    for (let i = 0; i < n; i++) {
      if (color[i] === -1) {
        if (!bfs(i)) {
          return false;
        }
      }
    }
    
    return true;
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

  // Parse locked array, defaulting to all zeros if missing
  const locked = Array(n).fill(0);
  let lockIdx = 0;
  while (ptr < tokens.length && lockIdx < n) {
    locked[lockIdx++] = Number(tokens[ptr++]);
  }

  const solution = new Solution();
  console.log(solution.canColorBipartite(n, adj, locked) ? "true" : "false");
});
