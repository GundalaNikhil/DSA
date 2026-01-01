import java.util.*;

class Solution {
    static class Result {
        int height;
        long weight;
        boolean balanced;

        Result(int h, long w, boolean b) {
            this.height = h;
            this.weight = w;
            this.balanced = b;
        }
    }

    public boolean isBalancedWeighted(int n, long[] weight, int[] left, int[] right, long W) {
        if (n == 0) return true;
        return dfs(0, weight, left, right, W).balanced;
    }

    private Result dfs(int u, long[] weight, int[] left, int[] right, long W) {
        if (u == -1) return new Result(0, 0, true);

        Result l = dfs(left[u], weight, left, right, W);
        if (!l.balanced) return new Result(0, 0, false); // Optimization: propagate failure

        Result r = dfs(right[u], weight, left, right, W);
        if (!r.balanced) return new Result(0, 0, false);

        boolean hBal = Math.abs(l.height - r.height) <= 1;
        boolean wBal = Math.abs(l.weight - r.weight) <= W;

        if (hBal && wBal) {
            return new Result(Math.max(l.height, r.height) + 1, l.weight + r.weight + weight[u], true);
        } else {
            return new Result(0, 0, false);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] weight = new long[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            weight[i] = sc.nextLong();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        long W = 0;
        if (sc.hasNextLong()) W = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.isBalancedWeighted(n, weight, left, right, W) ? "true" : "false");
        sc.close();
    }
}
