import java.util.*;

class Solution {
    int R, C, T;
    Long[][][][] memo;

    public long countPaths(int r, int c, int t) {
        R = r; C = c; T = t;
        // Assume constraints R,C <= 50. T <= R+C?
        memo = new Long[R][C][3][T + 1]; 
        // lastDir: 0=Right, 1=Down, 2=None (-1 mapped to 2)
        return dfs(0, 0, 2, 0);
    }

    private long dfs(int r, int c, int lastDir, int turns) {
        if (r == R - 1 && c == C - 1) return 1;
        if (turns > T) return 0;
        
        if (memo[r][c][lastDir][turns] != null) return memo[r][c][lastDir][turns];

        long count = 0;

        // Dir 0: Right (c+1)
        if (c + 1 < C) {
            int newTurns = turns;
            if (lastDir != 2 && lastDir != 0) newTurns++;
            count += dfs(r, c + 1, 0, newTurns);
        }

        // Dir 1: Down (r+1)
        if (r + 1 < R) {
            int newTurns = turns;
            if (lastDir != 2 && lastDir != 1) newTurns++;
            count += dfs(r + 1, c, 1, newTurns);
        }

        return memo[r][c][lastDir][turns] = count;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int r = sc.nextInt();
        int c = sc.nextInt();
        int T = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.println(sol.countPaths(r, c, T));
        sc.close();
    }
}
