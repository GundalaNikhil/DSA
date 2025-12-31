const readline = require("readline");

function xorFilterStats(n, b) {
  const cells = Math.ceil(1.23 * n);
  const mem = cells * b;
  const fpr = Math.pow(2.0, -b);
  return [mem, fpr];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const b = parseInt(data[1], 10);
  const res = xorFilterStats(n, b);
  console.log(res[0] + " " + res[1].toFixed(6));
});
