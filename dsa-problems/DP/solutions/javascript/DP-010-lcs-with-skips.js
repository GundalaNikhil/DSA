class Solution {
  lcsWithSkipLimit(a, b, s) {
    const n = a.length,
      m = b.length;
    let prev = new Array(m + 1).fill(0);
    let cur = new Array(m + 1).fill(0);

    for (let i = 1; i <= n; i++) {
      cur[0] = 0;
      const ai = a[i - 1];
      for (let j = 1; j <= m; j++) {
        if (ai === b[j - 1]) cur[j] = prev[j - 1] + 1;
        else cur[j] = Math.max(prev[j], cur[j - 1]);
      }
      const tmp = prev;
      prev = cur;
      cur = tmp;
    }

    const L = prev[m];
    return n - L <= s ? L : -1;
  }
}
