import java.util.*;

class Solution {
    static class Point {
        double x, y;
        Point(double x, double y) { this.x = x; this.y = y; }
    }

    private double getRadius(double x, double y, int xL, int yB, int xR, int yT, List<Point> pts) {
        double EPS = 1e-12;
        if (x < xL - EPS || x > xR + EPS || y < yB - EPS || y > yT + EPS) return 0.0;
        
        double r = Math.min(Math.min(x - xL, xR - x), Math.min(y - yB, yT - y));
        if (r <= EPS) return 0.0;
        
        for (Point p : pts) {
            double d2 = (x - p.x) * (x - p.x) + (y - p.y) * (y - p.y);
            if (d2 < r * r) return Math.sqrt(d2);
        }
        return r;
    }

    public double largestEmptyCircle(int xL, int yB, int xR, int yT, int[] xs, int[] ys) {
        int n = xs.length;
        List<Point> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new Point(xs[i], ys[i]));

        List<Point> candidates = new ArrayList<>();
        candidates.add(new Point((xL + xR) / 2.0, (yB + yT) / 2.0));
        
        for (Point p : pts) {
            candidates.add(new Point(p.x, (p.y + yB) / 2.0));
            candidates.add(new Point(p.x, (p.y + yT) / 2.0));
            candidates.add(new Point((p.x + xL) / 2.0, p.y));
            candidates.add(new Point((p.x + xR) / 2.0, p.y));
        }

        if (n <= 100) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    candidates.add(new Point((pts.get(i).x + pts.get(j).x) / 2.0, 
                                            (pts.get(i).y + pts.get(j).y) / 2.0));
                }
            }
        }
        
        int GRID = 12;
        for(int i=0; i<=GRID; i++) {
            for(int j=0; j<=GRID; j++) {
                double gx = xL + (double)(xR - xL) * i / GRID;
                double gy = yB + (double)(yT - yB) * j / GRID;
                candidates.add(new Point(gx, gy));
            }
        }

        PriorityQueue<Point> pq = new PriorityQueue<>((a, b) -> 
            Double.compare(getRadius(b.x, b.y, xL, yB, xR, yT, pts), 
                           getRadius(a.x, a.y, xL, yB, xR, yT, pts)));
        pq.addAll(candidates);

        List<Point> starts = new ArrayList<>();
        for(int i=0; i<40 && !pq.isEmpty(); i++) starts.add(pq.poll());
        
        double best = 0.0;
        if (!starts.isEmpty()) best = getRadius(starts.get(0).x, starts.get(0).y, xL, yB, xR, yT, pts);

        double stepSize = Math.max(xR - xL, yT - yB) / 2.0;
        double precision = 1e-7;
        Random rand = new Random(1337);
        
        for (Point start : starts) {
            double currX = start.x;
            double currY = start.y;
            double currR = getRadius(currX, currY, xL, yB, xR, yT, pts);
            double tempStep = stepSize;
            
            while (tempStep > precision) {
                boolean improved = false;
                double bestNeighR = currR;
                double bestNeighX = currX, bestNeighY = currY;
                
                double angle = rand.nextDouble() * 2 * Math.PI;
                for(int k=0; k<8; k++) {
                    double a = angle + k * (Math.PI / 4.0);
                    double dx = Math.cos(a);
                    double dy = Math.sin(a);
                    
                    double nx = currX + dx * tempStep;
                    double ny = currY + dy * tempStep;
                    nx = Math.max(xL, Math.min(xR, nx));
                    ny = Math.max(yB, Math.min(yT, ny));
                    
                    double nr = getRadius(nx, ny, xL, yB, xR, yT, pts);
                    if (nr > bestNeighR) {
                        bestNeighR = nr;
                        bestNeighX = nx;
                        bestNeighY = ny;
                        improved = true;
                    }
                }
                
                if (improved) {
                    currX = bestNeighX;
                    currY = bestNeighY;
                    currR = bestNeighR;
                } else {
                    tempStep *= 0.85;
                }
            }
            
            best = Math.max(best, currR);
        }
        
        return best;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int xL = sc.nextInt(), yB = sc.nextInt(), xR = sc.nextInt(), yT = sc.nextInt();
        int n = sc.nextInt();
        int[] xs = new int[n];
        int[] ys = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = sc.nextInt();
            ys[i] = sc.nextInt();
        }
        
        Solution sol = new Solution();
        System.out.printf("%.6f\n", sol.largestEmptyCircle(xL, yB, xR, yT, xs, ys));
        sc.close();
    }
}
