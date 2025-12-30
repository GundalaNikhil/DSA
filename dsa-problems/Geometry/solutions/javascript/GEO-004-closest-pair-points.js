function closestPair(xs, ys) {
  const n = xs.length;
  const pts = Array.from({ length: n }, (_, i) => [xs[i], ys[i]]);
  pts.sort((a, b) => (a[0] - b[0]) || (a[1] - b[1]));
  for (let i = 1; i < n; i++) {
    if (pts[i][0] === pts[i-1][0] && pts[i][1] === pts[i-1][1]) return 0;
  }
  const dist2 = (a, b) => {
    const dx = a[0] - b[0], dy = a[1] - b[1];
    return dx*dx + dy*dy;
  };
  function solve(arr) {
    const len = arr.length;
    if (len <= 3) {
      let best = Number.MAX_SAFE_INTEGER;
      for (let i = 0; i < len; i++)
        for (let j = i+1; j < len; j++)
          best = Math.min(best, dist2(arr[i], arr[j]));
      arr.sort((a,b)=>a[1]-b[1]);
      return best;
    }
    const mid = len >> 1;
    const midx = arr[mid][0];
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);
    let d = Math.min(solve(left), solve(right));
    const merged = [];
    let i=0,j=0;
    while (i<left.length && j<right.length) {
      if (left[i][1] <= right[j][1]) merged.push(left[i++]); else merged.push(right[j++]);
    }
    while (i<left.length) merged.push(left[i++]);
    while (j<right.length) merged.push(right[j++]);
    arr.splice(0, arr.length, ...merged);
    const strip = [];
    for (const p of arr) {
      const dx = p[0] - midx;
      if (dx*dx < d) strip.push(p);
    }
    for (let s = 0; s < strip.length; s++) {
      for (let t = s+1; t < strip.length && t <= s+7; t++) {
        const dy = strip[t][1] - strip[s][1];
        if (dy*dy >= d) break;
        d = Math.min(d, dist2(strip[s], strip[t]));
      }
    }
    return d;
  }
  return solve(pts);
}
