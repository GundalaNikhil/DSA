const readline = require("readline");

function expectedSteps(a, b, p) {
  if (Math.abs(p - 0.5) < 1e-9) {
    return a * b;
  }

  const q = 1.0 - p;
  const r = q / p;
  const M = a + b;
  const z = b;

  const term1 = z / (q - p);
  const term2 =
    (M / (q - p)) * ((1.0 - Math.pow(r, z)) / (1.0 - Math.pow(r, M)));

  return term1 - term2;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const a = parseInt(data[0], 10);
  const b = parseInt(data[1], 10);
  const p = parseFloat(data[2]);
  console.log(expectedSteps(a, b, p).toFixed(6));
});
