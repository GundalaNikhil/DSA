const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const firstLine = lines[idx++].split(" ").map(Number);
  const n = firstLine[0];
  const k = firstLine[1];

  const cost = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));
  for (let i = 1; i <= n; i++) {
    const vals = lines[idx++].split(" ").map(Number);
    for (let j = 1; j <= k; j++) {
      cost[i][j] = vals[j - 1];
    }
  }

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));
  const visited = Array(n + 1).fill(false);

  // Iterative DFS with post-order processing
  const stack = [[1, 0]]; // [node, phase]
  const parent = Array(n + 1).fill(0);

  while (stack.length > 0) {
    const [u, phase] = stack.pop();

    if (phase === 0) {
      visited[u] = true;
      for (let c = 1; c <= k; c++) {
        dp[u][c] = cost[u][c];
      }
      stack.push([u, 1]);
      for (const v of adj[u]) {
        if (!visited[v]) {
          parent[v] = u;
          stack.push([v, 0]);
        }
      }
    } else {
      // Post-order: process children contributions
      for (const v of adj[u]) {
        if (parent[v] === u) {
          let min1 = Infinity,
            min2 = Infinity;
          let minColor = -1;
          for (let c = 1; c <= k; c++) {
            if (dp[v][c] < min1) {
              min2 = min1;
              min1 = dp[v][c];
              minColor = c;
            } else if (dp[v][c] < min2) {
              min2 = dp[v][c];
            }
          }

          for (let c = 1; c <= k; c++) {
            if (c === minColor) {
              dp[u][c] += min2;
            } else {
              dp[u][c] += min1;
            }
          }
        }
      }
    }
  }

  let result = Infinity;
  for (let c = 1; c <= k; c++) {
    result = Math.min(result, dp[1][c]);
  }

  console.log(result);
});
