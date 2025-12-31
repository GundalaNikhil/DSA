import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 31L;

    public int longestCommonSubstring(String a, String b) {
        int low = 0, high = Math.min(a.length(), b.length());
        int ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            if (check(a, b, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

    private boolean check(String a, String b, int len) {
        Set<Long> hashesA = new HashSet<>();

        long currentHash = 0;
        long power = 1;

        // Precompute BASE^len
        for (int i = 0; i < len; i++) {
            if (i > 0) power = (power * BASE) % MOD;
            currentHash = (currentHash * BASE + a.charAt(i)) % MOD;
        }
        hashesA.add(currentHash);

        for (int i = len; i < a.length(); i++) {
            // Remove leading char: (H - s[i-len] * B^(len-1)) % MOD
            long remove = (a.charAt(i - len) * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            // Add trailing char
            currentHash = (currentHash * BASE + a.charAt(i)) % MOD;
            hashesA.add(currentHash);
        }

        // Check B
        currentHash = 0;
        for (int i = 0; i < len; i++) {
            currentHash = (currentHash * BASE + b.charAt(i)) % MOD;
        }
        if (hashesA.contains(currentHash)) return true;

        for (int i = len; i < b.length(); i++) {
            long remove = (b.charAt(i - len) * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            currentHash = (currentHash * BASE + b.charAt(i)) % MOD;
            if (hashesA.contains(currentHash)) return true;
        }

        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String a = sc.nextLine();
            String b = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.longestCommonSubstring(a, b));
        }
        sc.close();
    }
}
