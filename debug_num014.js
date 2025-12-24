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

function solve(points, L) {
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
  
  let maxPts = Math.max(...counts);
  
  for (let i = 0; i < uniquePts.length; i++) {
    const slopeMap = new Map();
    const [x1, y1] = uniquePts[i];
    
    for (let j = 0; j < uniquePts.length; j++) {
      if (i === j) continue;
      const [x2, y2] = uniquePts[j];
      
      const dx = x2 - x1;
      const dy = y2 - y1;
      const dist = Math.sqrt(dx * dx + dy * dy);
      
      if (dist > L + 1e-9) continue;
      
      const g = gcd(dx, dy);
      const slope = `${dx / g},${dy / g}`;
      slopeMap.set(slope, (slopeMap.get(slope) || 0) + counts[j]);
    }
    
    for (const count of slopeMap.values()) {
      maxPts = Math.max(maxPts, counts[i] + count);
    }
  }
  
  return maxPts;
}

const points = [[0,0], [1,1], [2,2], [0,1]];
const L = 2;
console.log(solve(points, L));
