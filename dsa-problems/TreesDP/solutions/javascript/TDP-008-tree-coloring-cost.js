const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  // Token-based parsing like Python
  const data = [];
  lines.forEach(line => data.push(...line.split(" ")));
  
  let idx = 0;
  const n = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);

  const cost = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= k; j++) {
      cost[i][j] = parseInt(data[idx++]);
    }
  }

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++]);
    const v = parseInt(data[idx++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));
  const visited = Array(n + 1).fill(false);

  function dfs(u) {
    visited[u] = true;
    for (let c = 1; c <= k; c++) {
      dp[u][c] = cost[u][c];
    }

    for (const v of adj[u]) {
      if (!visited[v]) {
        dfs(v);
        
        // For each color c at u, add minimum cost from child v
        // where child uses any color except c
        for (let c = 1; c <= k; c++) {
          let minChildCost = Infinity;
          for (let c2 = 1; c2 <= k; c2++) {
            if (c2 !== c) {
              minChildCost = Math.min(minChildCost, dp[v][c2]);
            }
          }
          dp[u][c] += minChildCost;
        }
      }
    }
  }

  dfs(1);
  
  let result = Infinity;
  for (let c = 1; c <= k; c++) {
    result = Math.min(result, dp[1][c]);
  }

  console.log(result);
});
