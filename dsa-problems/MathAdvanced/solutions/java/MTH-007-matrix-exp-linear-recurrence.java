import java.util.*;

class Solution {
    private long MOD;
    private int K;

    private long[][] multiply(long[][] A, long[][] B) {
        long[][] C = new long[K][K];
        for (int i = 0; i < K; i++) {
            for (int k = 0; k < K; k++) {
                if (A[i][k] == 0) continue;
                for (int j = 0; j < K; j++) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    private long[][] power(long[][] A, long exp) {
        long[][] res = new long[K][K];
        for (int i = 0; i < K; i++) res[i][i] = 1;
        
        while (exp > 0) {
            if ((exp & 1) == 1) res = multiply(res, A);
            A = multiply(A, A);
            exp >>= 1;
        }
        return res;
    }

    public long matrix_exp_linear_recurrence(int k, long n, long mod, long[] coeffs, long[] initial) {
        this.MOD = mod;
        this.K = k;
        
        if (n < k) return initial[(int)n];
        
        long[][] T = new long[k][k];
        // Fill first row with coeffs
        for (int j = 0; j < k; j++) {
            T[0][j] = coeffs[j];
        }
        // Fill sub-diagonal with 1s
        for (int i = 1; i < k; i++) {
            T[i][i - 1] = 1;
        }
        
        T = power(T, n - k + 1);
        
        // Result is T * InitialVector
        // InitialVector is [a_{k-1}, a_{k-2}, ..., a_0]^T
        // We only need the first element of the result vector
        long ans = 0;
        for (int j = 0; j < k; j++) {
            // initial[k - 1 - j] corresponds to a_{k-1}, a_{k-2}...
            ans = (ans + T[0][j] * initial[k - 1 - j]) % MOD;
        }
        
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        long n = sc.nextLong();
        long MOD = sc.nextLong();
        
        long[] coeffs = new long[k];
        for (int i = 0; i < k; i++) coeffs[i] = sc.nextLong();
        
        long[] initial = new long[k];
        for (int i = 0; i < k; i++) initial[i] = sc.nextLong();
        
        Solution solution = new Solution();
        System.out.println(solution.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial));
        
        sc.close();
    }
}
