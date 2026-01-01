import java.util.*;

class Solution {
    private long power(long base, long exp, long mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }

    private long modInverse(long n, long mod) {
        return power(n, mod - 2, mod);
    }

    private void ntt(long[] a, boolean invert, long mod, long g) {
        int n = a.length;
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; (j & bit) != 0; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) {
                long temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
        
        for (int len = 2; len <= n; len <<= 1) {
            long wlen = power(g, (mod - 1) / len, mod);
            if (invert) wlen = modInverse(wlen, mod);
            for (int i = 0; i < n; i += len) {
                long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long u = a[i + j];
                    long v = (a[i + j + len / 2] * w) % mod;
                    a[i + j] = (u + v) % mod;
                    a[i + j + len / 2] = (u - v + mod) % mod;
                    w = (w * wlen) % mod;
                }
            }
        }
        
        if (invert) {
            long nInv = modInverse(n, mod);
            for (int i = 0; i < n; i++) a[i] = (a[i] * nInv) % mod;
        }
    }

    private long[] convolve(long[] A, long[] B, long mod, long g) {
        int size = 1;
        while (size < A.length + B.length) size <<= 1;
        
        long[] fa = Arrays.copyOf(A, size);
        long[] fb = Arrays.copyOf(B, size);
        
        ntt(fa, false, mod, g);
        ntt(fb, false, mod, g);
        
        for (int i = 0; i < size; i++) fa[i] = (fa[i] * fb[i]) % mod;
        
        ntt(fa, true, mod, g);
        return fa;
    }

    public long[] convolution_multi_mod_crt(int n, int m, long[] A, long[] B, long targetMod) {
        long P1 = 998244353, G1 = 3;
        long P2 = 1004535809, G2 = 3;
        long P3 = 469762049, G3 = 3;
        
        long[] c1 = convolve(A, B, P1, G1);
        long[] c2 = convolve(A, B, P2, G2);
        long[] c3 = convolve(A, B, P3, G3);
        
        int len = n + m - 1;
        long[] res = new long[len];
        
        long P1_inv_P2 = modInverse(P1, P2);
        long P1P2_inv_P3 = modInverse((P1 * P2) % P3, P3);
        
        for (int i = 0; i < len; i++) {
            long a1 = c1[i];
            long a2 = c2[i];
            long a3 = c3[i];
            
            long x1 = a1;
            long x2 = ((a2 - x1 + P2) % P2 * P1_inv_P2) % P2;
            long x3 = ((a3 - x1) % P3 + P3) % P3;
            x3 = (x3 - (x2 * P1) % P3 + P3) % P3;
            x3 = (x3 * P1P2_inv_P3) % P3;
            
            // Result = x1 + x2*P1 + x3*P1*P2
            long ans = (x1 + x2 * P1) % targetMod;
            ans = (ans + (x3 * ((P1 * P2) % targetMod)) % targetMod) % targetMod;
            res[i] = ans;
        }
        
        return res;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();
        
        long[] B = new long[m];
        for (int i = 0; i < m; i++) B[i] = sc.nextLong();
        
        long MOD = sc.nextLong();
        
        Solution solution = new Solution();
        long[] res = solution.convolution_multi_mod_crt(n, m, A, B, MOD);
        
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + (i < res.length - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
