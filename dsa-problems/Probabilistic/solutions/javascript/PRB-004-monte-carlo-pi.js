const readline = require("readline");

function estimatePi(N, C) {
  const pHat = C / N;
  const piHat = 4.0 * pHat;

  const stdErrP = Math.sqrt((pHat * (1.0 - pHat)) / N);
  const error = 1.96 * stdErrP * 4.0;

  return [piHat, error];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const N = parseInt(data[0], 10);
  const C = parseInt(data[1], 10);
  const res = estimatePi(N, C);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
