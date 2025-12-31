const readline = require("readline");

class Solution {
  largestEmptyCircle(xL, yB, xR, yT, xs, ys) {
    const n = xs.length;
    const pts = [];
    for (let i = 0; i < n; i++) pts.push({ x: xs[i], y: ys[i] });
    
    const candidates = [];
    // Corners
    candidates.push({ x: xL, y: yB });
    candidates.push({ x: xL, y: yT });
    candidates.push({ x: xR, y: yB });
    candidates.push({ x: xR, y: yT });
    
    // Edge projections
    for (const p of pts) {
      candidates.push({ x: p.x, y: yB });
      candidates.push({ x: p.x, y: yT });
      candidates.push({ x: xL, y: p.y });
      candidates.push({ x: xR, y: p.y });
    }
    
    // Midpoints
    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        candidates.push({ x: (pts[i].x + pts[j].x) / 2.0, y: (pts[i].y + pts[j].y) / 2.0 });
      }
    }
    
    // Circumcenters (small n)
    if (n <= 60) {
      for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
          for (let k = j + 1; k < n; k++) {
            const a = pts[i], b = pts[j], c = pts[k];
            const d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
            if (Math.abs(d) < 1e-12) continue;
            const ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
            const uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
            candidates.push({ x: ux, y: uy });
          }
        }
      }
    }
    
    const dist = (p, q) => Math.hypot(p.x - q.x, p.y - q.y);
    const distToEdge = (p) => Math.min(p.x - xL, xR - p.x, p.y - yB, yT - p.y);
    const insideRect = (p) => {
      const EPS = 1e-12;
      return p.x >= xL - EPS && p.x <= xR + EPS && p.y >= yB - EPS && p.y <= yT + EPS;
    };
    
    let best = 0.0;
    for (const c of candidates) {
      if (!insideRect(c)) continue;
      let r = distToEdge(c);
      for (const p of pts) {
        r = Math.min(r, dist(c, p));
      }
      best = Math.max(best, r);
    }
    
    return best;
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
  const xL = parseInt(data[ptr++], 10);
  const yB = parseInt(data[ptr++], 10);
  const xR = parseInt(data[ptr++], 10);
  const yT = parseInt(data[ptr++], 10);
  
  const n = parseInt(data[ptr++], 10);
  
  const xs = [];
  for (let i = 0; i < n; i++) xs.push(parseInt(data[ptr++], 10));
  
  const ys = [];
  for (let i = 0; i < n; i++) ys.push(parseInt(data[ptr++], 10));
  
  const solution = new Solution();
  console.log(solution.largestEmptyCircle(xL, yB, xR, yT, xs, ys).toFixed(6));
});
