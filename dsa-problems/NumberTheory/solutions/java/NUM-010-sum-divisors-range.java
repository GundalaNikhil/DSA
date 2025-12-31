import java.util.*;

class Solution {
    static final int MOD = 1000000007;

    public long rangeSigma(int L, int R) {
        long[] sigma = new long[R + 1];
        
        // Sieve-like process to compute sigma for all numbers up to R
        for (int i = 1; i <= R; i++) {
            for (int j = i; j <= R; j += i) {
                sigma[j] += i;
            }
        }
        
        long total = 0;
        for (int i = L; i <= R; i++) {
            total = (total + sigma[i]) % MOD;
        }
        
        return total;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int L = sc.nextInt();
            int R = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.rangeSigma(L, R));
        }
        sc.close();
    }
}
