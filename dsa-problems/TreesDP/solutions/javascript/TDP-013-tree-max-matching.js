const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, terminal: false });

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const n = parseInt(lines[idx++]);

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () => [0, 0]);

  function dfs(u, p) {
    dp[u][0] = 0;
    dp[u][1] = 0;
    let sum = 0;

    for (const v of adj[u]) {
      if (v === p) continue;
      dfs(v, u);
      sum += Math.max(dp[v][0], dp[v][1]);
    }

    dp[u][0] = sum;

    for (const v of adj[u]) {
      if (v === p) continue;
      dp[u][1] = Math.max(
        dp[u][1],
        1 + dp[v][0] + sum - Math.max(dp[v][0], dp[v][1])
      );
    }
  }

  dfs(1, 0);
  console.log(Math.max(dp[1][0], dp[1][1]));
});
