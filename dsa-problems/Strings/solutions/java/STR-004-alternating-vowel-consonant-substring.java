class Solution {
    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    public Object[] longestAlternatingVC(String s) {
        if (s == null || s.isEmpty()) {
            return new Object[]{0, ""};
        }

        int maxLen = 1, bestStart = 0, currentLen = 1, start = 0;
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
