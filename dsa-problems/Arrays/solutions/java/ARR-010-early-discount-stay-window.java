import java.util.*;

class Solution {
    public int maxProfitWithConstraints(int[] prices, int dMin, int dMax, int C) {
        int n = prices.length;
        // Deque stores INDICES
        Deque<Integer> dq = new ArrayDeque<>();
        int maxProfit = 0;

        for (int j = dMin; j < n; j++) {
            // 1. Add new valid buy index (j - dMin) to window
            int buyCandidate = j - dMin;
            while (!dq.isEmpty() && prices[dq.peekLast()] >= prices[buyCandidate]) {
                dq.pollLast(); // Maintain monotonic increasing property
            }
            dq.offerLast(buyCandidate);

            // 2. Remove expired indices from window (older than j - dMax)
            if (!dq.isEmpty() && dq.peekFirst() < j - dMax) {
                dq.pollFirst();
            }

            // 3. Calculate profit using min price (front of deque)
            int minBuyPrice = prices[dq.peekFirst()];
            int sellPrice = Math.min(prices[j], C);
            maxProfit = Math.max(maxProfit, sellPrice - minBuyPrice);
        }

        return maxProfit;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] prices = new int[n];
        for (int i = 0; i < n; i++) prices[i] = sc.nextInt();

        int dMin = sc.nextInt();
        int dMax = sc.nextInt();
        int C = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maxProfitWithConstraints(prices, dMin, dMax, C));
        sc.close();
    }
}
