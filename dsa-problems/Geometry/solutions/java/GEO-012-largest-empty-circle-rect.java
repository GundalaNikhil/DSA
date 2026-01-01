import java.util.*;

class Solution {
    static class Point {
        double x, y;
        Point(double x, double y) { this.x = x; this.y = y; }
    }

    static class PyRandom {
        private static final int N = 624;
        private static final int M = 397;
        private static final int MATRIX_A = 0x9908b0df;
        private static final int UPPER_MASK = 0x80000000;
        private static final int LOWER_MASK = 0x7fffffff;

        private final int[] mt = new int[N];
        private int mti = N + 1;

        PyRandom(int seed) {
            initByArray(new int[]{seed});
        }

        private void initGenrand(int s) {
            mt[0] = s;
            for (mti = 1; mti < N; mti++) {
                int prev = mt[mti - 1];
                mt[mti] = (int)(1812433253L * (prev ^ (prev >>> 30)) + mti);
            }
        }

        private void initByArray(int[] initKey) {
            initGenrand(19650218);
            int i = 1;
            int j = 0;
            int k = Math.max(N, initKey.length);
            for (; k > 0; k--) {
                int prev = mt[i - 1];
                mt[i] = (int)((mt[i] ^ ((prev ^ (prev >>> 30)) * 1664525L)) + initKey[j] + j);
                i++; j++;
                if (i >= N) { mt[0] = mt[N - 1]; i = 1; }
                if (j >= initKey.length) j = 0;
            }
            for (k = N - 1; k > 0; k--) {
                int prev = mt[i - 1];
                mt[i] = (int)((mt[i] ^ ((prev ^ (prev >>> 30)) * 1566083941L)) - i);
                i++;
                if (i >= N) { mt[0] = mt[N - 1]; i = 1; }
            }
            mt[0] = 0x80000000;
        }

        private int genrandInt32() {
            int y;
            int[] mag01 = {0x0, MATRIX_A};
            if (mti >= N) {
                int kk;
                for (kk = 0; kk < N - M; kk++) {
                    y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK);
                    mt[kk] = mt[kk + M] ^ (y >>> 1) ^ mag01[y & 0x1];
                }
                for (; kk < N - 1; kk++) {
                    y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK);
                    mt[kk] = mt[kk + (M - N)] ^ (y >>> 1) ^ mag01[y & 0x1];
                }
                y = (mt[N - 1] & UPPER_MASK) | (mt[0] & LOWER_MASK);
                mt[N - 1] = mt[M - 1] ^ (y >>> 1) ^ mag01[y & 0x1];
                mti = 0;
            }
            y = mt[mti++];
            y ^= (y >>> 11);
            y ^= (y << 7) & 0x9d2c5680;
            y ^= (y << 15) & 0xefc60000;
            y ^= (y >>> 18);
            return y;
        }

        double random() {
            int a = genrandInt32() >>> 5;
            int b = genrandInt32() >>> 6;
            return (a * 67108864.0 + b) / 9007199254740992.0;
        }

        int getrandbits(int k) {
            if (k <= 0) return 0;
            return genrandInt32() >>> (32 - k);
        }

        int randbelow(int n) {
            if (n <= 1) return 0;
            int t = n;
            int k = 0;
            while (t > 0) {
                k++;
                t >>= 1;
            }
            int r;
            do { r = getrandbits(k); } while (r >= n);
            return r;
        }
    }

    private double getRadius(double x, double y, int xL, int yB, int xR, int yT, List<Point> pts) {
        double EPS = 1e-12;
        if (x < xL - EPS || x > xR + EPS || y < yB - EPS || y > yT + EPS) return 0.0;
        
        double r = Math.min(Math.min(x - xL, xR - x), Math.min(y - yB, yT - y));
        if (r <= EPS) return 0.0;
        
        double minD2 = Double.POSITIVE_INFINITY;
        for (Point p : pts) {
            double d2 = (x - p.x) * (x - p.x) + (y - p.y) * (y - p.y);
            if (d2 < minD2) minD2 = d2;
            if (d2 < r * r) return Math.sqrt(d2);
        }
        return Math.min(r, Math.sqrt(minD2));
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

        double best = 0.0;
        for (Point c : candidates) best = Math.max(best, getRadius(c.x, c.y, xL, yB, xR, yT, pts));

        PyRandom rand = new PyRandom(1337);
        List<Point> starts = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            double sx = xL + rand.random() * (xR - xL);
            double sy = yB + rand.random() * (yT - yB);
            starts.add(new Point(sx, sy));
        }
        if (!candidates.isEmpty()) {
            class Cand {
                Point p;
                double r;
                int idx;
                Cand(Point p, double r, int idx) { this.p = p; this.r = r; this.idx = idx; }
            }
            List<Cand> candScores = new ArrayList<>();
            for (int i = 0; i < candidates.size(); i++) {
                Point p = candidates.get(i);
                candScores.add(new Cand(p, getRadius(p.x, p.y, xL, yB, xR, yT, pts), i));
            }
            candScores.sort((a, b) -> {
                int cmp = Double.compare(b.r, a.r);
                if (cmp != 0) return cmp;
                if (a.p.x != b.p.x) return Double.compare(b.p.x, a.p.x);
                if (a.p.y != b.p.y) return Double.compare(b.p.y, a.p.y);
                return Integer.compare(a.idx, b.idx);
            });
            for (int i = 0; i < Math.min(candScores.size(), 5); i++) starts.add(candScores.get(i).p);
        }

        double stepSize = Math.max(xR - xL, yT - yB) / 2.0;
        double precision = 1e-4;
        List<Point> baseDirs = Arrays.asList(
            new Point(0, 1), new Point(0, -1), new Point(1, 0), new Point(-1, 0),
            new Point(0.7, 0.7), new Point(0.7, -0.7), new Point(-0.7, 0.7), new Point(-0.7, -0.7)
        );

        for (Point start : starts) {
            double currX = start.x;
            double currY = start.y;
            double currR = getRadius(currX, currY, xL, yB, xR, yT, pts);
            double tempStep = stepSize;
            
            while (tempStep > precision) {
                boolean improved = false;
                double bestNeighR = currR;
                double bestNeighX = currX, bestNeighY = currY;

                List<Point> dirs = new ArrayList<>(baseDirs);
                for (int i = dirs.size() - 1; i > 0; i--) {
                    int j = rand.randbelow(i + 1);
                    Point tmp = dirs.get(i);
                    dirs.set(i, dirs.get(j));
                    dirs.set(j, tmp);
                }
                for (Point d : dirs) {
                    double dx = d.x;
                    double dy = d.y;
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
                    tempStep *= 0.6;
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
