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

  const weight = [0, ...lines[idx++].split(" ").map(Number)];

  const graph = Array.from({ length: n + 1 }, () => []);

  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () => [0, 0, 0]);

  function dfs(u, parent) {
    dp[u][0] = 0;
    dp[u][1] = 0;
    dp[u][2] = weight[u];

    let sumWithoutSelected = 0;
    let maxGain = -Infinity;

    for (const v of graph[u]) {
      if (v === parent) continue;

      dfs(v, u);

      const bestNotSelected = Math.max(dp[v][0], dp[v][1]);
      sumWithoutSelected += bestNotSelected;

      const gain = dp[v][2] - bestNotSelected;
      maxGain = Math.max(maxGain, gain);

      dp[u][2] += dp[v][0];
    }

    dp[u][0] = sumWithoutSelected;

    if (maxGain > -Infinity) {
      dp[u][1] = sumWithoutSelected + maxGain;
    }
  }

  dfs(1, -1);

  const result = Math.max(dp[1][0], dp[1][1], dp[1][2]);
  console.log(result);
}
