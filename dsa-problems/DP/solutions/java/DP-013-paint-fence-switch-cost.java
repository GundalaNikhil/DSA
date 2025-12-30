import java.util.*;

class Solution {
    public long minCost(int n, int k, int[] s) {
        if (k == 1) return n <= 2 ? n : -1;
        final long INF = (long)4e18;
        long[] dp1 = new long[k];
        long[] dp2 = new long[k];
        Arrays.fill(dp1, 1);
        Arrays.fill(dp2, INF);

        for (int i = 1; i < n; i++) {
            long min1 = INF, min2 = INF;
            int c1 = -1;
            for (int c = 0; c < k; c++) {
                long v = Math.min(dp1[c], dp2[c]);
                if (v < min1) { min2 = min1; min1 = v; c1 = c; }
                else if (v < min2) { min2 = v; }
            }
            long[] ndp1 = new long[k];
            long[] ndp2 = new long[k];
            Arrays.fill(ndp1, INF);
            Arrays.fill(ndp2, INF);
            for (int c = 0; c < k; c++) {
                if (dp1[c] < INF) ndp2[c] = dp1[c] + 1; // extend streak
                long bestOther = (c == c1) ? min2 : min1;
                if (bestOther < INF) ndp1[c] = bestOther + 1 + s[i];
            }
            dp1 = ndp1; dp2 = ndp2;
        }
        long ans = INF;
        for (int c = 0; c < k; c++) ans = Math.min(ans, Math.min(dp1[c], dp2[c]));
        return ans >= INF ? -1 : ans;
    }
}
