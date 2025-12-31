const readline = require("readline");

function extendedGCD(a, b) {
  if (b === 0n) return [a, 1n, 0n];
  const [g, x1, y1] = extendedGCD(b, a % b);
  const x = y1;
  const y = x1 - (a / b) * y1;
  return [g, x, y];
}

function crtSolve(a, m) {
  let curA = 0n;
  let curM = 1n;
  
  for (let i = 0; i < a.length; i++) {
    const A = BigInt(a[i]);
    const M = BigInt(m[i]);
    
    let rhs = (A - curA) % M;
    if (rhs < 0n) rhs += M;
    
    const [g, x, y] = extendedGCD(curM, M);
    
    if (rhs % g !== 0n) return null;
    
    const mod = M / g;
    let k = (rhs / g) * (x % mod + mod) % mod; // x is inverse of curM/g
    
    const newM = curM * (M / g);
    curA = (curA + k * curM) % newM;
    curM = newM;
  }
  
  return curA;
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
  const k = parseInt(data[idx++], 10);
  const a = [];
  const m = [];
  for (let i = 0; i < k; i++) {
    a.push(parseInt(data[idx++], 10));
    m.push(parseInt(data[idx++], 10));
  }
  const res = crtSolve(a, m);
  console.log(res === null ? "NO" : res.toString());
});
