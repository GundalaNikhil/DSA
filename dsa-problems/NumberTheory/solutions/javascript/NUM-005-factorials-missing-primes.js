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

function factorialMissingPrime(n, p) {
  const N = BigInt(n);
  const P = BigInt(p);
  
  const numBlocks = N / P;
  const remainder = N % P;
  
  const res = power(P - 1n, numBlocks, P);
  
  let remFact = 1n;
  for (let i = 1n; i <= remainder; i++) {
    remFact = (remFact * i) % P;
  }
  
  return (res * remFact) % P;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10); // Note: n fits in number for parsing, but logic uses BigInt
  const p = parseInt(data[1], 10);
  // But let's pass strings to BigInt to be safe.
  console.log(factorialMissingPrime(data[0], data[1]).toString());
});
