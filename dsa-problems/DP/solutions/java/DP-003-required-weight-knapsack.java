import java.util.*;

class Solution {
    private static final long NEG = Long.MIN_VALUE / 4;

    public long maxValueWithRequiredWeight(int n, int W, int R, int[] w, long[] v) {
        long[] dp = new long[W + 1];
        Arrays.fill(dp, NEG);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            int wi = w[i];
            long vi = v[i];
            for (int wt = W; wt >= wi; wt--) {
                if (dp[wt - wi] != NEG) {
                    dp[wt] = Math.max(dp[wt], dp[wt - wi] + vi);
                }
            }
        }

        long ans = NEG;
        for (int wt = R; wt <= W; wt++) ans = Math.max(ans, dp[wt]);
        return ans == NEG ? -1 : ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int W = sc.nextInt();
        int R = sc.nextInt();
        int[] w = new int[n];
        long[] v = new long[n];
        for (int i = 0; i < n; i++) {
            w[i] = sc.nextInt();
            v[i] = sc.nextLong();
        }
        System.out.println(new Solution().maxValueWithRequiredWeight(n, W, R, w, v));
        sc.close();
    }
}
