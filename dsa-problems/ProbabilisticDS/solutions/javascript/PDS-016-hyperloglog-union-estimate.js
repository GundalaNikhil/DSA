const readline = require("readline");

function hllUnionEstimate(m, a, b) {
  let alpha;
  if (m === 16) alpha = 0.673;
  else if (m === 32) alpha = 0.697;
  else if (m === 64) alpha = 0.709;
  else alpha = 0.7213 / (1.0 + 1.079 / m);
  
  let sum = 0.0;
  for (let i = 0; i < m; i++) {
    const val = Math.max(a[i], b[i]);
    sum += Math.pow(2.0, -val);
  }
  
  return alpha * m * m / sum;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const m = parseInt(data[idx++], 10);
  const a = [];
  const b = [];
  for (let i = 0; i < m; i++) a.push(parseInt(data[idx++], 10));
  for (let i = 0; i < m; i++) b.push(parseInt(data[idx++], 10));
  console.log(hllUnionEstimate(m, a, b).toFixed(6));
});
