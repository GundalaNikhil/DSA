class Solution {
    public boolean canRotateToPalindrome(String s) {
        if (s == null || s.length() <= 1) return true;

        // Count character frequencies
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        // Count characters with odd frequency
        int oddCount = 0;
        for (int count : freq.values()) {
            if (count % 2 == 1) {
                oddCount++;
            }
        }

        return oddCount <= 1;
    }
}
