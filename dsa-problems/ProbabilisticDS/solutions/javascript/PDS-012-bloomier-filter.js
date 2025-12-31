const readline = require("readline");

function bloomierStats(m, r) {
  const mem = m * r;
  const fpr = Math.pow(2.0, -r);
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
  const m = parseInt(data[0], 10);
  const r = parseInt(data[1], 10);
  const res = bloomierStats(m, r);
  console.log(res[0] + " " + res[1].toFixed(6));
});
