import java.util.*;

class Solution {
    public long maxProfit(int[] prices, long fee) {
        int n = prices.length;
        final long NEG = (long)-4e18;
        long buyable = 0, hold = NEG, ans = 0;
        long[] unlock = new long[n + 8];
        Arrays.fill(unlock, NEG);
        for (int i = 0; i < n; i++) {
            if (unlock[i] != NEG) buyable = Math.max(buyable, unlock[i]);
            long prevHold = hold;
            hold = Math.max(hold, buyable - prices[i]);
            if (prevHold != NEG) {
                long sellProfit = prevHold + prices[i] - fee;
                ans = Math.max(ans, sellProfit);
                int nextMonday = i - (i % 7) + 7;
                if (nextMonday < unlock.length) {
                    unlock[nextMonday] = Math.max(unlock[nextMonday], sellProfit);
                }
            }
        }
        if (hold != NEG) ans = Math.max(ans, hold + prices[n - 1] - fee);
        ans = Math.max(ans, buyable);
        for (int i = n; i < unlock.length; i++) ans = Math.max(ans, unlock[i]);
        return ans;
    }
}
