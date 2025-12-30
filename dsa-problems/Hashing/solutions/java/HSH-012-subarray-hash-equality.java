import java.util.*;

class Solution {
    private static final long MOD1 = 1_000_000_007L;
    private static final long BASE1 = 100003L; // Larger than typical small constraints, but random is better
    private static final long MOD2 = 1_000_000_009L;
    private static final long BASE2 = 100019L;
    
    public boolean[] checkSubarrayEquality(int[] arr, int[][] queries) {
        int n = arr.length;
        long[] h1 = new long[n + 1];
        long[] p1 = new long[n + 1];
        long[] h2 = new long[n + 1];
        long[] p2 = new long[n + 1];
        
        p1[0] = 1;
        p2[0] = 1;
        
        for (int i = 0; i < n; i++) {
            // Handle negative numbers by adding offset or just standard mod arithmetic
            // (val % MOD + MOD) % MOD ensures positive
            long val = arr[i];
            
            h1[i + 1] = (h1[i] * BASE1 + val) % MOD1;
            if (h1[i + 1] < 0) h1[i + 1] += MOD1;
            
            p1[i + 1] = (p1[i] * BASE1) % MOD1;
            
            h2[i + 1] = (h2[i] * BASE2 + val) % MOD2;
            if (h2[i + 1] < 0) h2[i + 1] += MOD2;
            
            p2[i + 1] = (p2[i] * BASE2) % MOD2;
        }
        
        boolean[] results = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l1 = queries[i][0];
            int r1 = queries[i][1];
            int l2 = queries[i][2];
            int r2 = queries[i][3];
            
            if (r1 - l1 != r2 - l2) {
                results[i] = false;
                continue;
            }
            
            long hash1_sub1 = getHash(h1, p1, l1, r1, MOD1);
            long hash1_sub2 = getHash(h1, p1, l2, r2, MOD1);
            
            long hash2_sub1 = getHash(h2, p2, l1, r1, MOD2);
            long hash2_sub2 = getHash(h2, p2, l2, r2, MOD2);
            
            results[i] = (hash1_sub1 == hash1_sub2) && (hash2_sub1 == hash2_sub2);
        }
        
        return results;
    }
    
    private long getHash(long[] h, long[] p, int l, int r, long mod) {
        int len = r - l + 1;
        long val = (h[r + 1] - (h[l] * p[len]) % mod + mod) % mod;
        return val;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            
            int q = sc.nextInt();
            int[][] queries = new int[q][4];
            for (int i = 0; i < q; i++) {
                queries[i][0] = sc.nextInt();
                queries[i][1] = sc.nextInt();
                queries[i][2] = sc.nextInt();
                queries[i][3] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            boolean[] result = solution.checkSubarrayEquality(arr, queries);
            
            for (boolean ans : result) {
                System.out.println(ans);
            }
        }
        sc.close();
    }
}
