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

    // Polynomial Multiplication (Naive O(N^2))
    private long[] polyMul(long[] A, long[] B) {
        int n = A.length;
        int m = B.length;
        long[] res = new long[n + m - 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                res[i + j] = (res[i + j] + A[i] * B[j]) % MOD;
            }
        }
        return res;
    }

    // Polynomial Modulo (Naive O(N*M))
    private long[] polyMod(long[] A, long[] Mod) {
        int n = A.length;
        int m = Mod.length; // Degree of Mod is m-1
        if (n < m) return A;
        
        // We want remainder of A / Mod.
        // Mod is monic? Not necessarily x^L - ...
        // In Kitamasa, Mod is x^L - \sum c_i x^i. So Mod[L] = 1.
        // We reduce from highest degree.
        
        long[] res = Arrays.copyOf(A, n);
        for (int i = n - 1; i >= m - 1; i--) {
            long factor = res[i]; // Since Mod[last] is 1
            if (factor == 0) continue;
            for (int j = 0; j < m; j++) {
                // Mod corresponds to x^L - \sum c_i x^i
                // If recurrence is S[n] = \sum c_i S[n-i], char poly is x^L - \sum c_i x^{L-i}.
                // Let's implement simpler logic:
                // We have relation x^L = \sum_{i=1}^L c_i x^{L-i}.
                // Whenever we see x^k (k >= L), we replace x^L with the sum.
                // Let Mod be the array representing x^L - \sum ...
                // Mod[m-1] is coeff of x^L (which is 1).
                int degDiff = i - (m - 1);
                res[i - j] = (res[i - j] - factor * Mod[m - 1 - j] % MOD + MOD) % MOD;
            }
        }
        return Arrays.copyOf(res, m - 1);
    }
    
    // Better Kitamasa:
    // We want x^n mod (x^L - \sum_{i=1}^L C_i x^{L-i})
    // Let Rec = [C_1, C_2, ..., C_L]
    // Multiplication: A * B. Then reduce using Rec.
    private long[] combine(long[] A, long[] B, long[] Rec) {
        long[] prod = polyMul(A, B);
        int L = Rec.length;
        // Reduce terms with degree >= L
        for (int i = prod.length - 1; i >= L; i--) {
            long factor = prod[i];
            if (factor == 0) continue;
            for (int j = 0; j < L; j++) {
                // x^i = x^{i-L} * x^L = x^{i-L} * \sum C_k x^{L-k}
                // coeff of x^{i-1-j} gets added C_{j+1} * factor
                // Rec[j] is C_{j+1}
                int targetDeg = i - 1 - j;
                prod[targetDeg] = (prod[targetDeg] + factor * Rec[j]) % MOD;
            }
        }
        return Arrays.copyOf(prod, L);
    }

    public long berlekamp_massey(int m, long n, long mod, long[] S) {
        this.MOD = mod;
        
        ArrayList<Long> C = new ArrayList<>();
        ArrayList<Long> B = new ArrayList<>();
        C.add(1L);
        B.add(1L);
        
        int L = 0;
        int b = 1; // shift for B
        long b_delta = 1;
        
        for (int i = 0; i < m; i++) {
            long delta = S[i];
            for (int j = 1; j < C.size(); j++) {
                delta = (delta + C.get(j) * S[i - j]) % MOD;
            }
            
            if (delta == 0) {
                b++;
                continue;
            }
            
            ArrayList<Long> T = new ArrayList<>(C);
            long factor = (delta * modInverse(b_delta)) % MOD;
            
            // C = C - factor * x^b * B
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
        
        // C is [1, -c1, -c2, ...]
        // Recurrence: S[n] = c1 S[n-1] + c2 S[n-2] ...
        // So Rec array is [-C[1], -C[2], ...]
        int K = C.size() - 1;
        if (K == 0) return 0; // Sequence is all zeros
        
        long[] Rec = new long[K];
        for (int i = 0; i < K; i++) {
            Rec[i] = (MOD - C.get(i + 1)) % MOD;
        }
        
        if (n < m) return S[(int)n];
        
        // Compute x^n mod P(x)
        // Base: x^0 = [1]
        // Base: x^1 = [0, 1] (if K > 1)
        
        long[] res = new long[K];
        res[0] = 1;
        
        long[] base = new long[K];
        if (K > 0) base[1 % K] = 1; // Handle K=1 case carefully
        
        long exp = n;
        while (exp > 0) {
            if ((exp & 1) == 1) res = combine(res, base, Rec);
            base = combine(base, base, Rec);
            exp >>= 1;
        }
        
        long ans = 0;
        for (int i = 0; i < K; i++) {
            ans = (ans + res[i] * S[i]) % MOD;
        }
        
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int m = sc.nextInt();
        long n = sc.nextLong();
        long[] S = new long[m];
        for (int i = 0; i < m; i++) S[i] = sc.nextLong();
        long MOD = sc.nextLong();
        
        Solution solution = new Solution();
        System.out.println(solution.berlekamp_massey(m, n, MOD, S));
        
        sc.close();
    }
}
