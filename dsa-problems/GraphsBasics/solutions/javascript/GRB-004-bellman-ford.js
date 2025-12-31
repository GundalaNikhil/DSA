const readline = require("readline");

class Solution {
  bellmanFord(n, s, edges) {
    const INF = Number.MAX_SAFE_INTEGER;
    const dist = new Array(n).fill(INF);
    dist[s] = 0;

    // Relax edges N-1 times
    for (let i = 0; i < n - 1; i++) {
      let changed = false;
      for (const [u, v, w] of edges) {
        if (dist[u] !== INF && dist[u] + w < dist[v]) {
          dist[v] = dist[u] + w;
          changed = true;
        }
      }
      if (!changed) break;
    }

    // Check for negative cycle
    for (const [u, v, w] of edges) {
      if (dist[u] !== INF && dist[u] + w < dist[v]) {
        return null; // Negative cycle
      }
    }

    // Convert INF to -1
    for (let i = 0; i < n; i++) {
      if (dist[i] === INF) dist[i] = -1;
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
  if (data.length === 0) return;
  
  const tokens = data.join(" ").trim().split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;
  
  let ptr = 0;
  const n = parseInt(tokens[ptr++], 10);
  const m = parseInt(tokens[ptr++], 10);
  const s = parseInt(tokens[ptr++], 10);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(tokens[ptr++], 10);
    const v = parseInt(tokens[ptr++], 10);
    const w = parseInt(tokens[ptr++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  const dist = solution.bellmanFord(n, s, edges);
  
  if (dist === null) {
    console.log("NEGATIVE CYCLE");
  } else {
    console.log(dist.join(" "));
  }
});
