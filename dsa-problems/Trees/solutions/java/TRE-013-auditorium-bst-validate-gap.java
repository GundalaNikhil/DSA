import java.util.*;

class Solution {
    public boolean validateBSTGap(int n, long[] values, int[] left, int[] right, long G) {
        if (n == 0) return true;
        return validate(0, Long.MIN_VALUE, Long.MAX_VALUE, values, left, right, G);
    }

    private boolean validate(int u, long min, long max, long[] values, int[] left, int[] right, long G) {
        if (u == -1) return true;

        long val = values[u];
        // BST Check
        if (val <= min || val >= max) return false;

        // Left Child Check
        if (left[u] != -1) {
            long lVal = values[left[u]];
            if (Math.abs(val - lVal) < G) return false; // Gap Check
            if (!validate(left[u], min, val, values, left, right, G)) return false;
        }

        // Right Child Check
        if (right[u] != -1) {
            long rVal = values[right[u]];
            if (Math.abs(val - rVal) < G) return false; // Gap Check
            if (!validate(right[u], val, max, values, left, right, G)) return false;
        }

        return true;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] values = new long[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextLong();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        long G = 0;
        if (sc.hasNextLong()) G = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.validateBSTGap(n, values, left, right, G) ? "true" : "false");
        sc.close();
    }
}
