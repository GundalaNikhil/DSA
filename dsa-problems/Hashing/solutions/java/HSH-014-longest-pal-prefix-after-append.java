import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;

    public int longestPalindromicPrefix(String s, char c) {
        String T = s + c;
        int n = T.length();

        long fwdHash = 0;
        long revHash = 0;
        long power = 1;

        int maxLen = 0;

        for (int i = 0; i < n; i++) {
            char val = T.charAt(i);

            fwdHash = (fwdHash * BASE + val) % MOD;
            revHash = (revHash + val * power) % MOD;

            if (fwdHash == revHash) {
                maxLen = i + 1;
            }

            power = (power * BASE) % MOD;
        }

        return maxLen;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextLine()) {
                String line = sc.nextLine();
                if (line.length() > 0) {
                    char c = line.charAt(0);
                    Solution solution = new Solution();
                    System.out.println(solution.longestPalindromicPrefix(s, c));
                }
            }
        }
        sc.close();
    }
}
