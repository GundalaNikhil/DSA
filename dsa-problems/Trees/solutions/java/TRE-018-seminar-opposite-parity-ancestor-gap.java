import java.util.*;

class Solution {
    long maxDiff = 0;

    public long maxOppositeParityGap(int n, int[] values, int[] left, int[] right) {
        if (n == 0) return 0;
        maxDiff = 0;
        // Use null or special value to indicate "no ancestor".
        // Since values are int, we can use Long.MIN_VALUE/MAX_VALUE but need to be careful with logic.
        // Better: pass initialized flags or use objects.
        // Or simpler: root is depth 0. It sets the initial Even bounds.
        // Odd bounds are initially "empty".
        
        dfs(0, 0, values[0], values[0], Integer.MAX_VALUE, Integer.MIN_VALUE, values, left, right);
        return maxDiff;
    }

    // minE/maxE are valid because root is even.
    // minO/maxO might be invalid (sentinels).
    private void dfs(int u, int depth, int minE, int maxE, int minO, int maxO, int[] values, int[] left, int[] right) {
        if (u == -1) return;

        int val = values[u];

        if (depth % 2 == 0) {
            // Current is Even. Compare with Odd ancestors.
            if (minO != Integer.MAX_VALUE) {
                maxDiff = Math.max(maxDiff, Math.abs((long)val - minO));
                maxDiff = Math.max(maxDiff, Math.abs((long)val - maxO));
            }
            // Update Even bounds for children
            minE = Math.min(minE, val);
            maxE = Math.max(maxE, val);
        } else {
            // Current is Odd. Compare with Even ancestors.
            // Even ancestors always exist (root).
            maxDiff = Math.max(maxDiff, Math.abs((long)val - minE));
            maxDiff = Math.max(maxDiff, Math.abs((long)val - maxE));
            
            // Update Odd bounds for children
            minO = Math.min(minO, val);
            maxO = Math.max(maxO, val);
        }

        if (left[u] != -1) dfs(left[u], depth + 1, minE, maxE, minO, maxO, values, left, right);
        if (right[u] != -1) dfs(right[u], depth + 1, minE, maxE, minO, maxO, values, left, right);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxOppositeParityGap(n, values, left, right));
        sc.close();
    }
}
