const readline = require("readline");

class Solution {
  shortestPath(n, edges, s) {
    // 1. Build Adjacency List
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u);
    }

    // 2. Initialize Distance Array
    const dist = new Array(n).fill(-1);

    // 3. BFS
    const queue = [s];
    dist[s] = 0;
    let head = 0; // Use pointer for O(1) dequeue

    while (head < queue.length) {
      const u = queue[head++];
      for (const v of adj[u]) {
        if (dist[v] === -1) {
          dist[v] = dist[u] + 1;
          queue.push(v);
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
  if (data.length === 0) return;
  
  // Flatten data array to handle multiple numbers on one line
  const tokens = data.join(" ").trim().split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;
  
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);
  const s = Number(tokens[ptr++]);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.shortestPath(n, edges, s);
  console.log(result.join(" "));
});
