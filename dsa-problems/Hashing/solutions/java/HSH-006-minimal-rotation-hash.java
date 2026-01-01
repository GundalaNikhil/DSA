import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    public String minimalRotation(String s) {
        int n = s.length();
        String doubled = s + s;
        int m = doubled.length();
        
        long[] h = new long[m + 1];
        long[] p = new long[m + 1];
        p[0] = 1;
        
        for (int i = 0; i < m; i++) {
            h[i + 1] = (h[i] * BASE + doubled.charAt(i)) % MOD;
            p[i + 1] = (p[i] * BASE) % MOD;
        }
        
        int best = 0;
        for (int curr = 1; curr < n; curr++) {
            // Compare rotation at 'best' vs 'curr'
            int lcp = getLCP(h, p, best, curr, n);
            if (lcp < n) {
                if (doubled.charAt(curr + lcp) < doubled.charAt(best + lcp)) {
                    best = curr;
                }
            }
        }
        
        return doubled.substring(best, best + n);
    }
    
    private int getLCP(long[] h, long[] p, int i, int j, int maxLen) {
        int low = 0, high = maxLen;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            long h1 = getHash(h, p, i, i + mid - 1);
            long h2 = getHash(h, p, j, j + mid - 1);
            
            if (h1 == h2) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    private long getHash(long[] h, long[] p, int l, int r) {
        int len = r - l + 1;
        long val = (h[r + 1] - (h[l] * p[len]) % MOD + MOD) % MOD;
        return val;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.minimalRotation(s));
        }
        sc.close();
    }
}
