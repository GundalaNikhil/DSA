import java.util.*;
import java.io.*;

class Main {
    static class Solution {
        static class Event {
            long x;
            int type;
            int l, r;
            Event(long x, int type, int l, int r) {
                this.x = x;
                this.type = type;
                this.l = l;
                this.r = r;
            }
        }

        private int[] add;
        private int[] mx;

        private void update(int node, int l, int r, int ql, int qr, int val) {
            if (qr <= l || r <= ql) return;
            if (ql <= l && r <= qr) {
                int realVal = -val;
                add[node] += realVal;
                mx[node] += realVal;
                return;
            }
            int mid = (l + r) / 2;
            update(node * 2, l, mid, ql, qr, val);
            update(node * 2 + 1, mid, r, ql, qr, val);
            mx[node] = add[node] + Math.max(mx[node * 2], mx[node * 2 + 1]);
        }

        public int maxOverlap(long[] x1, long[] y1, long[] x2, long[] y2) {
            int n = x1.length;
            if (n == 0) return 0;
            List<Long> ys = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                ys.add(y1[i]);
                ys.add(y2[i]);
            }
            Collections.sort(ys);
            List<Long> unique = new ArrayList<>();
            for (long v : ys) {
                if (unique.isEmpty() || unique.get(unique.size() - 1) != v) unique.add(v);
            }
            ys = unique;
            int m = ys.size();
            if (m == 0) return 0;
            Map<Long, Integer> ymap = new HashMap<>();
            for (int i = 0; i < ys.size(); i++) ymap.put(ys.get(i), i);

            List<Event> events = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                int l = ymap.get(y1[i]);
                int r = ymap.get(y2[i]) + 1;
                events.add(new Event(x1[i], -1, l, r));
                events.add(new Event(x2[i], 1, l, r));
            }
            events.sort((a, b) -> {
                if (a.x != b.x) return Long.compare(a.x, b.x);
                return Integer.compare(a.type, b.type);
            });

            add = new int[4 * m];
            mx = new int[4 * m];
            int ans = 0;
            for (Event e : events) {
                update(1, 0, m, e.l, e.r, e.type);
                ans = Math.max(ans, mx[1]);
            }
            return ans;
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int m = sc.nextInt();
        long[] x1 = new long[m]; long[] y1 = new long[m];
        long[] x2 = new long[m]; long[] y2 = new long[m];
        for(int i=0; i<m; i++) {
            x1[i] = sc.nextLong(); y1[i] = sc.nextLong();
            x2[i] = sc.nextLong(); y2[i] = sc.nextLong();
        }
        System.out.println(new Solution().maxOverlap(x1, y1, x2, y2));
    }
}
