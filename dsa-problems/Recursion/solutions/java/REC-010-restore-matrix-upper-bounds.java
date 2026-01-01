import java.util.*;

class Solution {
    public int[][] restoreMatrix(int[] rowSums, int[] colSums) {
        int r = rowSums.length;
        int c = colSums.length;
        int[][] matrix = new int[r][c];

        if (backtrack(0, 0, rowSums, colSums, matrix)) {
            return matrix;
        }
        return new int[0][0];
    }

    private boolean backtrack(int i, int j, int[] rowSums, int[] colSums, int[][] matrix) {
        int R = rowSums.length;
        int C = colSums.length;

        if (i == R) {
            // Check if all colSums are 0 (should be guaranteed if logic is correct)
            for (int val : colSums) if (val != 0) return false;
            return true;
        }

        int nextI = (j == C - 1) ? i + 1 : i;
        int nextJ = (j == C - 1) ? 0 : j + 1;

        // Optimization: If last column, value is fixed
        if (j == C - 1) {
            int val = rowSums[i]; // Must use all remaining row sum
            if (val < 0 || val > colSums[j]) return false;
            
            matrix[i][j] = val;
            rowSums[i] -= val;
            colSums[j] -= val;
            
            if (backtrack(nextI, nextJ, rowSums, colSums, matrix)) return true;
            
            rowSums[i] += val;
            colSums[j] += val;
            return false;
        }

        int maxVal = Math.min(rowSums[i], colSums[j]);

        // Try values from maxVal down to 0
        for (int val = maxVal; val >= 0; val--) {
            matrix[i][j] = val;
            rowSums[i] -= val;
            colSums[j] -= val;

            if (backtrack(nextI, nextJ, rowSums, colSums, matrix)) return true;

            rowSums[i] += val;
            colSums[j] += val;
        }

        return false;
    }
}





class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int R = sc.nextInt();
        int C = sc.nextInt();
        int[] rowSums = new int[R];
        int[] colSums = new int[C];
        for (int i = 0; i < R; i++) rowSums[i] = sc.nextInt();
        for (int i = 0; i < C; i++) colSums[i] = sc.nextInt();
        Solution sol = new Solution();
        int[][] res = sol.restoreMatrix(rowSums, colSums);
        if (res.length == 0) {
            System.out.println("IMPOSSIBLE");
        } else {
            for (int i = 0; i < res.length; i++) {
                for (int j = 0; j < res[i].length; j++) {
                    System.out.print(res[i][j]);
                    if (j + 1 < res[i].length) System.out.print(" ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
