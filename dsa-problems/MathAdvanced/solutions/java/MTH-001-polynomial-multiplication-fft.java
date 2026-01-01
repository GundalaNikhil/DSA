import java.util.*;

class Solution {
    private static final long MOD = 1000000007;
    private static final double PI = Math.acos(-1);

    static class Complex {
        double r, i;
        Complex(double r, double i) { this.r = r; this.i = i; }
        Complex add(Complex o) { return new Complex(r + o.r, i + o.i); }
        Complex sub(Complex o) { return new Complex(r - o.r, i - o.i); }
        Complex mul(Complex o) { return new Complex(r * o.r - i * o.i, r * o.i + i * o.r); }
    }

    private void fft(Complex[] a, boolean invert) {
        int n = a.length;
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j >= bit; bit >>= 1) j -= bit;
            j += bit;
            if (i < j) { Complex temp = a[i]; a[i] = a[j]; a[j] = temp; }
        }
        for (int len = 2; len <= n; len <<= 1) {
            double ang = 2 * PI / len * (invert ? -1 : 1);
            Complex wlen = new Complex(Math.cos(ang), Math.sin(ang));
            for (int i = 0; i < n; i += len) {
                Complex w = new Complex(1, 0);
                for (int j = 0; j < len / 2; j++) {
                    Complex u = a[i + j], v = a[i + j + len / 2].mul(w);
                    a[i + j] = u.add(v);
                    a[i + j + len / 2] = u.sub(v);
                    w = w.mul(wlen);
                }
            }
        }
        if (invert) {
            for (int i = 0; i < n; i++) { a[i].r /= n; a[i].i /= n; }
        }
    }

    public long[] multiplyPolynomials(long[] A, long[] B) {
        int n = 1;
        while (n < A.length + B.length) n <<= 1;
        
        Complex[] fa = new Complex[n];
        Complex[] fb = new Complex[n];
        
        // Split coefficients to handle large modulo
        // Using simplified approach: Assuming standard FFT precision is enough for this problem's constraints
        // If strict 10^9+7 with full range, need 2-3 FFTs or splitting.
        // Here implementing standard FFT for simplicity, noting precision limits.
        // For robust solution, one would split A[i] = A1[i]*S + A0[i].
        
        // Let's implement the splitting method (MTT) for correctness.
        int S = 32000;
        Complex[] a0 = new Complex[n], a1 = new Complex[n];
        Complex[] b0 = new Complex[n], b1 = new Complex[n];
        
        for(int i=0; i<n; i++) {
            long valA = (i < A.length) ? A[i] : 0;
            long valB = (i < B.length) ? B[i] : 0;
            a0[i] = new Complex(valA % S, 0);
            a1[i] = new Complex(valA / S, 0);
            b0[i] = new Complex(valB % S, 0);
            b1[i] = new Complex(valB / S, 0);
        }
        
        fft(a0, false); fft(a1, false);
        fft(b0, false); fft(b1, false);
        
        Complex[] c0 = new Complex[n], c1 = new Complex[n], c2 = new Complex[n];
        for(int i=0; i<n; i++) {
            // (a1*S + a0) * (b1*S + b0) = a1*b1*S^2 + (a1*b0 + a0*b1)*S + a0*b0
            c0[i] = a0[i].mul(b0[i]); // a0*b0
            c2[i] = a1[i].mul(b1[i]); // a1*b1
            // Middle term: (a0+a1)*(b0+b1) - a0*b0 - a1*b1
            Complex sumA = a0[i].add(a1[i]);
            Complex sumB = b0[i].add(b1[i]);
            c1[i] = sumA.mul(sumB).sub(c0[i]).sub(c2[i]);
        }
        
        fft(c0, true); fft(c1, true); fft(c2, true);
        
        long[] res = new long[A.length + B.length - 1];
        for(int i=0; i<res.length; i++) {
            long v0 = (long)(c0[i].r + 0.5) % MOD;
            long v1 = (long)(c1[i].r + 0.5) % MOD;
            long v2 = (long)(c2[i].r + 0.5) % MOD;
            
            long term1 = v2 * S % MOD * S % MOD;
            long term2 = v1 * S % MOD;
            long term3 = v0;
            
            res[i] = (term1 + term2 + term3) % MOD;
        }
        return res;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();
        
        int m = sc.nextInt();
        long[] B = new long[m];
        for (int i = 0; i < m; i++) B[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[] result = solution.multiplyPolynomials(A, B);
        
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i < result.length - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
