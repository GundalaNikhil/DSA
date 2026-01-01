import java.util.*;
import java.io.*;

class Main {
static class Solution {
    public List<long[]> sortByAngle(int[] xs, int[] ys) {
        int n = xs.length;
        List<long[]> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new long[]{xs[i], ys[i]});
        pts.sort((a, b) -> {
            int ha = (a[1] > 0 || (a[1] == 0 && a[0] > 0)) ? 0 : 1;
            int hb = (b[1] > 0 || (b[1] == 0 && b[0] > 0)) ? 0 : 1;
            if (ha != hb) return ha - hb;
            long cross = a[0]*b[1] - a[1]*b[0];
            if (cross != 0) return cross > 0 ? -1 : 1;
            long ra = a[0]*a[0] + a[1]*a[1];
            long rb = b[0]*b[0] + b[1]*b[1];
            return Long.compare(ra, rb);
        });
        return pts;
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        List<long[]> res = new Solution().sortByAngle(xs, ys);
        for(long[] p : res) System.out.println(p[0] + " " + p[1]);
    }
}
