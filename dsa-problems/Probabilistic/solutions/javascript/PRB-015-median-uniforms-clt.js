const readline = require("readline");

function medianClt(n) {
  const mean = 0.5;
  const variance = 1.0 / (4 * n);
  return [mean, variance];
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
  const res = medianClt(n);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
