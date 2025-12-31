const readline = require("readline");

function hllEstimate(m, registers) {
  let alpha;
  if (m === 16) alpha = 0.673;
  else if (m === 32) alpha = 0.697;
  else if (m === 64) alpha = 0.709;
  else alpha = 0.7213 / (1.0 + 1.079 / m);
  
  let sum = 0.0;
  let zeros = 0;
  for (const val of registers) {
    sum += Math.pow(2.0, -val);
    if (val === 0) zeros++;
  }
  
  let E = alpha * m * m / sum;
  
  if (E <= 2.5 * m) {
    if (zeros > 0) {
      E = m * Math.log(m / zeros);
    }
  }
  
  return E;
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
  const registers = [];
  for (let i = 0; i < m; i++) registers.push(parseInt(data[idx++], 10));
  console.log(hllEstimate(m, registers).toFixed(6));
});
