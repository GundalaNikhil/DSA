const readline = require("readline");

function power(base, exp, mod) {
  let res = 1n;
  base %= mod;
  while (exp > 0n) {
    if (exp % 2n === 1n) res = (res * base) % mod;
    base = (base * base) % mod;
    exp /= 2n;
  }
  return res;
}

function modExpStream(a, m, e) {
  const modBig = BigInt(m);
  const baseBig = BigInt(a);
  let ans = 1n;
  
  for (let i = 0; i < e.length; i++) {
    const d = BigInt(e[i]);
    ans = power(ans, 10n, modBig);
    const term = power(baseBig, d, modBig);
    ans = (ans * term) % modBig;
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
  const a = parseInt(data[0], 10);
  const m = parseInt(data[1], 10);
  const e = data[2];
  console.log(modExpStream(a, m, e));
});
