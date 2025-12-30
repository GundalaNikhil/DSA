const readline = require("readline");

function minTrials(n, C) {
  const p = 1.0 / (n * n);
  
  const num = Math.log(1.0 - C);
  const den = Math.log(1.0 - p);
  
  return Math.ceil(num / den);
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
  const C = parseFloat(data[1]);
  console.log(minTrials(n, C));
});
