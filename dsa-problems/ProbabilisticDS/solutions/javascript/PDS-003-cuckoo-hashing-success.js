const readline = require("readline");

function successProbability(m, alpha) {
  const val = 1.0 - alpha;
  const exponent = -(val * val * m) / 2.0;
  const pFail = Math.exp(exponent);
  return 1.0 - pFail;
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
  const alpha = parseFloat(data[1]);
  console.log(successProbability(m, alpha).toFixed(6));
});
