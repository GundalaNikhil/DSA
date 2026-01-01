import java.util.*;

class Solution {
    private long MOD;
    private long G = 3;

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

    private void ntt(long[] a, boolean invert) {
        int n = a.length;
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; (j & bit) != 0; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) {
                long temp = a[i]; a[i] = a[j]; a[j] = temp;
            }
        }
        for (int len = 2; len <= n; len <<= 1) {
            long wlen = power(G, (MOD - 1) / len);
            if (invert) wlen = modInverse(wlen);
            for (int i = 0; i < n; i += len) {
                long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long u = a[i + j];
                    long v = (a[i + j + len / 2] * w) % MOD;
                    a[i + j] = (u + v) % MOD;
                    a[i + j + len / 2] = (u - v + MOD) % MOD;
                    w = (w * wlen) % MOD;
                }
            }
        }
        if (invert) {
            long nInv = modInverse(n);
            for (int i = 0; i < n; i++) a[i] = (a[i] * nInv) % MOD;
        }
    }

    public long[] inversePolynomial(long[] P, int n, long MOD) {
        this.MOD = MOD;
        int size = 1;
        while (size < n) size <<= 1;
        
        long[] a = new long[size];
        System.arraycopy(P, 0, a, 0, Math.min(P.length, size));
        
        long[] b = new long[1];
        b[0] = modInverse(a[0]);
        
        int len = 1;
        while (len < n) {
            len <<= 1;
            int limit = len << 1;
            
            long[] copyA = new long[limit];
            long[] copyB = new long[limit];
            
            System.arraycopy(a, 0, copyA, 0, Math.min(a.length, len));
            System.arraycopy(b, 0, copyB, 0, b.length);
            
            ntt(copyA, false);
            ntt(copyB, false);
            
            for (int i = 0; i < limit; i++) {
                // b_new = b * (2 - a * b)
                long term = (copyA[i] * copyB[i]) % MOD;
                copyB[i] = (copyB[i] * (2 - term + MOD)) % MOD;
            }
            
            ntt(copyB, true);
            
            b = new long[len];
            System.arraycopy(copyB, 0, b, 0, len);
        }
        
        long[] res = new long[n];
        System.arraycopy(b, 0, res, 0, n);
        return res;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        int n = sc.nextInt();
        long[] P = new long[k];
        for (int i = 0; i < k; i++) P[i] = sc.nextLong();
        long MOD = sc.nextLong();

        Solution solution = new Solution();
        long[] result = solution.inversePolynomial(P, n, MOD);

        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i < result.length - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
