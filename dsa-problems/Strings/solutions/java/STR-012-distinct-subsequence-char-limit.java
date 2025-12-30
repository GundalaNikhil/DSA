class Solution {
    public int countDistinctSubsequencesWithLimit(String s, int maxFreq, int MOD) {
        Map<String, Long> dp = new HashMap<>();
        dp.put(encode(new int[26]), 1L);

        for (char c : s.toCharArray()) {
            int charIdx = c - 'a';
            Map<String, Long> newDp = new HashMap<>();

            for (Map.Entry<String, Long> entry : dp.entrySet()) {
                String stateStr = entry.getKey();
                long count = entry.getValue();
                int[] state = decode(stateStr);

                // Don't include
                String key = stateStr;
                newDp.put(key, (newDp.getOrDefault(key, 0L) + count) % MOD);

                // Include if allowed
                if (state[charIdx] < maxFreq) {
                    state[charIdx]++;
                    String newKey = encode(state);
                    newDp.put(newKey, (newDp.getOrDefault(newKey, 0L) + count) % MOD);
                    state[charIdx]--;  // Restore
                }
            }

            dp = newDp;
        }

        long total = 0;
        for (long count : dp.values()) {
            total = (total + count) % MOD;
        }
        return (int) total;
    }

    private String encode(int[] freq) {
        StringBuilder sb = new StringBuilder();
        for (int f : freq) {
            sb.append(f).append(",");
        }
        return sb.toString();
    }

    private int[] decode(String s) {
        String[] parts = s.split(",");
        int[] freq = new int[26];
        for (int i = 0; i < 26; i++) {
            freq[i] = Integer.parseInt(parts[i]);
        }
        return freq;
    }
}
