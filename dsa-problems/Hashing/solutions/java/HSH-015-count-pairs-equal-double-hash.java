import java.util.*;

class Solution {
    private static final long MOD1 = 1_000_000_007L;
    private static final long BASE1 = 313L;
    private static final long MOD2 = 1_000_000_009L;
    private static final long BASE2 = 317L;
    
    public long countPairs(String s, int L) {
        int n = s.length();
        if (L > n) return 0;
        
        // Map key: "hash1,hash2" string or a custom object
        // Using String key is easiest in Java but slightly slower. 
        // For competitive programming, use a custom class or combine into one long if possible (but 2 longs don't fit in 1 long).
        // Here we use String for clarity.
        Map<String, Integer> counts = new HashMap<>();
        
        long h1 = 0, h2 = 0;
        long p1 = 1, p2 = 1;
        
        // Precompute powers
        for (int i = 0; i < L - 1; i++) {
            p1 = (p1 * BASE1) % MOD1;
            p2 = (p2 * BASE2) % MOD2;
        }
        
        // Initial window
        for (int i = 0; i < L; i++) {
            h1 = (h1 * BASE1 + s.charAt(i)) % MOD1;
            h2 = (h2 * BASE2 + s.charAt(i)) % MOD2;
        }
        
        String key = h1 + "," + h2;
        counts.put(key, 1);
        
        // Slide
        for (int i = 1; i <= n - L; i++) {
            long remove1 = (s.charAt(i - 1) * p1) % MOD1;
            h1 = (h1 - remove1 + MOD1) % MOD1;
            h1 = (h1 * BASE1 + s.charAt(i + L - 1)) % MOD1;
            
            long remove2 = (s.charAt(i - 1) * p2) % MOD2;
            h2 = (h2 - remove2 + MOD2) % MOD2;
            h2 = (h2 * BASE2 + s.charAt(i + L - 1)) % MOD2;
            
            key = h1 + "," + h2;
            counts.put(key, counts.getOrDefault(key, 0) + 1);
        }
        
        long ans = 0;
        for (int count : counts.values()) {
            ans += (long) count * (count - 1) / 2;
        }
        
        return ans;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextInt()) {
                int L = sc.nextInt();
                Solution solution = new Solution();
                System.out.println(solution.countPairs(s, L));
            }
        }
        sc.close();
    }
}
