import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    // Using single hash for simplicity in template, but double hash is safer
    // Ideally, implement double hashing as in HSH-002
    
    public boolean[] checkPalindromes(String s, int[][] queries) {
        int n = s.length();
        long[] hForward = new long[n + 1];
        long[] hReverse = new long[n + 1];
        long[] power = new long[n + 1];
        
        power[0] = 1;
        String revS = new StringBuilder(s).reverse().toString();
        
        for (int i = 0; i < n; i++) {
            hForward[i + 1] = (hForward[i] * BASE + s.charAt(i)) % MOD;
            hReverse[i + 1] = (hReverse[i] * BASE + revS.charAt(i)) % MOD;
            power[i + 1] = (power[i] * BASE) % MOD;
        }
        
        boolean[] results = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            
            long fwdHash = getHash(hForward, power, l, r);
            
            // Map indices to reversed string
            // s[l...r] corresponds to revS[n-1-r ... n-1-l]
            int revL = n - 1 - r;
            int revR = n - 1 - l;
            long revHash = getHash(hReverse, power, revL, revR);
            
            results[i] = (fwdHash == revHash);
        }
        return results;
    }
    
    private long getHash(long[] h, long[] p, int l, int r) {
        int len = r - l + 1;
        long val = (h[r + 1] - (h[l] * p[len]) % MOD + MOD) % MOD;
        return val;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextInt()) {
                int q = sc.nextInt();
                int[][] queries = new int[q][2];
                for (int i = 0; i < q; i++) {
                    queries[i][0] = sc.nextInt();
                    queries[i][1] = sc.nextInt();
                }
                Solution solution = new Solution();
                boolean[] result = solution.checkPalindromes(s, queries);
                for (boolean ans : result) {
                    System.out.println(ans);
                }
            }
        }
        sc.close();
    }
}
