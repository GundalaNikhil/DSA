const readline = require("readline");

class Solution {
  minEnclosingCircle(xs, ys) {
    const n = xs.length;
    const pts = [];
    for (let i = 0; i < n; i++) pts.push({ x: xs[i], y: ys[i] });
    
    // Shuffle
    for (let i = n - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [pts[i], pts[j]] = [pts[j], pts[i]];
    }
    
    const dist = (a, b) => Math.hypot(a.x - b.x, a.y - b.y);
    
    const fromTwo = (a, b) => {
      const cx = (a.x + b.x) / 2.0;
      const cy = (a.y + b.y) / 2.0;
      const r = dist(a, b) / 2.0;
      return { x: cx, y: cy, r: r };
    };
    
    const fromThree = (a, b, c) => {
      const d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
      if (Math.abs(d) < 1e-15) return { x: 0, y: 0, r: -1 };
      const ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
      const uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
      return { x: ux, y: uy, r: dist({ x: ux, y: uy }, a) };
    };
    
    const inside = (p, c) => dist(p, c) <= c.r + 1e-12;
    
    let c = { x: pts[0].x, y: pts[0].y, r: 0 };
    
    for (let i = 1; i < n; i++) {
      if (inside(pts[i], c)) continue;
      c = { x: pts[i].x, y: pts[i].y, r: 0 };
      for (let j = 0; j < i; j++) {
        if (inside(pts[j], c)) continue;
        c = fromTwo(pts[i], pts[j]);
        for (let k = 0; k < j; k++) {
          if (inside(pts[k], c)) continue;
          c = fromThree(pts[i], pts[j], pts[k]);
        }
      }
    }
    
    return [c.x, c.y, c.r];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  
  const xs = [];
  for (let i = 0; i < n; i++) xs.push(parseInt(data[ptr++], 10));
  
  const ys = [];
  for (let i = 0; i < n; i++) ys.push(parseInt(data[ptr++], 10));
  
  const solution = new Solution();
  const res = solution.minEnclosingCircle(xs, ys);
  
  console.log(``res[0].toFixed(6)`{res[1].toFixed(6)} ${res[2].toFixed(6)}`);
});
