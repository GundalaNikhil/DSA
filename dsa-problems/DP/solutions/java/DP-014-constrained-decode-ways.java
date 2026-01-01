import java.util.*;

class Solution {
    static final long MOD = 1_000_000_007L;

    public long decodeWays(String s) {
        int n = s.length();
        if (n == 0 || s.charAt(0) == '0') return 0;
        long prev2 = 1, prev1 = 1;
        for (int i = 1; i < n; i++) {
            char c = s.charAt(i);
            int pair = (s.charAt(i - 1) - '0') * 10 + (c - '0');
            long cur = 0;
            if (c != '0') {
                cur = (cur + prev1) % MOD;
                if (pair == 20 || (pair > 10 && pair <= 26)) cur = (cur + prev2) % MOD;
            } else {
                if (pair == 20) cur = (cur + prev2) % MOD;
            }
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1 % MOD;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        Solution sol = new Solution();
        System.out.println(sol.decodeWays(s));
        sc.close();
    }
}
