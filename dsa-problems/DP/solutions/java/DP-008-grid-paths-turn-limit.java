import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int countPathsWithTurnLimit(int m, int n, int T) {
        if (m == 1 && n == 1) return 1;
        int[][][] dpR = new int[m][n][T + 1];
        int[][][] dpD = new int[m][n][T + 1];

        if (n >= 2) dpR[0][1][0] = 1;
        if (m >= 2) dpD[1][0][0] = 1;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (r == 0 && c == 0) continue;
                if (r == 0 && c == 1) continue;
                if (r == 1 && c == 0) continue;

                for (int t = 0; t <= T; t++) {
                    long vR = 0;
                    if (c - 1 >= 0) {
                        vR += dpR[r][c - 1][t];
                        if (t - 1 >= 0) vR += dpD[r][c - 1][t - 1];
                    }
                    dpR[r][c][t] = (int) (vR % MOD);

                    long vD = 0;
                    if (r - 1 >= 0) {
                        vD += dpD[r - 1][c][t];
                        if (t - 1 >= 0) vD += dpR[r - 1][c][t - 1];
                    }
                    dpD[r][c][t] = (int) (vD % MOD);
                }
            }
        }

        long ans = 0;
        for (int t = 0; t <= T; t++) {
            ans += dpR[m - 1][n - 1][t];
            ans += dpD[m - 1][n - 1][t];
        }
        return (int) (ans % MOD);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int T = sc.nextInt();
        System.out.println(new Solution().countPathsWithTurnLimit(m, n, T));
        sc.close();
    }
}
