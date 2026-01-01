const readline = require('readline');

function distancePointSegment(x1, y1, x2, y2, px, py) {
  const ux = x2 - x1, uy = y2 - y1;
  const vx = px - x1, vy = py - y1;
  const denom = ux*ux + uy*uy;
  if (denom === 0) return Math.hypot(vx, vy);
  let t = (ux*vx + uy*vy) / denom;
  t = Math.max(0, Math.min(1, t));
  const cx = x1 + t * ux;
  const cy = y1 + t * uy;
  return Math.hypot(px - cx, py - cy);
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
    console.log(distancePointSegment(nextInt(), nextInt(), nextInt(), nextInt(), nextInt(), nextInt()).toFixed(6));
});
