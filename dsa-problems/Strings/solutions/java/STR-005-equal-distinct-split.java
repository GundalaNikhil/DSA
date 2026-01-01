class Solution {
    public int countEqualDistinctSplits(String s) {
        int n = s.length();
        if (n < 2) return 0;

        // Build suffix distinct counts
        int[] suffixDistinct = new int[n + 1];
        Set<Character> charSet = new HashSet<>();
        for (int i = n - 1; i >= 0; i--) {
            charSet.add(s.charAt(i));
            suffixDistinct[i] = charSet.size();
        }

        // Scan left and compare
        Set<Character> leftSet = new HashSet<>();
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            leftSet.add(s.charAt(i));
            if (leftSet.size() == suffixDistinct[i + 1]) {
                count++;
            }
        }

        return count;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        Solution sol = new Solution();
        System.out.println(sol.countEqualDistinctSplits(s));
        sc.close();
    }
}
