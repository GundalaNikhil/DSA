function classifyPoint(xs, ys, qx, qy) {
  const n = xs.length;
  let wn = 0;
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n;
    const xi = xs[i], yi = ys[i], xj = xs[j], yj = ys[j];
    const cross = (xj - xi) * (qy - yi) - (yj - yi) * (qx - xi);
    if (cross === 0 && Math.min(xi, xj) <= qx && qx <= Math.max(xi, xj) && Math.min(yi, yj) <= qy && qy <= Math.max(yi, yj)) {
      return "boundary";
    }
    if (yi <= qy && yj > qy && cross > 0) wn++;
    else if (yi > qy && yj <= qy && cross < 0) wn--;
  }
  return wn !== 0 ? "inside" : "outside";
}
