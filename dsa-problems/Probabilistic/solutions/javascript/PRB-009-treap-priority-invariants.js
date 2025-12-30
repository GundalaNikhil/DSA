const readline = require("readline");

function treapExpectations(n) {
  let H = 0.0;
  for (let i = 1; i <= n; i++) {
    H += 1.0 / i;
  }
  
  const eDepth = 2 * H - 2;
  const ePath = 2 * (n + 1) * H - 4 * n;
  
  return [eDepth, ePath];
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
  const res = treapExpectations(n);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
