const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, terminal: false });

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [n, D] = lines[idx++].split(" ").map(Number);

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v, w] = lines[idx++].split(" ").map(Number);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const q = parseInt(lines[idx++]);
  const marked = new Map();
  const results = [];

  function bfs(start) {
    const dist = new Array(n + 1).fill(Infinity);
    dist[start] = 0;
    const queue = [start];
    let head = 0;
    while (head < queue.length) {
      const u = queue[head++];
      for (const [v, w] of adj[u]) {
        if (dist[u] + w < dist[v]) {
          dist[v] = dist[u] + w;
          queue.push(v);
        }
      }
    }
    let minCost = Infinity;
    for (const [node, val] of marked) {
      if (dist[node] !== Infinity) {
        minCost = Math.min(minCost, dist[node] + val);
      }
    }
    return minCost;
  }

  for (let i = 0; i < q; i++) {
    const parts = lines[idx++].split(" ").map(Number);
    if (parts[0] === 1) {
      const [_, v, val, t] = parts;
      marked.set(v, val);
    } else {
      const [_, v, t] = parts;
      results.push(bfs(v));
    }
  }

  console.log(results.join("\n"));
});
