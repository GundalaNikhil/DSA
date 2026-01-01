import java.util.*;

class Solution {
    public long maxSumGapThree(long[] a) {
        long dp_i_3 = 0; // dp[i-3]
        long dp_i_2 = 0; // dp[i-2]
        long dp_i_1 = 0; // dp[i-1]

        for (long x : a) {
            long take = x + dp_i_3;
            long skip = dp_i_1;
            long cur = Math.max(skip, take);

            dp_i_3 = dp_i_2;
            dp_i_2 = dp_i_1;
            dp_i_1 = cur;
        }
        return dp_i_1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextLong();
        System.out.println(new Solution().maxSumGapThree(a));
        sc.close();
    }
}
