const readline = require("readline");

function gcd(a, b) {
  a = Math.abs(a);
  b = Math.abs(b);
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function maxPointsOnSegment(points, L) {
  const n = points.length;
  if (n <= 1) return n;
  
  const pointCounts = new Map();
  for (const p of points) {
    const key = `${p[0]},${p[1]}`;
    pointCounts.set(key, (pointCounts.get(key) || 0) + 1);
  }
  
  const uniquePts = [];
  const counts = [];
  for (const [key, count] of pointCounts.entries()) {
    const [x, y] = key.split(",").map(Number);
    uniquePts.push([x, y]);
    counts.push(count);
  }
  
  let maxPts = 0;
  for (const c of counts) if (c > maxPts) maxPts = c;
  
  const m = uniquePts.length;
  for (let i = 0; i < m; i++) {
    const slopeMap = new Map();
    const [x1, y1] = uniquePts[i];
    
    for (let j = 0; j < m; j++) {
      if (i === j) continue;
      const [x2, y2] = uniquePts[j];
      
      let dx = x2 - x1;
      let dy = y2 - y1;
      const dist = Math.sqrt(dx * dx + dy * dy);
      
      const g = gcd(dx, dy);
      dx /= g;
      dy /= g;
      
      // Normalize slope for a LINE (not a vector)
      if (dx < 0 || (dx === 0 && dy < 0)) {
        dx = -dx;
        dy = -dy;
      }
      
      const key = `${dx},${dy}`;
      if (!slopeMap.has(key)) slopeMap.set(key, []);
      
      // Determine signed distance along the line
      // Check if original dx matches normalized
      const origDx = x2 - x1;
      const origDy = y2 - y1;
      const signedDist = (origDx * dx + origDy * dy < 0) ? -dist : dist;
      
      slopeMap.get(key).push({dist: signedDist, count: counts[j]});
    }
    
    for (const group of slopeMap.values()) {
      group.push({dist: 0, count: counts[i]});
      group.sort((a, b) => a.dist - b.dist);
      
      let left = 0;
      let currentPts = 0;
      for (let right = 0; right < group.length; right++) {
        currentPts += group[right].count;
        while (group[right].dist - group[left].dist > L + 1e-9) {
          currentPts -= group[left].count;
          left++;
        }
        if (currentPts > maxPts) maxPts = currentPts;
      }
    }
  }
  
  return maxPts;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].length > 0) data.push(parts[i]);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const L = parseInt(data[idx++], 10);
  const points = [];
  for (let i = 0; i < n; i++) {
    const x = parseInt(data[idx++], 10);
    const y = parseInt(data[idx++], 10);
    points.push([x, y]);
  }
  console.log(maxPointsOnSegment(points, L));
});
