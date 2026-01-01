import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int countExpressions(String s, int M, int K, int L) {
        int n = s.length();
        if (L <= 0 || M <= 0 || K < 0 || K >= M) {
            return 0;
        }
        int[][][] dp = new int[n + 1][M][2];

        for (int len = 1; len <= L && len <= n; len++) {
            if (s.charAt(0) == '0' && len > 1) break;
            int val = Integer.parseInt(s.substring(0, len)) % M;
            dp[len][val][0] = (dp[len][val][0] + 1) % MOD;
        }

        for (int pos = 1; pos < n; pos++) {
            for (int rem = 0; rem < M; rem++) {
                for (int used = 0; used <= 1; used++) {
                    int ways = dp[pos][rem][used];
                    if (ways == 0) continue;
                    for (int len = 1; len <= L && pos + len <= n; len++) {
                        if (s.charAt(pos) == '0' && len > 1) break;
                        int val = Integer.parseInt(s.substring(pos, pos + len));
                        int addRem = (int)(((rem + val) % M + M) % M);
                        int subRem = (int)(((rem - val) % M + M) % M);

                        dp[pos + len][addRem][used] = (int)((dp[pos + len][addRem][used] + (long)ways) % MOD);
                        dp[pos + len][subRem][1] = (int)((dp[pos + len][subRem][1] + (long)ways) % MOD);
                    }
                }
            }
        }

        return dp[n][K][1];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();
        int M = sc.nextInt(), K = sc.nextInt(), L = sc.nextInt();
        System.out.println(new Solution().countExpressions(s, M, K, L));
        sc.close();
    }
}
