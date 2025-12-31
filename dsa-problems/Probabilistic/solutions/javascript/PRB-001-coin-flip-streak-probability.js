const readline = require("readline");

function streakProbability(n, k) {
  if (k > n) return 0.0;

  // Use BigInt because 2^60 exceeds Number.MAX_SAFE_INTEGER
  const dp = new Array(n + 1).fill(0n);

  for (let i = 0; i < k; i++) {
    dp[i] = 1n << BigInt(i);
  }
  dp[k] = (1n << BigInt(k)) - 1n;

  for (let i = k + 1; i <= n; i++) {
    dp[i] = 2n * dp[i - 1] - dp[i - k - 1];
  }

  const total = 1n << BigInt(n);
  const valid = dp[n];

  // Convert to double for division
  // Since we need probability, we can do Number(total - valid) / Number(total)
  // But total might be huge.
  // Better: 1.0 - Number(valid) / Number(total)
  // But valid and total are huge.
  // We can compute 1 - (valid/total).
  // BigInt division truncates.
  // Convert to string and parse? Or scale?
  // Number() works up to 2^1024, but loses precision after 2^53.
  // For probability, standard double precision is fine.

  const v = Number(valid);
  const t = Number(total);
  return 1.0 - v / t;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const k = parseInt(data[1], 10);
  console.log(streakProbability(n, k));
});
