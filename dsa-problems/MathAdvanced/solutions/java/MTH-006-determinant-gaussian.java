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

    public long determinant_gaussian(int n, long mod, long[][] matrix) {
        this.MOD = mod;
        long det = 1;
        
        for (int i = 0; i < n; i++) {
            int pivot = i;
            while (pivot < n && matrix[pivot][i] == 0) pivot++;
            
            if (pivot == n) return 0; // Singular matrix
            
            if (pivot != i) {
                // Swap rows
                long[] temp = matrix[i];
                matrix[i] = matrix[pivot];
                matrix[pivot] = temp;
                det = (MOD - det) % MOD; // Flip sign
            }
            
            det = (det * matrix[i][i]) % MOD;
            long inv = modInverse(matrix[i][i]);
            
            for (int j = i + 1; j < n; j++) {
                if (matrix[j][i] != 0) {
                    long factor = (matrix[j][i] * inv) % MOD;
                    for (int k = i; k < n; k++) {
                        long sub = (factor * matrix[i][k]) % MOD;
                        matrix[j][k] = (matrix[j][k] - sub + MOD) % MOD;
                    }
                }
            }
        }
        
        return det;
    }
}

public class Main {
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
        System.out.println(solution.determinant_gaussian(n, MOD, matrix));
        
        sc.close();
    }
}
