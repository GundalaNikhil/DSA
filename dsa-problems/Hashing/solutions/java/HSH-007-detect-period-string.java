import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    public int detectPeriod(String s) {
        int n = s.length();
        long[] h = new long[n + 1];
        long[] p = new long[n + 1];
        p[0] = 1;
        
        for (int i = 0; i < n; i++) {
            h[i + 1] = (h[i] * BASE + s.charAt(i)) % MOD;
            p[i + 1] = (p[i] * BASE) % MOD;
        }
        
        // Find divisors
        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                divisors.add(i);
                if (i * i != n) {
                    divisors.add(n / i);
                }
            }
        }
        Collections.sort(divisors);
        
        for (int len : divisors) {
            if (len == n) return n;
            
            // Check if prefix(n-len) == suffix(n-len)
            // S[0...n-len-1] vs S[len...n-1]
            long h1 = getHash(h, p, 0, n - len - 1);
            long h2 = getHash(h, p, len, n - 1);
            
            if (h1 == h2) return len;
        }
        
        return n;
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
            System.out.println(solution.detectPeriod(s));
        }
        sc.close();
    }
}
