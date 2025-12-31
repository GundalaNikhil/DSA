import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE1 = 313L; // For rows
    private static final long BASE2 = 317L; // For cols
    
    public boolean findMatrix(int[][] A, int[][] B) {
        int n = A.length, m = A[0].length;
        int p = B.length, q = B[0].length;
        
        if (p > n || q > m) return false;
        
        // 1. Compute Hash of B
        long targetHash = computeMatrixHash(B, p, q);
        
        // 2. Precompute Row Hashes of A
        // rowHashes[i][j] stores hash of A[i][j...j+q-1]
        long[][] rowHashes = new long[n][m - q + 1];
        long power1 = 1; // BASE1^(q-1)
        for (int k = 0; k < q - 1; k++) power1 = (power1 * BASE1) % MOD;
        
        for (int i = 0; i < n; i++) {
            long h = 0;
            // Initial window
            for (int k = 0; k < q; k++) {
                h = (h * BASE1 + A[i][k]) % MOD;
            }
            rowHashes[i][0] = h;
            
            // Slide
            for (int j = 1; j <= m - q; j++) {
                long remove = (A[i][j - 1] * power1) % MOD;
                h = (h - remove + MOD) % MOD;
                h = (h * BASE1 + A[i][j + q - 1]) % MOD;
                rowHashes[i][j] = h;
            }
        }
        
        // 3. Compute Column Hashes on rowHashes
        // We need to find hash of P rows in rowHashes column j
        long power2 = 1; // BASE2^(p-1)
        for (int k = 0; k < p - 1; k++) power2 = (power2 * BASE2) % MOD;
        
        for (int j = 0; j <= m - q; j++) {
            long h = 0;
            // Initial window of P rows
            for (int k = 0; k < p; k++) {
                h = (h * BASE2 + rowHashes[k][j]) % MOD;
            }
            if (h == targetHash) return true;
            
            // Slide down
            for (int i = 1; i <= n - p; i++) {
                long remove = (rowHashes[i - 1][j] * power2) % MOD;
                h = (h - remove + MOD) % MOD;
                h = (h * BASE2 + rowHashes[i + p - 1][j]) % MOD;
                
                if (h == targetHash) return true;
            }
        }
        
        return false;
    }
    
    private long computeMatrixHash(int[][] M, int p, int q) {
        long[] rowH = new long[p];
        for (int i = 0; i < p; i++) {
            long h = 0;
            for (int j = 0; j < q; j++) {
                h = (h * BASE1 + M[i][j]) % MOD;
            }
            rowH[i] = h;
        }
        
        long finalH = 0;
        for (int i = 0; i < p; i++) {
            finalH = (finalH * BASE2 + rowH[i]) % MOD;
        }
        return finalH;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] A = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    A[i][j] = sc.nextInt();
                }
            }
            
            int p = sc.nextInt();
            int q = sc.nextInt();
            int[][] B = new int[p][q];
            for (int i = 0; i < p; i++) {
                for (int j = 0; j < q; j++) {
                    B[i][j] = sc.nextInt();
                }
            }
            
            Solution solution = new Solution();
            System.out.println(solution.findMatrix(A, B));
        }
        sc.close();
    }
}
