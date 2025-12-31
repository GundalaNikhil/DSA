import java.util.*;

class Solution {
    public List<List<String>> minPalindromePartitions(String s, int L) {
        int n = s.length();
        // Precompute palindromes
        boolean[][] isPal = new boolean[n][n];
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                if (s.charAt(i) == s.charAt(j)) {
                    if (len <= 2 || isPal[i + 1][j - 1]) {
                        isPal[i][j] = true;
                    }
                }
            }
        }

        List<List<String>> results = new ArrayList<>();
        int[] minCount = {Integer.MAX_VALUE};
        
        backtrack(0, s, L, isPal, new ArrayList<>(), results, minCount);
        return results;
    }

    private void backtrack(int start, String s, int L, boolean[][] isPal, 
                           List<String> current, List<List<String>> results, int[] minCount) {
        if (start == s.length()) {
            if (current.size() < minCount[0]) {
                minCount[0] = current.size();
                results.clear();
                results.add(new ArrayList<>(current));
            } else if (current.size() == minCount[0]) {
                results.add(new ArrayList<>(current));
            }
            return;
        }

        // Pruning: if current size already exceeds min found, stop
        if (current.size() >= minCount[0]) return;

        for (int end = start; end < s.length(); end++) {
            if (end - start + 1 > L) break; // Length constraint
            if (isPal[start][end]) {
                current.add(s.substring(start, end + 1));
                backtrack(end + 1, s, L, isPal, current, results, minCount);
                current.remove(current.size() - 1);
            }
        }
    }
}
