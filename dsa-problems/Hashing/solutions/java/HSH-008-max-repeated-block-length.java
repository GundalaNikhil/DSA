import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    public int maxRepeatedBlockLength(String s) {
        int n = s.length();
        int low = 0, high = n / 2;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            if (check(s, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    private boolean check(String s, int len) {
        int n = s.length();
        Map<Long, Integer> firstOccurrence = new HashMap<>();
        
        long currentHash = 0;
        long power = 1;
        
        // Precompute BASE^(len-1)
        for (int i = 0; i < len - 1; i++) {
            power = (power * BASE) % MOD;
        }
        
        // Initial window
        for (int i = 0; i < len; i++) {
            currentHash = (currentHash * BASE + s.charAt(i)) % MOD;
        }
        firstOccurrence.put(currentHash, 0);
        
        // Slide window
        for (int i = 1; i <= n - len; i++) {
            // Remove char at i-1
            long remove = (s.charAt(i - 1) * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            
            // Add char at i+len-1
            currentHash = (currentHash * BASE + s.charAt(i + len - 1)) % MOD;
            
            if (firstOccurrence.containsKey(currentHash)) {
                int firstIdx = firstOccurrence.get(currentHash);
                if (i >= firstIdx + len) {
                    return true;
                }
            } else {
                firstOccurrence.put(currentHash, i);
            }
        }
        
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.maxRepeatedBlockLength(s));
        }
        sc.close();
    }
}
