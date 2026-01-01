const readline = require('readline');

function classifyPoint(xs, ys, qx, qy) {
  const n = xs.length;
  let wn = 0;
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n;
    const xi = xs[i], yi = ys[i], xj = xs[j], yj = ys[j];
    const cross = (xj - xi) * (qy - yi) - (yj - yi) * (qx - xi);
    if (cross === 0 && Math.min(xi, xj) <= qx && qx <= Math.max(xi, xj) && Math.min(yi, yj) <= qy && qy <= Math.max(yi, yj)) {
      return "boundary";
    }
    if (yi <= qy && yj > qy && cross > 0) wn++;
    else if (yi > qy && yj <= qy && cross < 0) wn--;
  }
  return wn !== 0 ? "inside" : "outside";
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
    console.log(classifyPoint(xs, ys, nextInt(), nextInt()));
});
