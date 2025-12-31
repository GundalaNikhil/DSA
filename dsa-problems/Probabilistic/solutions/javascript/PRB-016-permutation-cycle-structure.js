const readline = require("readline");

function cycleExpectations(n, k) {
  const expectedCyclesK = 1.0 / k;
  const expectedLongest = n * 0.624330;
  return [expectedCyclesK, expectedLongest];
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
  const k = parseInt(data[1], 10);
  const res = cycleExpectations(n, k);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
