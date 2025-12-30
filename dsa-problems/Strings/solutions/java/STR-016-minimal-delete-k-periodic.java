class Solution {
    public int minimalDeleteKPeriodic(String s, int k) {
        int n = s.length();
        int deletions = 0;

        for (int pos = 0; pos < k; pos++) {
            Map<Character, Integer> freq = new HashMap<>();

            // Count frequency at positions pos, pos+k, pos+2k, ...
            for (int i = pos; i < n; i += k) {
                char c = s.charAt(i);
                freq.put(c, freq.getOrDefault(c, 0) + 1);
            }

            // Keep most frequent, delete others
            if (!freq.isEmpty()) {
                int maxFreq = Collections.max(freq.values());
                int totalAtPos = freq.values().stream().mapToInt(Integer::intValue).sum();
                deletions += totalAtPos - maxFreq;
            }
        }

        return deletions;
    }
}
