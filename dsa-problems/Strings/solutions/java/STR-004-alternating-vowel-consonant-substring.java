import java.util.*;

class Solution {
    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) != -1;
    }

    public Object[] longestAlternatingVC(String s) {
        if (s == null || s.isEmpty()) {
            return new Object[]{0, ""};
        }

        int maxLen = 1;
        int bestStart = 0;
        int currentLen = 1;
        int start = 0;
        boolean prevIsVowel = isVowel(s.charAt(0));

        for (int i = 1; i < s.length(); i++) {
            boolean currIsVowel = isVowel(s.charAt(i));
            if (currIsVowel != prevIsVowel) {
                currentLen++;
                if (currentLen > maxLen) {
                    maxLen = currentLen;
                    bestStart = start;
                }
            } else {
                start = i;
                currentLen = 1;
            }
            prevIsVowel = currIsVowel;
        }

        return new Object[]{maxLen, s.substring(bestStart, bestStart + maxLen)};
    }
}











class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.useDelimiter("\\A").hasNext() ? sc.next() : "";
        s = s.trim();
        Solution sol = new Solution();
        Object[] res = sol.longestAlternatingVC(s);
        System.out.println(res[0]);
        System.out.println(res[1]);
        sc.close();
    }
}
