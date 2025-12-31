import java.util.*;

class Solution {
    private long MOD;

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

    private long modInverse(long n) {
        return power(n, MOD - 2);
    }

    public long lagrange_interpolation_mod(int k, long X, long MOD, long[][] points) {
        this.MOD = MOD;
        long ans = 0;
        
        for (int i = 0; i < k; i++) {
            long xi = points[i][0];
            long yi = points[i][1];
            
            long num = 1;
            long den = 1;
            
            for (int j = 0; j < k; j++) {
                if (i == j) continue;
                long xj = points[j][0];
                
                num = (num * (X - xj + MOD)) % MOD;
                den = (den * (xi - xj + MOD)) % MOD;
            }
            
            long term = (yi * num) % MOD;
            term = (term * modInverse(den)) % MOD;
            ans = (ans + term) % MOD;
        }
        
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        long X = sc.nextLong();
        long MOD = sc.nextLong();
        
        long[][] points = new long[k][2];
        for (int i = 0; i < k; i++) {
            points[i][0] = sc.nextLong();
            points[i][1] = sc.nextLong();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.lagrange_interpolation_mod(k, X, MOD, points));
        
        sc.close();
    }
}
