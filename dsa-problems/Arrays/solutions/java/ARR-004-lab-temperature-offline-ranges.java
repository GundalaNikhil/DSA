import java.io.InputStream;

class Solution {
    private static class SegmentTree {
        private final int n;
        private final long[] tree;
        private final long[] lazy;

        SegmentTree(int[] arr) {
            this.n = arr.length;
            this.tree = new long[4 * n];
            this.lazy = new long[4 * n];
            build(arr, 0, 0, n - 1);
        }

        private void build(int[] arr, int node, int start, int end) {
            if (start == end) {
                tree[node] = arr[start];
                return;
            }
            int mid = (start + end) >>> 1;
            build(arr, node * 2 + 1, start, mid);
            build(arr, node * 2 + 2, mid + 1, end);
            tree[node] = tree[node * 2 + 1] + tree[node * 2 + 2];
        }

        private void push(int node, int start, int end) {
            if (lazy[node] != 0) {
                tree[node] += lazy[node] * (end - start + 1L);
                if (start != end) {
                    lazy[node * 2 + 1] += lazy[node];
                    lazy[node * 2 + 2] += lazy[node];
                }
                lazy[node] = 0;
            }
        }

        void update(int l, int r, long val) {
            update(0, 0, n - 1, l, r, val);
        }

        private void update(int node, int start, int end, int l, int r, long val) {
            push(node, start, end);
            if (start > r || end < l) {
                return;
            }
            if (start >= l && end <= r) {
                lazy[node] += val;
                push(node, start, end);
                return;
            }
            int mid = (start + end) >>> 1;
            update(node * 2 + 1, start, mid, l, r, val);
            update(node * 2 + 2, mid + 1, end, l, r, val);
            tree[node] = tree[node * 2 + 1] + tree[node * 2 + 2];
        }

        long query(int l, int r) {
            return query(0, 0, n - 1, l, r);
        }

        private long query(int node, int start, int end, int l, int r) {
            push(node, start, end);
            if (start > r || end < l) {
                return 0;
            }
            if (start >= l && end <= r) {
                return tree[node];
            }
            int mid = (start + end) >>> 1;
            return query(node * 2 + 1, start, mid, l, r)
                    + query(node * 2 + 2, mid + 1, end, l, r);
        }
    }

    public long[] processTemperatureQueries(int[] temps, String[] types, int[] l, int[] r, long[] x) {
        SegmentTree st = new SegmentTree(temps);
        long[] results = new long[types.length];
        int outIdx = 0;
        for (int i = 0; i < types.length; i++) {
            if ("add".equals(types[i])) {
                st.update(l[i], r[i], x[i]);
            } else {
                results[outIdx++] = st.query(l[i], r[i]);
            }
        }
        if (outIdx == results.length) {
            return results;
        }
        long[] trimmed = new long[outIdx];
        System.arraycopy(results, 0, trimmed, 0, outIdx);
        return trimmed;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        Integer nObj = fs.nextInt();
        if (nObj == null) return;
        int n = nObj;
        int[] temps = new int[n];
        for (int i = 0; i < n; i++) temps[i] = fs.nextInt();
        int q = fs.nextInt();
        String[] types = new String[q];
        int[] l = new int[q];
        int[] r = new int[q];
        long[] x = new long[q];
        for (int i = 0; i < q; i++) {
            types[i] = fs.next();
            l[i] = fs.nextInt();
            r[i] = fs.nextInt();
            if ("add".equals(types[i])) {
                x[i] = fs.nextLong();
            }
        }

        Solution solution = new Solution();
        long[] result = solution.processTemperatureQueries(temps, types, l, r, x);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]);
            if (i + 1 < result.length) sb.append('\n');
        }
        System.out.print(sb.toString());
    }

    private static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0;
        private int len = 0;

        FastScanner(InputStream in) {
            this.in = in;
        }

        private int read() throws Exception {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        Integer nextInt() throws Exception {
            int c;
            do {
                c = read();
                if (c == -1) return null;
            } while (c <= ' ');
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }

        long nextLong() throws Exception {
            int c;
            do {
                c = read();
            } while (c <= ' ');
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            long val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }

        String next() throws Exception {
            int c;
            do {
                c = read();
            } while (c <= ' ');
            StringBuilder sb = new StringBuilder();
            while (c > ' ') {
                sb.append((char) c);
                c = read();
            }
            return sb.toString();
        }
    }
}
