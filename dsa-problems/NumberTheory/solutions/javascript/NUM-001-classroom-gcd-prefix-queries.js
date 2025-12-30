const readline = require("readline");

function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function prefixGcds(a) {
  const n = a.length;
  if (n === 0) return [];
  
  const pref = new Int32Array(n);
  pref[0] = Math.abs(a[0]);
  
  for (let i = 1; i < n; i++) {
    pref[i] = gcd(pref[i - 1], Math.abs(a[i]));
  }
  
  return pref;
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
  const a = [];
  for (let i = 0; i < n; i++) a.push(parseInt(data[idx++], 10));
  
  const pref = prefixGcds(a);
  const out = [];
  for (let i = 0; i < q; i++) {
    const r = parseInt(data[idx++], 10);
    out.push(pref[r].toString());
  }
  console.log(out.join("\n"));
});
