const readline = require("readline");

class Solution {
  findArticulationPoints(n, adj) {
    const disc = Array(n).fill(-1);
    const low = Array(n).fill(-1);
    const parent = Array(n).fill(-1);
    const ap = new Set();
    let time = 0;
    
    const dfs = (u) => {
      let children = 0;
      disc[u] = low[u] = time++;
      
      for (const v of adj[u]) {
        if (disc[v] === -1) {
          children++;
          parent[v] = u;
          dfs(v);
          
          low[u] = Math.min(low[u], low[v]);
          
          if (parent[u] !== -1 && low[v] >= disc[u]) {
            ap.add(u);
          }
        } else if (v !== parent[u]) {
          low[u] = Math.min(low[u], disc[v]);
        }
      }
      
      if (parent[u] === -1 && children > 1) {
        ap.add(u);
      }
    };
    
    for (let i = 0; i < n; i++) {
      if (disc[i] === -1) {
        dfs(i);
      }
    }
    
    return Array.from(ap);
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

  const solution = new Solution();
  const articulationPoints = solution.findArticulationPoints(n, adj);
  articulationPoints.sort((a, b) => a - b);

  console.log(articulationPoints.length);
  if (articulationPoints.length > 0) {
    console.log(articulationPoints.join(" "));
  }
});
