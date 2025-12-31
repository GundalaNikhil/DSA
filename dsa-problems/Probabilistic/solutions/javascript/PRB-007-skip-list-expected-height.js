const readline = require("readline");

function expectedHeight(n, p) {
  return Math.log(n) / Math.log(1.0 / p);
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
  const p = parseFloat(data[1]);
  console.log(expectedHeight(n, p));
});
