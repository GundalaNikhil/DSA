import java.util.*;

class Solution {
    private static class Pt {
        long x, y;
        Pt(long x, long y){ this.x = x; this.y = y; }
    }

    public long closestPair(int[] xs, int[] ys) {
        int n = xs.length;
        Pt[] pts = new Pt[n];
        for (int i = 0; i < n; i++) pts[i] = new Pt(xs[i], ys[i]);
        Arrays.sort(pts, Comparator.comparingLong(p -> p.x));
        Pt[] tmp = new Pt[n];
        return solve(pts, 0, n, tmp);
    }

    private long dist2(Pt a, Pt b) {
        long dx = a.x - b.x, dy = a.y - b.y;
        return dx*dx + dy*dy;
    }

    private long solve(Pt[] a, int l, int r, Pt[] tmp) {
        int n = r - l;
        if (n <= 3) {
            long best = Long.MAX_VALUE;
            for (int i = l; i < r; i++)
                for (int j = i+1; j < r; j++)
                    best = Math.min(best, dist2(a[i], a[j]));
            Arrays.sort(a, l, r, Comparator.comparingLong(p -> p.y));
            return best;
        }
        int mid = (l + r) >>> 1;
        long midx = a[mid].x;
        long dl = solve(a, l, mid, tmp);
        long dr = solve(a, mid, r, tmp);
        long d = Math.min(dl, dr);

        // merge by y
        int i=l, j=mid, k=0;
        while (i<mid && j<r) tmp[k++] = (a[i].y <= a[j].y) ? a[i++] : a[j++];
        while (i<mid) tmp[k++] = a[i++];
        while (j<r) tmp[k++] = a[j++];
        System.arraycopy(tmp, 0, a, l, k);

        List<Pt> strip = new ArrayList<>();
        for (int t = l; t < r; t++) {
            long dx = a[t].x - midx;
            if (dx*dx < d) strip.add(a[t]);
        }
        for (int s = 0; s < strip.size(); s++) {
            for (int t = s+1; t < strip.size(); t++) {
                long dy = strip.get(t).y - strip.get(s).y;
                if (dy*dy >= d) break;
                d = Math.min(d, dist2(strip.get(s), strip.get(t)));
            }
        }
        return d;
    }
}
