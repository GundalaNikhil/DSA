class Solution {
    public boolean canBalanceWithSkips(String s, int k) {
        int balance = 0;
        int skipsUsed = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                balance++;
            } else {  // c == ')'
                balance--;
                if (balance < 0) {
                    // Need to skip this ')'
                    skipsUsed++;
                    balance = 0;
                }
            }
        }

        // Remaining balance are unmatched '('
        int totalSkipsNeeded = skipsUsed + balance;
        return totalSkipsNeeded <= k;
    }
}
