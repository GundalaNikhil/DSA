const readline = require('readline');

function sortByAngle(xs, ys) {
  const pts = xs.map((x, i) => [x, ys[i]]);
  const half = ([x,y]) => (y > 0 || (y === 0 && x > 0)) ? 0 : 1;
  pts.sort((a, b) => {
    const ha = half(a), hb = half(b);
    if (ha !== hb) return ha - hb;
    const cross = a[0]*b[1] - a[1]*b[0];
    if (cross !== 0) return cross > 0 ? -1 : 1;
    const ra = a[0]*a[0] + a[1]*a[1];
    const rb = b[0]*b[0] + b[1]*b[1];
    return ra - rb;
  });
  return pts;
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
    let res = sortByAngle(xs, ys);
    res.forEach(p => console.log(p.join(' ')));
});
