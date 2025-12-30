import java.util.*;

class Solution {
    static final int MOD = 1000000007;

    private long power(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }

    public long countSurjections(int n, int k) {
        if (k > n) return 0;
        
        long ans = 0;
        long[][] C = new long[k + 1][k + 1];
        
        // Compute Binomial Coefficients
        for (int i = 0; i <= k; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }
        
        for (int i = 0; i <= k; i++) {
            long term = (C[k][i] * power(k - i, n)) % MOD;
            if (i % 2 == 1) {
                ans = (ans - term + MOD) % MOD;
            } else {
                ans = (ans + term) % MOD;
            }
        }
        
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.countSurjections(n, k));
        }
        sc.close();
    }
}
