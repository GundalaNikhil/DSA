const readline = require("readline");
const MOD = 1000000007n;

class Solution {
  countWays(n, J, cracked) {
    if (cracked[n]) return 0;

    const dp = new Array(n + 1).fill(0n);
    dp[0] = 1n;
    let windowSum = 1n;

    for (let i = 1; i <= n; i++) {
      dp[i] = cracked[i] ? 0n : windowSum;
      windowSum = (windowSum + dp[i]) % MOD;

      const out = i - J;
      if (out >= 0) {
        windowSum = (windowSum - dp[out]) % MOD;
        if (windowSum < 0n) windowSum += MOD;
      }
    }
    return Number(dp[n] % MOD);
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [nStr, jStr] = lines[idx++].split(" ");
  const n = Number(nStr);
  const J = Number(jStr);
  const m = Number(lines[idx++]);

  const cracked = new Array(n + 1).fill(false);
  if (m > 0) {
    const arr = (lines[idx++] ?? "").split(" ").filter(Boolean).map(Number);
    for (const x of arr) {
      if (1 <= x && x <= n) cracked[x] = true;
    }
  }

  const sol = new Solution();
  console.log(sol.countWays(n, J, cracked));
});
