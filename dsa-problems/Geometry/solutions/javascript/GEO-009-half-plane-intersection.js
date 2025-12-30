const readline = require("readline");

class Solution {
  halfPlaneIntersection(A, B, C) {
    const EPS = 1e-9;
    const m = A.length;
    let lines = [];
    
    for (let i = 0; i < m; i++) {
      const a = Number(A[i]);
      const b = Number(B[i]);
      const c = Number(C[i]);
      const ang = Math.atan2(b, a);
      lines.push({ a, b, c, ang });
    }
    
    // Sort by angle
    lines.sort((l1, l2) => {
      if (Math.abs(l1.ang - l2.ang) > EPS) {
        return l1.ang - l2.ang;
      }
      // Tie-break: keep tighter constraint (smaller c / norm)
      // distance from origin is c / hypot(a,b)
      // If angles are same, they are parallel and point same direction.
      // We want the one with smaller c (shifted more towards negative normal)
      // Distance from origin along normal (a,b) is c/|n|.
      // Smaller c means closer to -infinity along normal direction.
      // So smaller c is more restrictive.
      const dist1 = l1.c / Math.hypot(l1.a, l1.b);
      const dist2 = l2.c / Math.hypot(l2.a, l2.b);
      return dist1 - dist2;
    });
    
    // Remove duplicates (parallel with same angle)
    const unique = [];
    for (const ln of lines) {
      if (unique.length > 0 && Math.abs(ln.ang - unique[unique.length - 1].ang) < EPS) {
        // Already sorted by restrictiveness, so the first one we saw was the most restrictive?
        // No, we sorted ascending by dist.
        // So the first one is smaller c (more restrictive).
        // Or did we sort such that the BEST one is first?
        // Yes, dist1 - dist2 means smaller dist comes first.
        // So we keep the first one we see for each angle group.
        continue;
      }
      unique.push(ln);
    }
    lines = unique;
    
    const intersect = (l1, l2) => {
      const det = l1.a * l2.b - l2.a * l1.b;
      if (Math.abs(det) < EPS) return null;
      const x = (l1.c * l2.b - l2.c * l1.b) / det;
      const y = (l1.a * l2.c - l2.a * l1.c) / det;
      return { x, y };
    };
    
    const outside = (p, l) => {
      return l.a * p.x + l.b * p.y - l.c > EPS;
    };
    
    const dq = [];
    
    for (const ln of lines) {
      while (dq.length >= 2 && outside(intersect(dq[dq.length - 2], dq[dq.length - 1]), ln)) {
        dq.pop();
      }
      while (dq.length >= 2 && outside(intersect(dq[0], dq[1]), ln)) {
        dq.shift();
      }
      dq.push(ln);
    }
    
    while (dq.length >= 3 && outside(intersect(dq[dq.length - 2], dq[dq.length - 1]), dq[0])) {
      dq.pop();
    }
    while (dq.length >= 3 && outside(intersect(dq[0], dq[1]), dq[dq.length - 1])) {
      dq.shift();
    }
    
    if (dq.length < 3) return [];
    
    const poly = [];
    for (let i = 0; i < dq.length; i++) {
      const p = intersect(dq[i], dq[(i + 1) % dq.length]);
      if (!p) return []; // Should not happen if logic is correct
      poly.push(p);
    }
    
    // Rotate to lowest x, then y
    let minIdx = 0;
    for (let i = 1; i < poly.length; i++) {
      if (poly[i].x < poly[minIdx].x - EPS || (Math.abs(poly[i].x - poly[minIdx].x) < EPS && poly[i].y < poly[minIdx].y)) {
        minIdx = i;
      }
    }
    
    const res = [];
    for (let i = 0; i < poly.length; i++) {
      res.push(poly[(minIdx + i) % poly.length]);
    }
    
    return res;
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
  const m = parseInt(data[ptr++], 10);
  
  const A = [];
  const B = [];
  const C = [];
  
  for (let i = 0; i < m; i++) {
    A.push(parseInt(data[ptr++], 10));
    B.push(parseInt(data[ptr++], 10));
    C.push(parseInt(data[ptr++], 10));
  }
  
  const solution = new Solution();
  const res = solution.halfPlaneIntersection(A, B, C);
  
  if (res.length === 0) {
    console.log("EMPTY");
  } else {
    console.log(res.length);
    for (const p of res) {
      console.log(``p.x.toFixed(6)`{p.y.toFixed(6)}`);
    }
  }
});
