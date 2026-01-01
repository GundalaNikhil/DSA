const readline = require("readline");

function solve(n) {
  let h = 0.0;
  for (let i = 1; i <= n; i++) {
    h += 1.0 / i;
  }
  return h;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  console.log(solve(n).toFixed(6));
});
