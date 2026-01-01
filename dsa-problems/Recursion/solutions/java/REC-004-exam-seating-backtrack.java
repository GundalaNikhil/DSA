import java.util.*;

class Solution {
    int count = 0;
    int N;
    boolean[] cols;
    boolean[] diag1;
    boolean[] diag2;

    public int countNQueens(int n) {
        N = n;
        count = 0;
        cols = new boolean[2 * n];
        diag1 = new boolean[2 * n]; // row + col
        diag2 = new boolean[2 * n]; // row - col + N
        backtrack(0);
        return count;
    }

    private void backtrack(int row) {
        if (row == N) {
            count++;
            return;
        }

        for (int col = 0; col < N; col++) {
            if (cols[col] || diag1[row + col] || diag2[row - col + N]) continue;

            cols[col] = true;
            diag1[row + col] = true;
            diag2[row - col + N] = true;

            backtrack(row + 1);

            cols[col] = false;
            diag1[row + col] = false;
            diag2[row - col + N] = false;
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.println(sol.countNQueens(n));
        sc.close();
    }
}
