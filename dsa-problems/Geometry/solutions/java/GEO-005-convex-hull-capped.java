import java.util.*;
import java.io.*;

class Main {

static class Solution {
    private long cross(long ox, long oy, long ax, long ay, long bx, long by) {
        return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox);
    }

    public List<long[]> cappedHull(long[] xs, long[] ys, int theta) {
        int n = xs.length;
        List<long[]> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new long[]{xs[i], ys[i]});
        pts.sort((a,b) -> a[0]==b[0] ? Long.compare(a[1], b[1]) : Long.compare(a[0], b[0]));
        List<long[]> unique = new ArrayList<>();
        long lastX = Long.MIN_VALUE, lastY = Long.MIN_VALUE;
        for (long[] p : pts) {
            if (p[0]!=lastX || p[1]!=lastY) { unique.add(p); lastX=p[0]; lastY=p[1]; }
        }
        pts = unique;
        if (pts.size() == 1) return pts;
        List<long[]> lower = new ArrayList<>();
        for (long[] p : pts) {
            while (lower.size() >= 2 && cross(lower.get(lower.size()-2)[0], lower.get(lower.size()-2)[1],
                                              lower.get(lower.size()-1)[0], lower.get(lower.size()-1)[1],
                                              p[0], p[1]) <= 0) {
                lower.remove(lower.size()-1);
            }
            lower.add(p);
        }
        List<long[]> upper = new ArrayList<>();
        for (int i = pts.size()-1; i>=0; i--) {
            long[] p = pts.get(i);
            while (upper.size() >= 2 && cross(upper.get(upper.size()-2)[0], upper.get(upper.size()-2)[1],
                                              upper.get(upper.size()-1)[0], upper.get(upper.size()-1)[1],
                                              p[0], p[1]) <= 0) {
                upper.remove(upper.size()-1);
            }
            upper.add(p);
        }
        List<long[]> hull = new ArrayList<>(lower);
        hull.remove(hull.size()-1);
        upper.remove(upper.size()-1);
        hull.addAll(upper);
        int h = hull.size();
        if (h <= 2) return hull;

        double cosT = Math.cos(Math.toRadians(theta));
        List<long[]> keep = new ArrayList<>();
        for (int i = 0; i < h; i++) {
            long[] prev = hull.get((i-1+h)%h);
            long[] curr = hull.get(i);
            long[] nxt = hull.get((i+1)%h);
            long ux = prev[0]-curr[0], uy = prev[1]-curr[1];
            long vx = nxt[0]-curr[0], vy = nxt[1]-curr[1];
            double lenU = Math.hypot(ux, uy), lenV = Math.hypot(vx, vy);
            if (lenU == 0 || lenV == 0) { keep.add(curr); continue; }
            double dot = ux*vx + uy*vy;
            double cosA = dot / (lenU * lenV);
            if (cosA <= cosT) keep.add(curr);
        }
        return keep;
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        try {
            if (!sc.hasNext()) return;
            int n = sc.nextInt();
            long[] xs = new long[n];
            long[] ys = new long[n];
            for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
            int theta = sc.nextInt();
            List<long[]> res = new Solution().cappedHull(xs, ys, theta);
            System.out.println(res.size());
            for(long[] p : res) System.out.println(p[0] + " " + p[1]);
        } finally {
            sc.close();
        }
    }
}
