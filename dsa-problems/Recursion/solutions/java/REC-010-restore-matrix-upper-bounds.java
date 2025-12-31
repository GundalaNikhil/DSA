import java.util.*;

class Solution {
    public int[][] restoreMatrix(int[] rowSums, int[] colSums, int[][] bounds) {
        int r = rowSums.length;
        int c = colSums.length;
        int[][] matrix = new int[r][c];
        
        if (backtrack(0, 0, rowSums, colSums, bounds, matrix)) {
            return matrix;
        }
        return new int[0][0];
    }

    private boolean backtrack(int i, int j, int[] rowSums, int[] colSums, int[][] bounds, int[][] matrix) {
        int R = rowSums.length;
        int C = colSums.length;

        if (i == R) {
            // Check if all colSums are 0 (should be guaranteed if logic is correct)
            for (int val : colSums) if (val != 0) return false;
            return true;
        }

        int nextI = (j == C - 1) ? i + 1 : i;
        int nextJ = (j == C - 1) ? 0 : j + 1;

        // Determine range for matrix[i][j]
        // Must be <= bounds[i][j]
        // Must be <= rowSums[i]
        // Must be <= colSums[j]
        int maxVal = Math.min(bounds[i][j], Math.min(rowSums[i], colSums[j]));
        
        // Optimization: If last column, value is fixed
        if (j == C - 1) {
            int val = rowSums[i]; // Must use all remaining row sum
            if (val > maxVal || val < 0) return false; // Invalid
            
            matrix[i][j] = val;
            rowSums[i] -= val;
            colSums[j] -= val;
            
            if (backtrack(nextI, nextJ, rowSums, colSums, bounds, matrix)) return true;
            
            rowSums[i] += val;
            colSums[j] += val;
            return false;
        }

        // Try values from maxVal down to 0
        for (int val = maxVal; val >= 0; val--) {
            matrix[i][j] = val;
            rowSums[i] -= val;
            colSums[j] -= val;

            if (backtrack(nextI, nextJ, rowSums, colSums, bounds, matrix)) return true;

            rowSums[i] += val;
            colSums[j] += val;
        }

        return false;
    }
}
