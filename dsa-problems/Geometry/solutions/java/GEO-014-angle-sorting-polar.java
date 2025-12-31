class Solution {
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
