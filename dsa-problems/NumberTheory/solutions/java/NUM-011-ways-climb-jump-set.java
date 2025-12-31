import java.util.*;

class Solution {
    static final int MOD = 1000000007;

    public int countWays(int n, int[] jumps) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        
        for (int i = 1; i <= n; i++) {
            for (int jump : jumps) {
                if (i >= jump) {
                    dp[i] = (dp[i] + dp[i - jump]) % MOD;
                }
            }
        }
        
        return dp[n];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] jumps = new int[m];
            for (int i = 0; i < m; i++) jumps[i] = sc.nextInt();

            Solution solution = new Solution();
            System.out.println(solution.countWays(n, jumps));
        }
        sc.close();
    }
}
