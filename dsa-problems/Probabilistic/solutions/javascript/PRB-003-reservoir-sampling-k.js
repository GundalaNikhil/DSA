const readline = require("readline");

function reservoirSample(n, k, seed) {
  if (k === 0) return [];
  if (k > n) k = n;

  const reservoir = new Int32Array(k);
  for (let i = 0; i < k; i++) {
    reservoir[i] = i + 1;
  }

  let state = BigInt(seed);
  const multiplier = 6364136223846793005n;
  const increment = 1n;
  const mask = (1n << 64n) - 1n;

  for (let i = k + 1; i <= n; i++) {
    state = (state * multiplier + increment) & mask;

    // BigInt modulo
    const j = state % BigInt(i);

    if (j < BigInt(k)) {
      reservoir[Number(j)] = i;
    }
  }

  return Array.from(reservoir);
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
  const seed = BigInt(data[2]);
  const res = reservoirSample(n, k, seed);
  console.log(res.join(" "));
});
