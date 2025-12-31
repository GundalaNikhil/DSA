const readline = require("readline");

function overflowProbability(m, k, c, n) {
  const lambda = (k * n) / m;
  const maxVal = (1 << c) - 1;
  
  let term = Math.exp(-lambda);
  let sum = term;
  
  for (let i = 1; i <= maxVal; i++) {
    term *= (lambda / i);
    sum += term;
  }
  
  return 1.0 - sum;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const m = parseInt(data[0], 10);
  const k = parseInt(data[1], 10);
  const c = parseInt(data[2], 10);
  const n = parseInt(data[3], 10);
  console.log(overflowProbability(m, k, c, n).toFixed(15));
});
