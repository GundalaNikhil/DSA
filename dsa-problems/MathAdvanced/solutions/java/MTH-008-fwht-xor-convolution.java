import java.util.*;

class Solution {
    private long MOD = 1000000007;

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

    private void fwht(long[] a, boolean invert) {
        int n = a.length;
        for (int len = 1; len < n; len <<= 1) {
            for (int i = 0; i < n; i += 2 * len) {
                for (int j = 0; j < len; j++) {
                    long u = a[i + j];
                    long v = a[i + j + len];
                    a[i + j] = (u + v) % MOD;
                    a[i + j + len] = (u - v + MOD) % MOD;
                }
            }
        }
        
        if (invert) {
            long invN = modInverse(n);
            for (int i = 0; i < n; i++) {
                a[i] = (a[i] * invN) % MOD;
            }
        }
    }

    public long[] fwht_xor_convolution(int k, long[] A, long[] B) {
        int n = 1 << k;
        
        fwht(A, false);
        fwht(B, false);
        
        long[] C = new long[n];
        for (int i = 0; i < n; i++) {
            C[i] = (A[i] * B[i]) % MOD;
        }
        
        fwht(C, true);
        return C;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        int n = 1 << k;
        
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();
        
        long[] B = new long[n];
        for (int i = 0; i < n; i++) B[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[] res = solution.fwht_xor_convolution(k, A, B);
        
        for (int i = 0; i < n; i++) {
            System.out.print(res[i] + (i < n - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
