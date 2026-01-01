const readline = require("readline");

class LCG {
  constructor(seed) {
    this.state = BigInt(seed) & 0xFFFFFFFFn;
  }
  nextFloat() {
    this.state = (this.state * 1664525n + 1013904223n) & 0xFFFFFFFFn;
    return Number(this.state) / 4294967296.0;
  }
}

function estimatePi(N, seed) {
  const rng = new LCG(seed);
  let countInside = 0;
  
  for (let i = 0; i < N; i++) {
    const x = rng.nextFloat();
    const y = rng.nextFloat();
    if (x * x + y * y <= 1.0) {
      countInside++;
    }
  }

  const pHat = countInside / N;
  const piHat = 4.0 * pHat;

  let error = 0.0;
  if (N > 0) {
    const stdErrP = Math.sqrt((pHat * (1.0 - pHat)) / N);
    error = 1.96 * stdErrP * 4.0;
  }

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
