const readline = require("readline");

function minTrials(n, P) {
  if (n < 2) return 0;
  
  const pSuccess = 2.0 / (n * (n - 1));
  
  const numerator = Math.log(1.0 - P);
  const denominator = Math.log(1.0 - pSuccess);
  
  return Math.ceil(numerator / denominator);
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
  const P = parseFloat(data[1]);
  console.log(minTrials(n, P));
});
