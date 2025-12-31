const readline = require("readline");

function countSketchEstimate(count, sign) {
  const estimates = [];
  for (let i = 0; i < count.length; i++) {
    estimates.push(count[i] * sign[i]);
  }
  estimates.sort((a, b) => a - b);
  const res = estimates[Math.floor(estimates.length / 2)];
  return res === 0 ? 0 : res;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const d = parseInt(data[idx++], 10);
  const count = [];
  const sign = [];
  for (let i = 0; i < d; i++) {
    count.push(parseInt(data[idx++], 10));
    sign.push(parseInt(data[idx++], 10));
  }
  console.log(countSketchEstimate(count, sign));
});
