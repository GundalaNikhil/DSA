import java.util.*;

class Solution {
    public String longestWildcardPalindrome(String s) {
        if (s == null || s.length() == 0) return "";
        
        StringBuilder sb = new StringBuilder();
        sb.append('^');
        for (char c : s.toCharArray()) {
            sb.append('#').append(c);
        }
        sb.append("#$");
        String T = sb.toString();
        
        int n = T.length();
        int[] P = new int[n];
        int C = 0, R = 0;
        
        for (int i = 1; i < n - 1; i++) {
            P[i] = (R > i) ? Math.min(R - i, P[2 * C - i]) : 0;
            
            while (match(T.charAt(i + 1 + P[i]), T.charAt(i - 1 - P[i]))) {
                P[i]++;
            }
            
            if (i + P[i] > R) {
                C = i;
                R = i + P[i];
            }
        }
        
        int maxLen = 0;
        int centerIndex = 0;
        for (int i = 1; i < n - 1; i++) {
            if (P[i] > maxLen) {
                maxLen = P[i];
                centerIndex = i;
            }
        }
        
        int start = (centerIndex - maxLen) / 2;
        return s.substring(start, start + maxLen);
    }
    
    private boolean match(char c1, char c2) {
        if (c1 == '#' || c2 == '#') return c1 == c2;
        if (c1 == '^' || c2 == '^' || c1 == '`' || c2 == '`') return c1 == c2;
        // Both are letters or ?
        return c1 == c2 || c1 == '?' || c2 == '?';
    }
}

public class Main {
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
