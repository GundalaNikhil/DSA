import java.util.*;

class Solution {
    long maxDiameter = 0;

    public long weightedDiameter(int n, int[] left, int[] right, long[] lw, long[] rw) {
        if (n == 0) return 0;
        maxDiameter = 0;
        dfs(0, left, right, lw, rw);
        return maxDiameter;
    }

    private long dfs(int u, int[] left, int[] right, long[] lw, long[] rw) {
        if (u == -1) return 0;

        long lPath = 0;
        long rPath = 0;

        if (left[u] != -1) {
            lPath = lw[u] + dfs(left[u], left, right, lw, rw);
        }
        if (right[u] != -1) {
            rPath = rw[u] + dfs(right[u], left, right, lw, rw);
        }

        maxDiameter = Math.max(maxDiameter, lPath + rPath);

        return Math.max(lPath, rPath);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] left = new int[n];
        int[] right = new int[n];
        long[] lw = new long[n];
        long[] rw = new long[n];
        for (int i = 0; i < n; i++) {
            int val = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
            lw[i] = sc.nextLong();
            rw[i] = sc.nextLong();
        }

        Solution solution = new Solution();
        System.out.println(solution.weightedDiameter(n, left, right, lw, rw));
        sc.close();
    }
}
