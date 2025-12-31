import java.util.*;

class Solution {
    public double expectedComparisons(int n, int k) {
        double[][] dp = new double[n + 1][n + 1];
        // colSum[k][i] stores sum(dp[j][k] for j=1..i)
        // Note: swapped indices for easier column access: colSum[k][i]
        double[][] colSum = new double[n + 1][n + 1];
        
        // diagSum[d][i] stores sum along diagonal diff d up to row i
        // diff = row - col. Range 0 to n.
        double[][] diagSum = new double[n + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                // Compute dp[i][j] (Size i, Rank j)
                double sum = 0;
                
                // Left subproblems (pivot > j): Sizes j..i-1, Rank j
                // Sum dp[x][j] for x in [j, i-1]
                if (i - 1 >= j) {
                    sum += colSum[j][i - 1] - colSum[j][j - 1];
                }
                
                // Right subproblems (pivot < j): Sizes i-j+1..i-1, Rank 1..j-1
                // Diff = size - rank = (i-p) - (j-p) = i-j.
                // We need sum of dp[x][y] where x-y = i-j and x < i.
                // The terms are E(i-j+1, 1), ..., E(i-1, j-1).
                // Diagonal index d = i - j.
                // We want sum up to row i-1.
                int d = i - j;
                if (j > 1) {
                    sum += diagSum[d][i - 1]; // diagSum accumulates from row 1
                }
                
                dp[i][j] = (i - 1) + sum / i;
                
                // Update sums
                colSum[j][i] = colSum[j][i - 1] + dp[i][j];
                diagSum[i - j][i] = diagSum[i - j][i - 1] + dp[i][j];
            }
        }
        
        return dp[n][k];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.expectedComparisons(n, k));
        }
        sc.close();
    }
}
