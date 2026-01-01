import java.util.*;

class Solution {
    private long[][] memo;

    public long countPaths(int r, int c) {
        memo = new long[r][c];
        for (long[] row : memo) {
            Arrays.fill(row, -1);
        }
        return helper(r - 1, c - 1);
    }

    private long helper(int r, int c) {
        // Base case: Start point
        if (r == 0 && c == 0) return 1;
        
        // Out of bounds
        if (r < 0 || c < 0) return 0;
        
        // Return memoized value
        if (memo[r][c] != -1) return memo[r][c];
        
        // Recursive step
        long paths = helper(r - 1, c) + helper(r, c - 1);
        memo[r][c] = paths;
        return paths;
    }
}





class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countPaths(r, c));
        sc.close();
    }
}
