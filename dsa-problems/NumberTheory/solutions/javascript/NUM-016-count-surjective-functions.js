const readline = require("readline");

const MOD = 1000000007n;

function power(base, exp) {
  let res = 1n;
  base %= MOD;
  while (exp > 0n) {
    if (exp % 2n === 1n) res = (res * base) % MOD;
    base = (base * base) % MOD;
    exp /= 2n;
  }
  return res;
}

function countSurjections(n, k) {
  if (k > n) return 0;
  
  const N = BigInt(n);
  const K = BigInt(k);
  
  const C = Array(k + 1).fill(0).map(() => Array(k + 1).fill(0n));
  
  for (let i = 0; i <= k; i++) {
    C[i][0] = 1n;
    for (let j = 1; j <= i; j++) {
      C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
    }
  }
  
  let ans = 0n;
  for (let i = 0; i <= k; i++) {
    const term = (C[k][i] * power(BigInt(k - i), N)) % MOD;
    if (i % 2 === 1) {
      ans = (ans - term + MOD) % MOD;
    } else {
      ans = (ans + term) % MOD;
    }
  }
  
  return ans.toString();
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
  console.log(countSurjections(n, k));
});
