import java.util.*;

class Solution {
    public long minPlanksForRoof(int[] height) {
        int n = height.length;
        if (n == 0) return 0;

        long[] L = new long[n];
        long[] SumL = new long[n];

        L[0] = height[0];
        SumL[0] = height[0];
        for (int i = 1; i < n; i++) {
            L[i] = Math.max(height[i], L[i - 1]);
            SumL[i] = SumL[i - 1] + L[i];
        }

        long[] R = new long[n];
        long[] SumR = new long[n];

        R[n - 1] = height[n - 1];
        SumR[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            R[i] = Math.max(height[i], R[i + 1]);
            SumR[i] = SumR[i + 1] + R[i];
        }

        long minTotalHeight = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            long currentTotal = SumL[i] + SumR[i] - Math.min(L[i], R[i]);
            minTotalHeight = Math.min(minTotalHeight, currentTotal);
        }

        long originalSum = 0;
        for (int h : height) originalSum += h;

        return minTotalHeight - originalSum;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] height = new int[n];
        for (int i = 0; i < n; i++) height[i] = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.minPlanksForRoof(height);
        System.out.println(result);
        sc.close();
    }
}
