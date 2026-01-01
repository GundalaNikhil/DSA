import java.util.*;

class Solution {
    private int[][][][] memo;
    private int[][] mat;
    private int N, M;

    private int solve(int r1, int r2, int c1, int c2) {
        if (r1 == r2 && c1 == c2) return mat[r1][c1];
        if (memo[r1][r2][c1][c2] != Integer.MIN_VALUE) return memo[r1][r2][c1][c2];

        int movesMade = (N - (r2 - r1 + 1)) + (M - (c2 - c1 + 1));
        boolean isMax = (movesMade % 2 == 0);

        int res;
        if (isMax) {
            res = Integer.MIN_VALUE;
            if (r1 < r2) {
                res = Math.max(res, solve(r1 + 1, r2, c1, c2)); // Remove Top
                res = Math.max(res, solve(r1, r2 - 1, c1, c2)); // Remove Bottom
            }
            if (c1 < c2) {
                res = Math.max(res, solve(r1, r2, c1 + 1, c2)); // Remove Left
                res = Math.max(res, solve(r1, r2, c1, c2 - 1)); // Remove Right
            }
        } else {
            res = Integer.MAX_VALUE;
            if (r1 < r2) {
                res = Math.min(res, solve(r1 + 1, r2, c1, c2));
                res = Math.min(res, solve(r1, r2 - 1, c1, c2));
            }
            if (c1 < c2) {
                res = Math.min(res, solve(r1, r2, c1 + 1, c2));
                res = Math.min(res, solve(r1, r2, c1, c2 - 1));
            }
        }

        return memo[r1][r2][c1][c2] = res;
    }

    public int matrixGame(int n, int m, int[][] matrix) {
        this.N = n;
        this.M = m;
        this.mat = matrix;
        memo = new int[n][n][m][m];
        for (int[][][] row : memo) {
            for (int[][] col : row) {
                for (int[] arr : col) {
                    Arrays.fill(arr, Integer.MIN_VALUE);
                }
            }
        }
        return solve(0, n - 1, 0, m - 1);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] matrix = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    matrix[i][j] = sc.nextInt();
                }
            }

            Solution solution = new Solution();
            System.out.println(solution.matrixGame(n, m, matrix));
        }
        sc.close();
    }
}
