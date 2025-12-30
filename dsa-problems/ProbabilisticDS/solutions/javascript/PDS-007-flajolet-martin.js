const readline = require("readline");

function estimateDistinct(R) {
  return Math.pow(2, R) / 0.77351;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const R = parseInt(data[0], 10);
  console.log(estimateDistinct(R).toFixed(6));
});
