import java.util.*;

class Solution {
    public long bestStreakWithSmoothing(int[] a) {
        int n = a.length;
        if (n < 3) return 0; // Should not happen per constraints

        long[] maxEndingAt = new long[n];
        long[] globalMaxPrefix = new long[n];

        // Forward Pass
        maxEndingAt[0] = a[0];
        globalMaxPrefix[0] = a[0];
        for (int i = 1; i < n; i++) {
            maxEndingAt[i] = Math.max(a[i], maxEndingAt[i - 1] + a[i]);
            globalMaxPrefix[i] = Math.max(globalMaxPrefix[i - 1], maxEndingAt[i]);
        }

        long[] maxStartingAt = new long[n];
        long[] globalMaxSuffix = new long[n];

        // Backward Pass
        maxStartingAt[n - 1] = a[n - 1];
        globalMaxSuffix[n - 1] = a[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            maxStartingAt[i] = Math.max(a[i], maxStartingAt[i + 1] + a[i]);
            globalMaxSuffix[i] = Math.max(globalMaxSuffix[i + 1], maxStartingAt[i]);
        }

        long ans = Long.MIN_VALUE;

        // Try smoothing each valid i
        for (int i = 1; i <= n - 2; i++) {
            long sum = (long) a[i - 1] + (long) a[i] + (long) a[i + 1];
            long smoothedVal = Math.floorDiv(sum, 3);

            // 1. Check pass-through sum
            long leftPart = Math.max(0, maxEndingAt[i - 1]);
            long rightPart = Math.max(0, maxStartingAt[i + 1]);
            long crossSum = leftPart + smoothedVal + rightPart;

            // 2. Check disjoint sums
            long globalLeft = globalMaxPrefix[i - 1];
            long globalRight = globalMaxSuffix[i + 1];

            long currentBest = Math.max(crossSum, Math.max(globalLeft, globalRight));
            ans = Math.max(ans, currentBest);
        }

        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.bestStreakWithSmoothing(a);
        System.out.println(result);
        sc.close();
    }
}
