import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;

    public int countDistinctSubstrings(String s) {
        int n = s.length();
        // Use a Set to store unique hashes
        // For competitive programming with N=10^5, this will TLE/MLE.
        // But for N <= 2000, it works.
        Set<Long> distinctHashes = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            long currentHash = 0;
            for (int j = i; j < n; j++) {
                currentHash = (currentHash * BASE + s.charAt(j)) % MOD;
                distinctHashes.add(currentHash);
            }
        }
        
        // +1 for empty string
        return distinctHashes.size() + 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.countDistinctSubstrings(s));
        }
        sc.close();
    }
}
