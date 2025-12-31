function diameterSquared(xs, ys) {
  const n = xs.length;
  const cross = (a, b, c) =>
    (xs[b]-xs[a]) * (ys[c]-ys[a]) - (ys[b]-ys[a]) * (xs[c]-xs[a]);
  const dist2 = (a, b) => {
    const dx = xs[a]-xs[b], dy = ys[a]-ys[b];
    return dx*dx + dy*dy;
  };
  let best = 0;
  let j = 1;
  for (let i = 0; i < n; i++) {
    const ni = (i + 1) % n;
    while (cross(i, ni, (j + 1) % n) > cross(i, ni, j)) j = (j + 1) % n;
    best = Math.max(best, dist2(i, j), dist2(ni, j));
  }
  return best;
}
