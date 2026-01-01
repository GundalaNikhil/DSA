import java.util.*;
import java.io.*;

class Main {
static class Solution {
    private long cross(long ax, long ay, long bx, long by, long cx, long cy) {
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
    }
    private long dist2(long ax, long ay, long bx, long by) {
        long dx = ax - bx, dy = ay - by;
        return dx*dx + dy*dy;
    }
    public long diameterSquared(long[] xs, long[] ys) {
        int n = xs.length;
        if (n <= 1) return 0;
        long best = 0;
        int j = 1;
        for (int i = 0; i < n; i++) {
            int ni = (i + 1) % n;
            while (cross(xs[i], ys[i], xs[ni], ys[ni], xs[(j+1)%n], ys[(j+1)%n]) >
                   cross(xs[i], ys[i], xs[ni], ys[ni], xs[j], ys[j])) {
                j = (j + 1) % n;
            }
            best = Math.max(best, dist2(xs[i], ys[i], xs[j], ys[j]));
            best = Math.max(best, dist2(xs[ni], ys[ni], xs[j], ys[j]));
        }
        return best;
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        System.out.println(new Solution().diameterSquared(xs, ys));
    }
}
