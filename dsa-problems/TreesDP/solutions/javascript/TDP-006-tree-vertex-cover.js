const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  solve();
});

function solve() {
  let idx = 0;
  const n = parseInt(lines[idx++]);

  const graph = Array.from({ length: n + 1 }, () => []);

  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () => [0, 0]);

  function dfs(u, parent) {
    dp[u][0] = 0; // Not including u
    dp[u][1] = 1; // Including u

    for (const v of graph[u]) {
      if (v === parent) continue;

      dfs(v, u);

      // If u not included, all children must be included
      dp[u][0] += dp[v][1];

      // If u included, take minimum for each child
      dp[u][1] += Math.min(dp[v][0], dp[v][1]);
    }
  }

  dfs(1, -1);

  const result = Math.min(dp[1][0], dp[1][1]);
  console.log(result);
}
