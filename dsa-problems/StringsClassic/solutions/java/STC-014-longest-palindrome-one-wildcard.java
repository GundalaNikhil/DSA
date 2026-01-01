import java.util.*;

class Solution {
    public int longestWildcardPalindrome(String s) {
        int n = s.length();
        if (s == null || n == 0) return 0;

        int maxLen = 1;

        // Expand around each center (character and between characters)
        // 2*n - 1 centers
        for (int i = 0; i < 2 * n - 1; i++) {
            int l = i / 2;
            int r = (i + 1) / 2;

            int tempMismatch = 0;

            while (l >= 0 && r < n) {
                if (s.charAt(l) != s.charAt(r)) {
                    tempMismatch++;
                }

                if (tempMismatch > 1) {
                    break;
                }

                int length = r - l + 1;
                if (length > maxLen) {
                    maxLen = length;
                }

                l--;
                r++;
            }
        }

        return maxLen;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.longestWildcardPalindrome(s));
        }
        sc.close();
    }
}
