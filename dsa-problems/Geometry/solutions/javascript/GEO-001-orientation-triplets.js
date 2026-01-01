const readline = require('readline');

function orientation(x1, y1, x2, y2, x3, y3) {
  const cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
  if (cross === 0) return "collinear";
  return cross > 0 ? "counterclockwise" : "clockwise";
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
    console.log(orientation(nextInt(), nextInt(), nextInt(), nextInt(), nextInt(), nextInt()));
});
