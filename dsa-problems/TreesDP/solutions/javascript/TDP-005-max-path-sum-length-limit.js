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
  const [n, L] = lines[idx++].split(" ").map(Number);

  const value = [0];
  const values = lines[idx++].split(" ").map(Number);
  value.push(...values);

  const graph = Array.from({ length: n + 1 }, () => []);

  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  const NEG_INF = -1e18;
  const dp = Array.from({ length: n + 1 }, () => Array(L + 1).fill(NEG_INF));

  let maxSum = NEG_INF;

  function dfs(u, parent) {
    dp[u][0] = value[u];
    maxSum = Math.max(maxSum, value[u]);

    const childPaths = [];

    for (const v of graph[u]) {
      if (v === parent) continue;

      dfs(v, u);

      const childBest = Array(L + 1).fill(NEG_INF);

      for (let len = 0; len < L; len++) {
        if (dp[v][len] > NEG_INF) {
          const extended = dp[v][len] + value[u];
          dp[u][len + 1] = Math.max(dp[u][len + 1], extended);
          childBest[len] = dp[v][len];
        }
      }

      childPaths.push(childBest);
    }

    for (let len = 0; len <= L; len++) {
      maxSum = Math.max(maxSum, dp[u][len]);
    }

    for (let i = 0; i < childPaths.length; i++) {
      for (let j = i + 1; j < childPaths.length; j++) {
        const path1 = childPaths[i];
        const path2 = childPaths[j];

        for (let len1 = 0; len1 <= L; len1++) {
          for (let len2 = 0; len2 <= L; len2++) {
            // Total edges: len1 + 1 (to u) + 1 (from u) + len2
            if (len1 + len2 + 2 > L) continue;
            if (path1[len1] > NEG_INF && path2[len2] > NEG_INF) {
              const combined = path1[len1] + path2[len2] + value[u];
              maxSum = Math.max(maxSum, combined);
            }
          }
        }
      }
    }
  }

  dfs(1, -1);

  console.log(maxSum);
}
