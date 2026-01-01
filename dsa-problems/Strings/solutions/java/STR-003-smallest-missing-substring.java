class Solution {
    public String smallestMissingSubstring(String s, int k) {
        // Extract all k-length substrings
        Set<String> substrings = new HashSet<>();
        for (int i = 0; i <= s.length() - k; i++) {
            substrings.add(s.substring(i, i + k));
        }

        // DFS to find smallest missing
        return dfs(new StringBuilder(), k, substrings);
    }

    private String dfs(StringBuilder current, int remaining, Set<String> substrings) {
        if (remaining == 0) {
            String candidate = current.toString();
            return substrings.contains(candidate) ? null : candidate;
        }

        for (char c = 'a'; c <= 'z'; c++) {
            current.append(c);
            String result = dfs(current, remaining - 1, substrings);
            if (result != null) {
                return result;
            }
            current.setLength(current.length() - 1); // backtrack
        }

        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.smallestMissingSubstring(s, k));
        sc.close();
    }
}
