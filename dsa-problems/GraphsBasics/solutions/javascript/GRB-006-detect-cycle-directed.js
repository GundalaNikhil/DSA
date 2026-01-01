const readline = require("readline");

class Solution {
  hasCycle(n, adj) {
    const state = new Int8Array(n).fill(0); // 0: unvisited, 1: visiting, 2: visited

    for (let i = 0; i < n; i++) {
      if (state[i] === 0) {
        if (this.dfs(i, adj, state)) return true;
      }
    }
    return false;
  }

  dfs(u, adj, state) {
    state[u] = 1;
    for (const v of adj[u]) {
      if (state[v] === 1) return true;
      if (state[v] === 0) {
        if (this.dfs(v, adj, state)) return true;
      }
    }
    state[u] = 2;
    return false;
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
  
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
  }

  const solution = new Solution();
  console.log(solution.hasCycle(n, adj) ? "1" : "0");
});
