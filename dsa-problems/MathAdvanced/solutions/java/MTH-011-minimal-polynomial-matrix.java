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

    private ArrayList<Long> berlekampMassey(List<Long> s) {
        ArrayList<Long> C = new ArrayList<>();
        ArrayList<Long> B = new ArrayList<>();
        C.add(1L);
        B.add(1L);
        
        int L = 0;
        int b = 1;
        long b_delta = 1;
        
        for (int i = 0; i < s.size(); i++) {
            long delta = s.get(i);
            for (int j = 1; j < C.size(); j++) {
                delta = (delta + C.get(j) * s.get(i - j)) % MOD;
            }
            
            if (delta == 0) {
                b++;
                continue;
            }
            
            ArrayList<Long> T = new ArrayList<>(C);
            long factor = (delta * modInverse(b_delta)) % MOD;
            
            while (C.size() < B.size() + b) C.add(0L);
            for (int j = 0; j < B.size(); j++) {
                long val = (B.get(j) * factor) % MOD;
                int idx = j + b;
                C.set(idx, (C.get(idx) - val + MOD) % MOD);
            }
            
            if (2 * L <= i) {
                L = i + 1 - L;
                B = T;
                b_delta = delta;
                b = 1;
            } else {
                b++;
            }
        }
        return C;
    }

    public long[] minimal_polynomial_matrix(int n, long mod, long[][] matrix) {
        this.MOD = mod;
        
        // Random vectors u and v
        long[] u = new long[n];
        long[] v = new long[n];
        Random rand = new Random(12345); // Fixed seed for reproducibility
        for(int i=0; i<n; i++) {
            u[i] = rand.nextInt((int)MOD);
            v[i] = rand.nextInt((int)MOD);
        }
        
        List<Long> seq = new ArrayList<>();
        long[] currV = Arrays.copyOf(v, n);
        
        for(int k=0; k < 2*n + 2; k++) {
            long val = 0;
            for(int i=0; i<n; i++) val = (val + u[i] * currV[i]) % MOD;
            seq.add(val);
            
            // Multiply A * currV
            long[] nextV = new long[n];
            for(int r=0; r<n; r++) {
                for(int c=0; c<n; c++) {
                    nextV[r] = (nextV[r] + matrix[r][c] * currV[c]) % MOD;
                }
            }
            currV = nextV;
        }
        
        ArrayList<Long> C = berlekampMassey(seq);
        
        // C is [1, -c1, -c2, ...] corresponding to 1 - c1 x - c2 x^2 ...
        // We want monic polynomial x^d - c1 x^{d-1} ...
        // Minimal poly is x^L C(1/x). i.e., reverse C.
        // And normalize leading coeff to 1.
        
        int d = C.size() - 1;
        long[] res = new long[d + 1];
        
        // Reverse C to get P(x)
        // C[0] is constant term of connection poly -> coeff of x^d in minimal poly
        // C[d] is coeff of x^d in connection poly -> constant term in minimal poly
        // Then recurrence is S_n + c1 S_{n-1} + ... = 0
        // Char poly is x^L + c1 x^{L-1} + ... + cL
        
        // So coeff of x^{L-i} is C[i].
        // Coeff of x^L is C[0] = 1.
        // Coeff of x^0 is C[L].
        
        // We need to output coefficients from constant to highest degree.
        // So output C[L], C[L-1], ..., C[0].
        // But we need to ensure C[0] is 1 (it is by BM construction).
        // And we need to negate coefficients?
        // BM finds \sum C_j S_{n-j} = 0.
        // Char poly is \sum C_j x^{L-j}.
        // Yes, directly C is the coefficients in reverse order.
        
        for(int i=0; i<=d; i++) {
            res[i] = C.get(d - i);
        }
        
        // Output format: degree, then coeffs
        long[] output = new long[d + 2];
        output[0] = d;
        System.arraycopy(res, 0, output, 1, d + 1);
        
        return output;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long MOD = sc.nextLong();
        
        long[][] matrix = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextLong();
            }
        }
        
        Solution solution = new Solution();
        long[] result = solution.minimal_polynomial_matrix(n, MOD, matrix);
        
        System.out.println(result[0]);
        for (int i = 1; i < result.length; i++) {
            System.out.print(result[i] + (i < result.length - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
