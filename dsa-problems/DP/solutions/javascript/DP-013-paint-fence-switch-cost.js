function minCost(n, k, s) {
  if (k === 1) return n <= 2 ? n : -1;
  const INF = BigInt(4e18);
  let dp1 = Array(k).fill(1n);
  let dp2 = Array(k).fill(INF);
  for (let i = 1; i < n; i++) {
    let min1 = INF, min2 = INF, c1 = -1;
    for (let c = 0; c < k; c++) {
      const v = dp1[c] < dp2[c] ? dp1[c] : dp2[c];
      if (v < min1) { min2 = min1; min1 = v; c1 = c; }
      else if (v < min2) { min2 = v; }
    }
    const ndp1 = Array(k).fill(INF);
    const ndp2 = Array(k).fill(INF);
    for (let c = 0; c < k; c++) {
      if (dp1[c] < INF) ndp2[c] = dp1[c] + 1n;
      const bestOther = c === c1 ? min2 : min1;
      if (bestOther < INF) ndp1[c] = bestOther + 1n + BigInt(s[i]);
    }
    dp1 = ndp1; dp2 = ndp2;
  }
  let ans = dp1.concat(dp2).reduce((a, b) => (a < b ? a : b), INF);
  return ans >= INF ? -1 : Number(ans);
}
