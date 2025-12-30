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

function lcmRange(a, l, r, MOD) {
  const maxExponents = new Map();
  const modBig = BigInt(MOD);
  
  for (let i = l; i <= r; i++) {
    let num = a[i];
    for (let p = 2; p * p <= num; p++) {
      if (num % p === 0) {
        let count = 0;
        while (num % p === 0) {
          num /= p;
          count++;
        }
        const current = maxExponents.get(p) || 0;
        if (count > current) maxExponents.set(p, count);
      }
    }
    if (num > 1) {
      const current = maxExponents.get(num) || 0;
      if (1 > current) maxExponents.set(num, 1);
    }
  }
  
  let ans = 1n;
  for (const [p, e] of maxExponents.entries()) {
    ans = (ans * power(BigInt(p), BigInt(e), modBig)) % modBig;
  }
  
  return ans.toString();
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].length > 0) data.push(parts[i]);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const MOD = parseInt(data[idx++], 10);
  const a = [];
  for (let i = 0; i < n; i++) a.push(parseInt(data[idx++], 10));
  
  const out = [];
  for (let i = 0; i < q; i++) {
    const l = parseInt(data[idx++], 10);
    const r = parseInt(data[idx++], 10);
    out.push(lcmRange(a, l, r, MOD));
  }
  console.log(out.join("\n"));
});
