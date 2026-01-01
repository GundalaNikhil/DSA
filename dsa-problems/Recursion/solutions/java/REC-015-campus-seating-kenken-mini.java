import java.util.*;

class Solution {
    public int[][] solveLatinSquare(int n) {
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = ((i + j) % n) + 1;
            }
        }
        return grid;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        
        Solution sol = new Solution();
        int[][] res = sol.solveLatinSquare(n);
        for(int[] row : res) {
            for(int i=0; i<row.length; i++) {
                System.out.print(row[i] + (i==row.length-1?"":" "));
            }
            System.out.println();
        }
        sc.close();
    }
}
