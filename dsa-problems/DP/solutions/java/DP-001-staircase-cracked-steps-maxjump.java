import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int countWays(int n, int J, boolean[] cracked) {
        if (cracked[n]) return 0;

        long[] dp = new long[n + 1];
        dp[0] = 1;
        long windowSum = dp[0]; // sum of dp[max(0, i-J) .. i-1] for current i (starts at i=1)

        for (int i = 1; i <= n; i++) {
            // You cannot land on cracked steps.
            if (cracked[i]) {
                dp[i] = 0;
            } else {
                dp[i] = windowSum;
            }

            // Slide window: include dp[i] for future steps.
            windowSum = (windowSum + dp[i]) % MOD;
            int out = i - J;
            if (out >= 0) {
                // Remove the value that is now too old to contribute.
                windowSum = (windowSum - dp[out]) % MOD;
                if (windowSum < 0) windowSum += MOD;
            }
        }
        return (int) (dp[n] % MOD);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int J = sc.nextInt();
        int m = sc.nextInt();
        boolean[] cracked = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            int idx = sc.nextInt();
            if (1 <= idx && idx <= n) cracked[idx] = true;
        }
        System.out.println(new Solution().countWays(n, J, cracked));
        sc.close();
    }
}
