function polygonArea(xs, ys) {
  const n = xs.length;
  let sum = 0n;
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n;
    sum += BigInt(xs[i]) * BigInt(ys[j]) - BigInt(xs[j]) * BigInt(ys[i]);
  }
  const absSum = sum < 0n ? -sum : sum;
  return absSum / 2n;
}
