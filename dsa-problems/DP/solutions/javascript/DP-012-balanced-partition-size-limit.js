class Solution {
  minLargerGroupSize(a, D) {
    const n = a.length;
    const total = a.reduce((s, x) => s + x, 0);
    const dp = Array.from({ length: n + 1 }, () => new Set());
    dp[0].add(0);

    for (const x of a) {
      for (let k = n - 1; k >= 0; k--) {
        for (const s of Array.from(dp[k])) {
          dp[k + 1].add(s + x);
        }
      }
    }

    let ans = Infinity;
    for (let k = 0; k <= n; k++) {
      for (const s of dp[k]) {
        if (Math.abs(total - 2 * s) <= D) {
          ans = Math.min(ans, Math.max(k, n - k));
        }
      }
    }
    return ans === Infinity ? -1 : ans;
  }
}
