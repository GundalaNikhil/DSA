import java.util.*;

class Solution {
    static class Point {
        double x, y;
        Point(double x, double y) { this.x = x; this.y = y; }
    }

    private double dist(Point p, Point q) {
        return Math.hypot(p.x - q.x, p.y - q.y);
    }

    private double distToEdge(Point p, int xL, int yB, int xR, int yT) {
        return Math.min(Math.min(p.x - xL, xR - p.x), Math.min(p.y - yB, yT - p.y));
    }

    private boolean insideRect(Point p, int xL, int yB, int xR, int yT) {
        double EPS = 1e-12;
        return p.x >= xL - EPS && p.x <= xR + EPS && p.y >= yB - EPS && p.y <= yT + EPS;
    }

    public double largestEmptyCircle(int xL, int yB, int xR, int yT, int[] xs, int[] ys) {
        int n = xs.length;
        List<Point> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new Point(xs[i], ys[i]));

        List<Point> candidates = new ArrayList<>();
        // Corners
        candidates.add(new Point(xL, yB));
        candidates.add(new Point(xL, yT));
        candidates.add(new Point(xR, yB));
        candidates.add(new Point(xR, yT));

        // Edge projections
        for (Point p : pts) {
            candidates.add(new Point(p.x, yB));
            candidates.add(new Point(p.x, yT));
            candidates.add(new Point(xL, p.y));
            candidates.add(new Point(xR, p.y));
        }

        // Midpoints
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                candidates.add(new Point((pts.get(i).x + pts.get(j).x) / 2.0, (pts.get(i).y + pts.get(j).y) / 2.0));
            }
        }

        // Circumcenters (small n)
        if (n <= 60) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    for (int k = j + 1; k < n; k++) {
                        Point a = pts.get(i), b = pts.get(j), c = pts.get(k);
                        double d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
                        if (Math.abs(d) < 1e-12) continue;
                        double ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
                        double uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
                        candidates.add(new Point(ux, uy));
                    }
                }
            }
        }

        double best = 0.0;
        for (Point c : candidates) {
            if (!insideRect(c, xL, yB, xR, yT)) continue;
            double r = distToEdge(c, xL, yB, xR, yT);
            for (Point p : pts) {
                r = Math.min(r, dist(c, p));
            }
            best = Math.max(best, r);
        }
        return best;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int xL = sc.nextInt(), yB = sc.nextInt(), xR = sc.nextInt(), yT = sc.nextInt();
        int n = sc.nextInt();
        int[] xs = new int[n];
        int[] ys = new int[n];
        for (int i = 0; i < n; i++) xs[i] = sc.nextInt();
        for (int i = 0; i < n; i++) ys[i] = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.printf("%.6f\n", sol.largestEmptyCircle(xL, yB, xR, yT, xs, ys));
        sc.close();
    }
}
