import java.util.*;

class Solution {
    private static final long INF = Long.MAX_VALUE / 4;

    private static long key(long dpVal, int y) {
        return dpVal - (long) y;
    }

    public long minCost(int k, int target, int[] d, long[] c, long[] p) {
        long[] dp = new long[target + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int i = 0; i < k; i++) {
            int denom = d[i];
            int cap = (int) Math.min(c[i], target / (long) denom);
            long thresholdRaw = c[i] / 2L;
            int t = (int) Math.min(thresholdRaw, (long) cap);
            long penalty = p[i];

            long[] next = new long[target + 1];
            Arrays.fill(next, INF);

            for (int r = 0; r < denom; r++) {
                int qMax = (target - r) / denom;
                if (qMax < 0) continue;

                int L1 = Math.min(cap, t); // no-pen window length in q-space

                ArrayDeque<Integer> dqNoPen = new ArrayDeque<>();
                ArrayDeque<Integer> dqPen = new ArrayDeque<>();

                for (int q = 0; q <= qMax; q++) {
                    int sumY = r + q * denom;
                    long dpVal = dp[sumY];
                    if (dpVal < INF) {
                        long kVal = key(dpVal, q);
                        while (!dqNoPen.isEmpty()) {
                            int last = dqNoPen.peekLast();
                            long lastVal = key(dp[r + last * denom], last);
                            if (kVal <= lastVal) dqNoPen.pollLast();
                            else break;
                        }
                        dqNoPen.addLast(q);
                    }

                    int minYNoPen = q - L1;
                    while (!dqNoPen.isEmpty() && dqNoPen.peekFirst() < minYNoPen) dqNoPen.pollFirst();

                    long best = INF;
                    if (!dqNoPen.isEmpty()) {
                        int y = dqNoPen.peekFirst();
                        long base = key(dp[r + y * denom], y);
                        best = Math.min(best, (long) q + base);
                    }

                    if (cap > t) {
                        int yAdd = q - (t + 1);
                        if (yAdd >= 0) {
                            int sumAdd = r + yAdd * denom;
                            long dpAdd = dp[sumAdd];
                            if (dpAdd < INF) {
                                long kVal = key(dpAdd, yAdd);
                                while (!dqPen.isEmpty()) {
                                    int last = dqPen.peekLast();
                                    long lastVal = key(dp[r + last * denom], last);
                                    if (kVal <= lastVal) dqPen.pollLast();
                                    else break;
                                }
                                dqPen.addLast(yAdd);
                            }
                        }

                        int minYPen = q - cap;
                        while (!dqPen.isEmpty() && dqPen.peekFirst() < minYPen) dqPen.pollFirst();

                        if (!dqPen.isEmpty()) {
                            int y = dqPen.peekFirst();
                            long base = key(dp[r + y * denom], y);
                            best = Math.min(best, (long) q + penalty + base);
                        }
                    }

                    int sum = r + q * denom;
                    if (best < next[sum]) next[sum] = best;
                }
            }

            dp = next;
        }

        return dp[target] >= INF ? -1 : dp[target];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int target = sc.nextInt();
        int[] d = new int[k];
        long[] c = new long[k];
        long[] p = new long[k];
        for (int i = 0; i < k; i++) {
            d[i] = sc.nextInt();
            c[i] = sc.nextLong();
            p[i] = sc.nextLong();
        }
        System.out.println(new Solution().minCost(k, target, d, c, p));
        sc.close();
    }
}
