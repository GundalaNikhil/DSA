import java.util.*;

class Solution {
    public boolean canRotateToPalindrome(String s) {
        if (s == null || s.length() == 0) return true;
        int n = s.length();
        String doubled = s + s;
        
        for (int i = 0; i < n; i++) {
            String rotated = doubled.substring(i, i + n);
            if (isPalindrome(rotated)) {
                return true;
            }
        }
        return false;
    }

    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }
}








class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.useDelimiter("\\A").hasNext() ? sc.next() : "";
        s = s.trim();
        Solution sol = new Solution();
        System.out.println(sol.canRotateToPalindrome(s));
        sc.close();
    }
}
