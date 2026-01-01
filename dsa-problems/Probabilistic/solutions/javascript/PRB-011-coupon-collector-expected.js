const readline = require("readline");

function expectedDraws(N) {
  let harmonicSum = 0.0;
  for (let i = 1; i <= N; i++) {
    harmonicSum += 1.0 / i;
  }
  return N * harmonicSum;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  const N = parseInt(data[0], 10);
  console.log(expectedDraws(N).toFixed(6));
});
