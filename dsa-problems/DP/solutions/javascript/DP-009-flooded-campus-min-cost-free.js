class Solution {
  minCostWithFreeCells(cost, f) {
    const m = cost.length, n = cost[0].length;
    const INF = 4e18;
    const dp = Array.from({ length: m }, () =>
      Array.from({ length: n }, () => new Array(f + 1).fill(INF))
    );
    dp[0][0][0] = cost[0][0];
    if (f > 0) dp[0][0][1] = 0;

    for (let r = 0; r < m; r++) {
      for (let c = 0; c < n; c++) {
        for (let k = 0; k <= f; k++) {
          const cur = dp[r][c][k];
          if (cur >= INF) continue;
          if (c + 1 < n) {
            dp[r][c + 1][k] = Math.min(dp[r][c + 1][k], cur + cost[r][c + 1]);
            if (k + 1 <= f) dp[r][c + 1][k + 1] = Math.min(dp[r][c + 1][k + 1], cur);
          }
          if (r + 1 < m) {
            dp[r + 1][c][k] = Math.min(dp[r + 1][c][k], cur + cost[r + 1][c]);
            if (k + 1 <= f) dp[r + 1][c][k + 1] = Math.min(dp[r + 1][c][k + 1], cur);
          }
        }
      }
    }

    let ans = INF;
    for (let k = 0; k <= f; k++) ans = Math.min(ans, dp[m - 1][n - 1][k]);
    return ans;
  }
}
