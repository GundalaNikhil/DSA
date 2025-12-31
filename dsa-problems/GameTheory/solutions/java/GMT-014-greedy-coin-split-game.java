import java.util.*;

class Solution {
    private int[][] dp;
    private int[] prefixSum;
    private boolean[][] visited;

    private int getSum(int i, int j) {
        return prefixSum[j + 1] - prefixSum[i];
    }

    private int solve(int i, int j) {
        if (i == j) return 0;
        if (visited[i][j]) return dp[i][j];

        int maxDiff = Integer.MIN_VALUE;

        for (int k = i; k < j; k++) {
            // Split into [i...k] and [k+1...j]
            int sumLeft = getSum(i, k);
            int sumRight = getSum(k + 1, j);

            // If Chooser takes Left: Splitter gets -(sumLeft + solve(k+1, j))
            int valTakeLeft = -sumLeft - solve(k + 1, j);
            
            // If Chooser takes Right: Splitter gets -(sumRight + solve(i, k))
            int valTakeRight = -sumRight - solve(i, k);

            // Chooser minimizes Splitter's gain
            int outcome = Math.min(valTakeLeft, valTakeRight);
            maxDiff = Math.max(maxDiff, outcome);
        }

        visited[i][j] = true;
        dp[i][j] = maxDiff;
        return maxDiff;
    }

    public int coinSplit(int n, int[] A) {
        dp = new int[n][n];
        visited = new boolean[n][n];
        prefixSum = new int[n + 1];
        for (int i = 0; i < n; i++) prefixSum[i + 1] = prefixSum[i] + A[i];

        return solve(0, n - 1);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] A = new int[n];
            for (int i = 0; i < n; i++) {
                A[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.coinSplit(n, A));
        }
        sc.close();
    }
}
