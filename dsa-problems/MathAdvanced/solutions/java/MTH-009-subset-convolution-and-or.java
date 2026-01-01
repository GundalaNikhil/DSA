import java.util.*;

class Solution {
    private long MOD = 1000000007;

    private void fzt_or(long[] a, boolean invert) {
        int n = a.length;
        int bits = Integer.numberOfTrailingZeros(n);
        for (int i = 0; i < bits; i++) {
            for (int mask = 0; mask < n; mask++) {
                if ((mask & (1 << i)) != 0) {
                    long u = a[mask];
                    long v = a[mask ^ (1 << i)];
                    if (!invert) {
                        a[mask] = (u + v) % MOD;
                    } else {
                        a[mask] = (u - v + MOD) % MOD;
                    }
                }
            }
        }
    }

    private void fzt_and(long[] a, boolean invert) {
        int n = a.length;
        int bits = Integer.numberOfTrailingZeros(n);
        for (int i = 0; i < bits; i++) {
            for (int mask = 0; mask < n; mask++) {
                if ((mask & (1 << i)) == 0) {
                    long u = a[mask];
                    long v = a[mask ^ (1 << i)];
                    if (!invert) {
                        a[mask] = (u + v) % MOD;
                    } else {
                        a[mask] = (u - v + MOD) % MOD;
                    }
                }
            }
        }
    }

    public long[] subset_convolution_and_or(int n, int op, long[] A, long[] B) {
        int size = 1 << n;
        
        if (op == 1) { // OR
            fzt_or(A, false);
            fzt_or(B, false);
        } else { // AND
            fzt_and(A, false);
            fzt_and(B, false);
        }
        
        long[] C = new long[size];
        for (int i = 0; i < size; i++) {
            C[i] = (A[i] * B[i]) % MOD;
        }
        
        if (op == 1) { // OR
            fzt_or(C, true);
        } else { // AND
            fzt_and(C, true);
        }
        
        return C;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int op = sc.nextInt();
        int size = 1 << n;
        
        long[] A = new long[size];
        for (int i = 0; i < size; i++) A[i] = sc.nextLong();
        
        long[] B = new long[size];
        for (int i = 0; i < size; i++) B[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[] res = solution.subset_convolution_and_or(n, op, A, B);
        
        for (int i = 0; i < size; i++) {
            System.out.print(res[i] + (i < size - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
