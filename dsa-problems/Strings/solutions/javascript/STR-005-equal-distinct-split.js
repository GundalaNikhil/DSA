function countEqualDistinctSplits(s) {
  const n = s.length;
  if (n < 2) return 0;

  // Build suffix distinct counts
  const suffixDistinct = new Array(n + 1).fill(0);
  const charSet = new Set();
  for (let i = n - 1; i >= 0; i--) {
    charSet.add(s[i]);
    suffixDistinct[i] = charSet.size;
  }

  // Scan left and compare
  const leftSet = new Set();
  let count = 0;
  for (let i = 0; i < n - 1; i++) {
    leftSet.add(s[i]);
    if (leftSet.size === suffixDistinct[i + 1]) {
      count++;
    }
  }

  return count;
}
