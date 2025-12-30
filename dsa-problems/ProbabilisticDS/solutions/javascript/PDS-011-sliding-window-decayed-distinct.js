const readline = require("readline");

function decayedDistinct(T, lambda, times) {
  let sum = 0.0;
  for (const t of times) {
    sum += Math.exp(-lambda * (T - t));
  }
  return sum;
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
  const T = parseInt(data[idx++], 10);
  const lambda = parseFloat(data[idx++]);
  const m = parseInt(data[idx++], 10);
  const times = [];
  for (let i = 0; i < m; i++) times.push(parseInt(data[idx++], 10));
  console.log(decayedDistinct(T, lambda, times).toFixed(6));
});
