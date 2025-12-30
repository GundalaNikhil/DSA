const MOD = 1000000007;

class Solution {
  countPathsWithTurnLimit(m, n, T) {
    if (m === 1 && n === 1) return 1;
    const dpR = Array.from({ length: m }, () =>
      Array.from({ length: n }, () => new Array(T + 1).fill(0))
    );
    const dpD = Array.from({ length: m }, () =>
      Array.from({ length: n }, () => new Array(T + 1).fill(0))
    );

    if (n >= 2) dpR[0][1][0] = 1;
    if (m >= 2) dpD[1][0][0] = 1;

    for (let r = 0; r < m; r++) {
      for (let c = 0; c < n; c++) {
        if ((r === 0 && c === 0) || (r === 0 && c === 1) || (r === 1 && c === 0)) continue;
        for (let t = 0; t <= T; t++) {
          let vR = 0;
          if (c - 1 >= 0) {
            vR += dpR[r][c - 1][t];
            if (t - 1 >= 0) vR += dpD[r][c - 1][t - 1];
          }
          dpR[r][c][t] = vR % MOD;

          let vD = 0;
          if (r - 1 >= 0) {
            vD += dpD[r - 1][c][t];
            if (t - 1 >= 0) vD += dpR[r - 1][c][t - 1];
          }
          dpD[r][c][t] = vD % MOD;
        }
      }
    }

    let ans = 0;
    for (let t = 0; t <= T; t++) {
      ans = (ans + dpR[m - 1][n - 1][t] + dpD[m - 1][n - 1][t]) % MOD;
    }
    return ans;
  }
}
