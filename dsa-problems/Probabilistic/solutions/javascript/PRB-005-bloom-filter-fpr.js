const readline = require("readline");

function bloomFpr(m, k, n) {
  const exponent = (-k * n) / m;
  const term = 1.0 - Math.exp(exponent);
  return Math.pow(term, k);
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const m = parseFloat(data[0]);
  const k = parseFloat(data[1]);
  const n = parseFloat(data[2]);
  console.log(bloomFpr(m, k, n).toFixed(6));
});
