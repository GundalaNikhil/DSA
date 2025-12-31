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
  const [n, K, F] = lines[idx++].split(" ").map(Number);
  const color = [0, ...lines[idx++].split(" ").map(Number)];

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () =>
    Array.from({ length: K + 1 }, () => [0, 0])
  );
  let answer = 0;

  function dfs(u, p) {
    dp[u][0][color[u] === F ? 1 : 0] = 1;

    for (const v of adj[u]) {
      if (v === p) continue;
      dfs(v, u);

      // Save current dp[u] before merging
      const temp = dp[u].map((row) => [...row]);

      for (let d1 = 0; d1 < K; d1++) {
        for (let d2 = 0; d1 + d2 + 1 <= K; d2++) {
          for (let h1 = 0; h1 < 2; h1++) {
            for (let h2 = 0; h2 < 2; h2++) {
              if (d1 + d2 + 1 === K) {
                // Count pairs only if path is clean
                if (h1 === 0 && h2 === 0 && color[u] !== F) {
                  answer += temp[d1][h1] * dp[v][d2][h2];
                }
              }

              // Merge: path has forbidden if any segment has it or u has it
              const newHas = h1 | h2 | (color[u] === F ? 1 : 0);
              if (d1 + d2 + 1 <= K) {
                dp[u][d1 + d2 + 1][newHas] += temp[d1][h1] * dp[v][d2][h2];
              }
            }
          }
        }
      }
    }
  }

  dfs(1, 0);
  console.log(answer);
});
