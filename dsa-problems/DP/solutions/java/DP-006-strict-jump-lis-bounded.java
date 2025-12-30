import java.util.*;

class Solution {
    static class SegTree {
        int n;
        int[] t;
        SegTree(int n) {
            this.n = n;
            this.t = new int[4 * n];
        }
        void update(int idx, int val) { update(1, 0, n - 1, idx, val); }
        private void update(int node, int l, int r, int idx, int val) {
            if (l == r) { t[node] = Math.max(t[node], val); return; }
            int mid = (l + r) >>> 1;
            if (idx <= mid) update(node << 1, l, mid, idx, val);
            else update(node << 1 | 1, mid + 1, r, idx, val);
            t[node] = Math.max(t[node << 1], t[node << 1 | 1]);
        }
        int query(int ql, int qr) {
            if (ql > qr) return 0;
            return query(1, 0, n - 1, ql, qr);
        }
        private int query(int node, int l, int r, int ql, int qr) {
            if (qr < l || r < ql) return 0;
            if (ql <= l && r <= qr) return t[node];
            int mid = (l + r) >>> 1;
            return Math.max(query(node << 1, l, mid, ql, qr), query(node << 1 | 1, mid + 1, r, ql, qr));
        }
    }

    private static int lowerBound(long[] a, long x) {
        int l = 0, r = a.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (a[m] >= x) r = m;
            else l = m + 1;
        }
        return l;
    }

    private static int upperBound(long[] a, long x) {
        int l = 0, r = a.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (a[m] <= x) l = m + 1;
            else r = m;
        }
        return l;
    }

    public int longestBoundedDiffSubsequence(int[] arr, long d, long g) {
        int n = arr.length;
        long[] vals = new long[n];
        for (int i = 0; i < n; i++) vals[i] = arr[i];
        Arrays.sort(vals);
        int m = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || vals[i] != vals[i - 1]) vals[m++] = vals[i];
        }
        vals = Arrays.copyOf(vals, m);

        SegTree st = new SegTree(m);
        int ans = 1;

        for (int x0 : arr) {
            long x = x0;
            long lo = x - g;
            long hi = x - d;
            int L = lowerBound(vals, lo);
            int R = upperBound(vals, hi) - 1;
            int best = st.query(L, R);
            int dp = best + 1;

            int idx = lowerBound(vals, x);
            st.update(idx, dp);
            ans = Math.max(ans, dp);
        }
        return ans;
    }
}
