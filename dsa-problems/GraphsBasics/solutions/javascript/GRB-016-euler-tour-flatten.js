const readline = require("readline");

class Solution {
  eulerTour(n, adj, root) {
    const tin = new Int32Array(n);
    const tout = new Int32Array(n);
    let timer = 0;

    const dfs = (u, p) => {
      tin[u] = timer++;
      
      for (const v of adj[u]) {
        if (v !== p) {
          dfs(v, u);
          timer++;
        }
      }
      
      tout[u] = timer;
    };

    dfs(root, -1);
    return [tin, tout];
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
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
    adj[v].push(u);
  }
  const root = parseInt(data[idx++], 10);

  const solution = new Solution();
  const res = solution.eulerTour(n, adj, root);
  console.log(res[0].join(" "));
  console.log(res[1].join(" "));
});
