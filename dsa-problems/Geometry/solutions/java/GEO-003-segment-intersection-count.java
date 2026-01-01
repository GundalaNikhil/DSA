import java.util.*;
import java.io.*;

class Main {
import java.util.*;

static class Solution {
    private static class Segment {
        long x1, y1, x2, y2;
        Segment(long a, long b, long c, long d){ x1=a; y1=b; x2=c; y2=d; }
        boolean isLeft() { return x1 < x2 || (x1 == x2 && y1 <= y2); }
    }

    private static int orient(long ax, long ay, long bx, long by, long cx, long cy) {
        long v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
        return Long.compare(v, 0);
    }

    private static boolean onSeg(long ax, long ay, long bx, long by, long cx, long cy) {
        return orient(ax, ay, bx, by, cx, cy) == 0 &&
               Math.min(ax, bx) <= cx && cx <= Math.max(ax, bx) &&
               Math.min(ay, by) <= cy && cy <= Math.max(ay, by);
    }

    private static boolean intersects(Segment s, Segment t) {
        int o1 = orient(s.x1, s.y1, s.x2, s.y2, t.x1, t.y1);
        int o2 = orient(s.x1, s.y1, s.x2, s.y2, t.x2, t.y2);
        int o3 = orient(t.x1, t.y1, t.x2, t.y2, s.x1, s.y1);
        int o4 = orient(t.x1, t.y1, t.x2, t.y2, s.x2, s.y2);
        if (o1 == 0 && onSeg(s.x1, s.y1, s.x2, s.y2, t.x1, t.y1)) return true;
        if (o2 == 0 && onSeg(s.x1, s.y1, s.x2, s.y2, t.x2, t.y2)) return true;
        if (o3 == 0 && onSeg(t.x1, t.y1, t.x2, t.y2, s.x1, s.y1)) return true;
        if (o4 == 0 && onSeg(t.x1, t.y1, t.x2, t.y2, s.x2, s.y2)) return true;
        return (long)o1 * o2 < 0 && (long)o3 * o4 < 0;
    }

    public long countIntersections(int[] x1, int[] y1, int[] x2, int[] y2) {
        int m = x1.length;
        Segment[] segs = new Segment[m];
        for (int i = 0; i < m; i++) segs[i] = new Segment(x1[i], y1[i], x2[i], y2[i]);

        class Event implements Comparable<Event> {
            long x; int type; int id; long y;
            Event(long x, int type, int id, long y){ this.x=x; this.type=type; this.id=id; this.y=y; }
            public int compareTo(Event o){
                if (x != o.x) return Long.compare(x, o.x);
                if (type != o.type) return Integer.compare(type, o.type); // start before end
                return Long.compare(y, o.y);
            }
        }

        List<Event> evs = new ArrayList<>(2*m);
        for (int i = 0; i < m; i++) {
            Segment s = segs[i];
            boolean left = s.isLeft();
            long sx = left ? s.x1 : s.x2;
            long sy = left ? s.y1 : s.y2;
            long ex = left ? s.x2 : s.x1;
            long ey = left ? s.y2 : s.y1;
            evs.add(new Event(sx, 0, i, sy));
            evs.add(new Event(ex, 1, i, ey));
        }
        Collections.sort(evs);

        TreeSet<Integer> status = new TreeSet<>((a,b)->{
            if (a.equals(b)) return 0;
            Segment sa=segs[a], sb=segs[b];
            // compare by y at currentX (global var)
            double ya = sa.y1 + (sa.y2 - sa.y1) * (curX - sa.x1) / (double)(sa.x2 - sa.x1);
            double yb = sb.y1 + (sb.y2 - sb.y1) * (curX - sb.x1) / (double)(sb.x2 - sb.x1);
            if (ya == yb) return Integer.compare(a,b);
            return ya < yb ? -1 : 1;
        });

        long ans = 0;
        for (Event e : evs) {
            curX = e.x;
            int id = e.id;
            if (e.type == 0) { // start
                status.add(id);
                Integer lower = status.lower(id), higher = status.higher(id);
                if (lower != null && intersects(segs[id], segs[lower])) ans++;
                if (higher != null && intersects(segs[id], segs[higher])) ans++;
            } else { // end
                Integer lower = status.lower(id), higher = status.higher(id);
                if (lower != null && higher != null && intersects(segs[lower], segs[higher])) ans++;
                status.remove(id);
            }
        }
        return ans;
    }

    private double curX = 0; // updated per event
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
        System.out.println(new Solution().countIntersections(x1, y1, x2, y2));
    }
}
