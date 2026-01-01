import java.util.*;
import java.io.*;

class Main {

static class Solution {
    private boolean onSegment(long xi, long yi, long xj, long yj, long qx, long qy) {
        long cross = (xj - xi) * (qy - yi) - (yj - yi) * (qx - xi);
        if (cross != 0) return false;
        return Math.min(xi, xj) <= qx && qx <= Math.max(xi, xj)
            && Math.min(yi, yj) <= qy && qy <= Math.max(yi, yj);
    }

    public String pointInPolygon(long[] xs, long[] ys, long qx, long qy) {
        int n = xs.length;
        int wn = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            long xi = xs[i], yi = ys[i];
            long xj = xs[j], yj = ys[j];
            if (onSegment(xi, yi, xj, yj, qx, qy)) return "boundary";
            long cross = (xj - xi) * (qy - yi) - (yj - yi) * (qx - xi);
            if (yi <= qy && yj > qy && cross > 0) wn++;
            if (yi > qy && yj <= qy && cross < 0) wn--;
        }
        return wn != 0 ? "inside" : "outside";
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        long qx = sc.nextLong(); long qy = sc.nextLong();
        System.out.println(new Solution().pointInPolygon(xs, ys, qx, qy));
    }
}
