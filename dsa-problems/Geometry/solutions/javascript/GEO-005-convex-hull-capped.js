const readline = require("readline");

class Solution {
  cappedHull(xs, ys, theta) {
    const n = xs.length;
    let pts = [];
    for (let i = 0; i < n; i++) pts.push([BigInt(xs[i]), BigInt(ys[i])]);
    
    // Sort points
    pts.sort((a, b) => {
      if (a[0] !== b[0]) return a[0] < b[0] ? -1 : 1;
      return a[1] < b[1] ? -1 : 1;
    });
    
    // Remove duplicates
    const unique = [];
    if (pts.length > 0) {
      unique.push(pts[0]);
      for (let i = 1; i < pts.length; i++) {
        const last = unique[unique.length - 1];
        if (pts[i][0] !== last[0] || pts[i][1] !== last[1]) {
          unique.push(pts[i]);
        }
      }
    }
    pts = unique;
    
    if (pts.length <= 1) return pts.map(p => [Number(p[0]), Number(p[1])]);
    
    const cross = (o, a, b) => {
      return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    };
    
    const lower = [];
    for (const p of pts) {
      while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], p) <= 0n) {
        lower.pop();
      }
      lower.push(p);
    }
    
    const upper = [];
    for (let i = pts.length - 1; i >= 0; i--) {
      const p = pts[i];
      while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], p) <= 0n) {
        upper.pop();
      }
      upper.push(p);
    }
    
    const hull = [...lower];
    hull.pop();
    hull.push(...upper);
    hull.pop();
    
    const h = hull.length;
    if (h <= 2) return hull.map(p => [Number(p[0]), Number(p[1])]);
    
    const cosT = Math.cos(theta * Math.PI / 180.0);
    const keep = [];
    
    for (let i = 0; i < h; i++) {
      const prev = hull[(i - 1 + h) % h];
      const curr = hull[i];
      const nxt = hull[(i + 1) % h];
      
      const ux = Number(prev[0] - curr[0]);
      const uy = Number(prev[1] - curr[1]);
      const vx = Number(nxt[0] - curr[0]);
      const vy = Number(nxt[1] - curr[1]);
      
      const lenU = Math.hypot(ux, uy);
      const lenV = Math.hypot(vx, vy);
      
      if (lenU === 0 || lenV === 0) {
        keep.push([Number(curr[0]), Number(curr[1])]);
        continue;
      }
      
      const dot = ux * vx + uy * vy;
      const cosA = -dot / (lenU * lenV);
      
      if (cosA <= cosT) {
        keep.push([Number(curr[0]), Number(curr[1])]);
      }
    }
    
    return keep;
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
  
  const theta = parseInt(data[ptr++], 10);
  
  const solution = new Solution();
  const res = solution.cappedHull(xs, ys, theta);
  
  if (res.length === 0) {
    console.log(0);
  } else {
    console.log(res.length);
    for (const p of res) {
      console.log(``p[0]`{p[1]}`);
    }
  }
});
