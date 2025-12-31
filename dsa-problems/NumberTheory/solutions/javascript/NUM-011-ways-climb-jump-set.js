const readline = require("readline");

function countWays(n, jumps) {
  const MOD = 1000000007;
  const dp = new Int32Array(n + 1);
  dp[0] = 1;
  
  for (let i = 1; i <= n; i++) {
    for (const jump of jumps) {
      if (i >= jump) {
        dp[i] = (dp[i] + dp[i - jump]) % MOD;
      }
    }
  }
  
  return dp[n];
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
  const jumps = [];
  for (let i = 0; i < m; i++) jumps.push(parseInt(data[idx++], 10));
  console.log(countWays(n, jumps));
});
