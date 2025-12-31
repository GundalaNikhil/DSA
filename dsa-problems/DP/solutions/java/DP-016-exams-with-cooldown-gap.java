import java.util.*;

class Solution {
    static class Exam { long s, e, w; Exam(long s, long e, long w){ this.s=s; this.e=e; this.w=w; } }

    public long maxScore(List<Exam> exams, long g) {
        exams.sort(Comparator.comparingLong(x -> x.e));
        int n = exams.size();
        long[] ends = new long[n];
        for (int i = 0; i < n; i++) ends[i] = exams.get(i).e;
        long[] dp = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            Exam ex = exams.get(i - 1);
            long target = ex.s - g;
            int j = upperBound(ends, target);
            dp[i] = Math.max(dp[i - 1], dp[j] + ex.w);
        }
        return dp[n];
    }

    private int upperBound(long[] a, long x) {
        int l = 0, r = a.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (a[m] <= x) l = m + 1;
            else r = m;
        }
        return l;
    }
}
