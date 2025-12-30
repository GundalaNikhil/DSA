import java.util.*;

class Solution {
    public double streakProbability(int n, int k) {
        if (k > n) return 0.0;

        // dp[i] = number of sequences of length i with NO streak of k heads
        long[] dp = new long[n + 1];

        // Base cases
        for (int i = 0; i < k; i++) {
            dp[i] = 1L << i; // 2^i
        }
        dp[k] = (1L << k) - 1; // 2^k - 1 (exclude H...H)

        for (int i = k + 1; i <= n; i++) {
            // dp[i] = 2 * dp[i-1] - dp[i-k-1]
            // We subtract cases ending in T H...H (k times)
            // The prefix must be valid of length i - (k+1)
            dp[i] = 2 * dp[i - 1] - dp[i - k - 1];
        }

        long total = 1L << n;
        long valid = dp[n];
        return 1.0 - (double)valid / total;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.streakProbability(n, k));
        }
        sc.close();
    }
}
