import java.util.*;

class Solution {
    public long maximizeOrWithKPicks(int[] a, int k) {
        int n = a.length;
        // Optimization: 30 bits max. If k >= 30, we can collect all bits.
        if (k >= 30) {
            long totalOr = 0;
            for (int x : a) totalOr |= x;
            return totalOr;
        }

        long currentOr = 0;
        boolean[] used = new boolean[n];

        for (int step = 0; step < k; step++) {
            long bestOr = -1;
            int bestIdx = -1;

            for (int i = 0; i < n; i++) {
                if (!used[i]) {
                    long newOr = currentOr | a[i];
                    if (newOr > bestOr) {
                        bestOr = newOr;
                        bestIdx = i;
                    }
                }
            }

            if (bestIdx != -1) {
                currentOr = bestOr;
                used[bestIdx] = true;
            }
        }
        return currentOr;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maximizeOrWithKPicks(a, k));
        sc.close();
    }
}
