import java.util.*;
import java.io.*;

class Main {
    static class Solution {
        static class Event {
            long x, y1, y2, w;
            int type;
            Event(long x, int type, long y1, long y2, long w) {
                this.x = x;
                this.type = type;
                this.y1 = y1;
                this.y2 = y2;
                this.w = w;
            }
        }

        public long weightedArea(long[] x1, long[] y1, long[] x2, long[] y2, long[] w, long W) {
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
            int m = ys.size() - 1;
            if (m <= 0) return 0;

            long[] widths = new long[m];
            for (int i = 0; i < m; i++) widths[i] = ys.get(i + 1) - ys.get(i);
            Map<Long, Integer> ymap = new HashMap<>();
            for (int i = 0; i < ys.size(); i++) ymap.put(ys.get(i), i);

            List<Event> events = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                events.add(new Event(x1[i], 1, y1[i], y2[i], w[i]));
                events.add(new Event(x2[i], -1, y1[i], y2[i], w[i]));
            }
            events.sort((a, b) -> {
                if (a.x != b.x) return Long.compare(a.x, b.x);
                return Integer.compare(a.type, b.type);
            });

            long[] curr = new long[m];
            long totalArea = 0;
            long prevX = events.get(0).x;
            for (int i = 0; i < events.size(); i++) {
                Event e = events.get(i);
                if (i > 0) {
                    long width = e.x - prevX;
                    if (width > 0) {
                        long covered = 0;
                        for (int j = 0; j < m; j++) {
                            if (curr[j] >= W) covered += widths[j];
                        }
                        totalArea += covered * width;
                    }
                }
                int l = ymap.get(e.y1);
                int r = ymap.get(e.y2);
                long delta = e.w * e.type;
                for (int j = l; j < r; j++) curr[j] += delta;
                prevX = e.x;
            }
            return totalArea;
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int m = sc.nextInt();
        int W = sc.nextInt();
        long[] x1 = new long[m]; long[] y1 = new long[m];
        long[] x2 = new long[m]; long[] y2 = new long[m]; long[] w = new long[m];
        for(int i=0; i<m; i++) {
            x1[i] = sc.nextLong(); y1[i] = sc.nextLong();
            x2[i] = sc.nextLong(); y2[i] = sc.nextLong(); w[i] = sc.nextLong();
        }
        System.out.println(new Solution().weightedArea(x1, y1, x2, y2, w, W));
    }
}
