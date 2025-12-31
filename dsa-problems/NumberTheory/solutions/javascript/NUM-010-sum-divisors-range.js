const readline = require("readline");

function rangeSigma(L, R) {
  const MOD = 1000000007n;
  const sigma = new BigInt64Array(R + 1);
  
  for (let i = 1; i <= R; i++) {
    const val = BigInt(i);
    for (let j = i; j <= R; j += i) {
      sigma[j] += val;
    }
  }
  
  let total = 0n;
  for (let i = L; i <= R; i++) {
    total = (total + sigma[i]) % MOD;
  }
  
  return total.toString();
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const L = parseInt(data[0], 10);
  const R = parseInt(data[1], 10);
  console.log(rangeSigma(L, R));
});
