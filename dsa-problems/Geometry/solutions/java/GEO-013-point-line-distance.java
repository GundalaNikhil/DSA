import java.util.*;
import java.io.*;

class Main {
static class Solution {
    public double distancePointSegment(long x1, long y1, long x2, long y2, long px, long py) {
        long ux = x2 - x1, uy = y2 - y1;
        long vx = px - x1, vy = py - y1;
        long denom = ux*ux + uy*uy;
        if (denom == 0) return Math.hypot(vx, vy);
        double t = (ux * (double)vx + uy * (double)vy) / denom;
        t = Math.max(0.0, Math.min(1.0, t));
        double cx = x1 + t * ux;
        double cy = y1 + t * uy;
        return Math.hypot(px - cx, py - cy);
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        long x1 = sc.nextLong(); long y1 = sc.nextLong();
        long x2 = sc.nextLong(); long y2 = sc.nextLong();
        long px = sc.nextLong(); long py = sc.nextLong();
        System.out.printf("%.6f\n", new Solution().distancePointSegment(x1, y1, x2, y2, px, py));
    }
}
