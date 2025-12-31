const readline = require("readline");

class Solution {
  shortestPathDAG(n, adj, s) {
    const visited = new Int8Array(n).fill(0);
    const stack = [];

    const dfs = (u) => {
      visited[u] = 1;
      for (const [v, w] of adj[u]) {
        if (!visited[v]) dfs(v);
      }
      stack.push(u);
    };

    for (let i = 0; i < n; i++) {
      if (!visited[i]) dfs(i);
    }

    // Initialize distances
    // Use BigInt for safety with large weights, though Number is usually fine up to 2^53
    // Problem constraints 10^9 * 10^5 = 10^14, fits in Number.
    const INF = 1e15;
    const dist = new Array(n).fill(INF);
    dist[s] = 0;

    // Process in topological order (reverse of post-order stack)
    while (stack.length > 0) {
      const u = stack.pop();

      if (dist[u] !== INF) {
        for (const [v, w] of adj[u]) {
          if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
          }
        }
      }
    }

    return dist.map((d) => (d === INF ? -1 : d));
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const s = parseInt(data[idx++], 10);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    adj[u].push([v, w]);
  }

  const solution = new Solution();
  const dist = solution.shortestPathDAG(n, adj, s);
  console.log(dist.join(" "));
});
