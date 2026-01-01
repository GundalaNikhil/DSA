import java.util.*;

class Solution {
    private static final long INF = (long)4e18;

    public int minCostWithFreeCells(int[][] cost, int f) {
        int m = cost.length, n = cost[0].length;
        long[][][] dp = new long[m][n][f + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.fill(dp[i][j], INF);
            }
        }

        dp[0][0][0] = cost[0][0];
        if (f > 0) dp[0][0][1] = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                for (int k = 0; k <= f; k++) {
                    long cur = dp[r][c][k];
                    if (cur == INF) continue;

                    // Move Right
                    if (c + 1 < n) {
                        // pay cost
                        dp[r][c + 1][k] = Math.min(dp[r][c + 1][k], cur + cost[r][c + 1]);
                        // free cell
                        if (k + 1 <= f) dp[r][c + 1][k + 1] = Math.min(dp[r][c + 1][k + 1], cur);
                    }
                    // Move Down
                    if (r + 1 < m) {
                        dp[r + 1][c][k] = Math.min(dp[r + 1][c][k], cur + cost[r + 1][c]);
                        if (k + 1 <= f) dp[r + 1][c][k + 1] = Math.min(dp[r + 1][c][k + 1], cur);
                    }
                }
            }
        }

        long ans = INF;
        for (int k = 0; k <= f; k++) ans = Math.min(ans, dp[m - 1][n - 1][k]);
        return (int) ans;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int[][] cost = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cost[i][j] = sc.nextInt();
            }
        }
        int f = sc.nextInt();
        System.out.println(new Solution().minCostWithFreeCells(cost, f));
        sc.close();
    }
}
