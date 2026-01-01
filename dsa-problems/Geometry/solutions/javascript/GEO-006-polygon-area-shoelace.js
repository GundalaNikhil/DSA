const readline = require('readline');

function polygonArea(xs, ys) {
  const n = xs.length;
  let sum = 0n;
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n;
    sum += BigInt(xs[i]) * BigInt(ys[j]) - BigInt(xs[j]) * BigInt(ys[i]);
  }
  const absSum = sum < 0n ? -sum : sum;
  return absSum / 2n;
}


const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    const nextFloat = () => parseFloat(next());
    let n = nextInt();
    let xs = [], ys = [];
    for(let i=0; i<n; i++) { xs.push(nextInt()); ys.push(nextInt()); }
    console.log(Number(polygonArea(xs, ys)));
});
