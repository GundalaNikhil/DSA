import java.util.*;

class Solution {
    private static final long MOD = 998244353;
    private static final long G = 3;

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
            for (; j & bit; bit >>= 1) j ^= bit;
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
            for (int i = 0; i < n; i++) {
                a[i] = (a[i] * nInv) % MOD;
            }
        }
    }

    public long[] convolution(long[] A, long[] B, long MOD_UNUSED) {
        int size = 1;
        while (size < A.length + B.length) size <<= 1;

        long[] fa = new long[size];
        long[] fb = new long[size];

        System.arraycopy(A, 0, fa, 0, A.length);
        System.arraycopy(B, 0, fb, 0, B.length);

        ntt(fa, false);
        ntt(fb, false);

        for (int i = 0; i < size; i++) {
            fa[i] = (fa[i] * fb[i]) % MOD;
        }

        ntt(fa, true);

        long[] result = new long[A.length + B.length - 1];
        System.arraycopy(fa, 0, result, 0, result.length);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // MOD is fixed to 998244353 for this problem
        long MOD = 998244353L;

        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();

        int m = sc.nextInt();
        long[] B = new long[m];
        for (int i = 0; i < m; i++) B[i] = sc.nextLong();

        Solution solution = new Solution();
        long[] result = solution.convolution(A, B, MOD);

        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i < result.length - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
