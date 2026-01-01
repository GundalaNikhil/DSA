const MOD = 1000000007n;

class Solution {
  countExpressions(s, M, K, L) {
    if (L <= 0 || M <= 0) return 0;
    const n = s.length;
    const dp = Array.from({ length: n + 1 }, () =>
      Array.from({ length: M }, () => [0n, 0n])
    );

    for (let len = 1; len <= L && len <= n; len++) {
      if (s[0] === '0' && len > 1) break;
      const val = BigInt(parseInt(s.substring(0, len))) % BigInt(M);
      dp[len][Number(val)][0] = (dp[len][Number(val)][0] + 1n) % MOD;
    }

    for (let pos = 1; pos < n; pos++) {
      for (let rem = 0; rem < M; rem++) {
        for (let used = 0; used <= 1; used++) {
          const ways = dp[pos][rem][used];
          if (ways === 0n) continue;
          for (let len = 1; len <= L && pos + len <= n; len++) {
            if (s[pos] === '0' && len > 1) break;
            const val = BigInt(parseInt(s.substring(pos, pos + len)));
            const addRem = Number((BigInt(rem) + val) % BigInt(M));
            const subRem = Number((BigInt(rem) - val) % BigInt(M) + BigInt(M)) % M;
            dp[pos + len][addRem][used] = (dp[pos + len][addRem][used] + ways) % MOD;
            dp[pos + len][subRem][1] = (dp[pos + len][subRem][1] + ways) % MOD;
          }
        }
      }
    }

    if (K < 0 || K >= M) return 0;
    return Number(dp[n][K][1] % MOD);
  }
}

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;

  let ptr = 0;
  const s = data[ptr++];
  const parts = data[ptr++].split(/\s+/).map(Number);
  const M = parts[0];
  const K = parts[1];
  const L = parts[2];

  const solution = new Solution();
  console.log(solution.countExpressions(s, M, K, L));
});
