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

    public long[][] invert_vandermonde(int n, long mod, long[] x) {
        this.MOD = mod;
        
        // 1. Compute P(x) = product(x - x_k)
        // P has degree n, so n+1 coefficients.
        long[] P = new long[n + 1];
        P[0] = 1; // Highest degree term coeff (monic)
        // Let's stick to P[0] is x^0, P[n] is x^n.
        // Initially P(x) = 1 (degree 0). P[0]=1.
        
        // (c0 + c1 x + ...) * ( -xk + x )
        // New c_i = c_{i-1} - xk * c_i
        
        Arrays.fill(P, 0);
        P[0] = 1;
        
        for (int k = 0; k < n; k++) {
            // Multiply by (x - x_k)
            // Shift right (multiply by x) and subtract x_k * P
            for (int i = k + 1; i >= 1; i--) {
                P[i] = (P[i - 1] - x[k] * P[i] % MOD + MOD) % MOD;
            }
            P[0] = (MOD - x[k] * P[0] % MOD) % MOD;
        }
        
        long[][] inv = new long[n][n];
        
        for (int i = 0; i < n; i++) {
            // 2. Compute w_i
            long prod = 1;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                prod = (prod * (x[i] - x[j] + MOD)) % MOD;
            }
            long w = modInverse(prod);
            
            // 3. Compute Q(x) = P(x) / (x - x_i)
            // Synthetic division of P by (x - x_i)
            // P(x) = Q(x) * (x - x_i)
            // Let Q(x) = q_0 + ... + q_{n-1} x^{n-1}
            // Coeff of x^n in P is 1. Coeff of x^n in Q*(x-xi) is q_{n-1}. So q_{n-1} = 1.
            // Generally, P[k] = q_{k-1} - x_i * q_k
            // So q_{k-1} = P[k] + x_i * q_k
            
            long q_k = 0; // Represents q_n (which is 0)
            // We iterate from highest degree n down to 1
            for (int k = n; k >= 1; k--) {
                // q_{k-1} corresponds to coeff of x^{k-1}
                long val = (P[k] + x[i] * q_k) % MOD;
                q_k = val;
                
                // Store in column i, row k-1
                // inv[row][col]
                inv[k - 1][i] = (val * w) % MOD;
            }
        }
        
        return inv;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long MOD = sc.nextLong();
        
        long[] x = new long[n];
        for (int i = 0; i < n; i++) x[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[][] res = solution.invert_vandermonde(n, MOD, x);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(res[i][j] + (j < n - 1 ? " " : ""));
            }
            System.out.println();
        }
        sc.close();
    }
}
