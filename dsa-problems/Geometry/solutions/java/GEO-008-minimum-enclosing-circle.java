import java.util.*;

class Solution {
    static class Circle { double x,y,r; Circle(double x,double y,double r){this.x=x;this.y=y;this.r=r;} }

    private double dist(double x1, double y1, double x2, double y2) {
        double dx = x1 - x2, dy = y1 - y2;
        return Math.hypot(dx, dy);
    }
    private Circle fromTwo(double x1, double y1, double x2, double y2) {
        double cx = (x1 + x2) / 2.0, cy = (y1 + y2) / 2.0;
        double r = dist(x1, y1, x2, y2) / 2.0;
        return new Circle(cx, cy, r);
    }
    private Circle fromThree(double x1, double y1, double x2, double y2, double x3, double y3) {
        double d = 2*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2));
        if (Math.abs(d) < 1e-15) return new Circle(0,0,-1);
        double ux = ((x1*x1+y1*y1)*(y2-y3) + (x2*x2+y2*y2)*(y3-y1) + (x3*x3+y3*y3)*(y1-y2)) / d;
        double uy = ((x1*x1+y1*y1)*(x3-x2) + (x2*x2+y2*y2)*(x1-x3) + (x3*x3+y3*y3)*(x2-x1)) / d;
        double r = dist(ux, uy, x1, y1);
        return new Circle(ux, uy, r);
    }
    private boolean inside(double px, double py, Circle c) {
        return dist(px, py, c.x, c.y) <= c.r + 1e-12;
    }

    public double[] minEnclosingCircle(int[] xs, int[] ys) {
        int n = xs.length;
        List<int[]> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new int[]{xs[i], ys[i]});
        Collections.shuffle(pts, new Random());
        Circle c = new Circle(pts.get(0)[0], pts.get(0)[1], 0);
        for (int i = 1; i < n; i++) {
            int[] p = pts.get(i);
            if (inside(p[0], p[1], c)) continue;
            c = new Circle(p[0], p[1], 0);
            for (int j = 0; j < i; j++) {
                int[] q = pts.get(j);
                if (inside(q[0], q[1], c)) continue;
                c = fromTwo(p[0], p[1], q[0], q[1]);
                for (int k = 0; k < j; k++) {
                    int[] r = pts.get(k);
                    if (inside(r[0], r[1], c)) continue;
                    c = fromThree(p[0], p[1], q[0], q[1], r[0], r[1]);
                }
            }
        }
        return new double[]{c.x, c.y, c.r};
    }
}
