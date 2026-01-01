import java.util.*;

class Main {
    static class Candidate implements Comparable<Candidate> {
        double x, y, r;
        Candidate(double x, double y, double r) { this.x = x; this.y = y; this.r = r; }
        @Override
        public int compareTo(Candidate other) {
            return Double.compare(other.r, this.r);
        }
    }

    private static double getRadius(double x, double y, int xL, int yB, int xR, int yT, int n, int[] xs, int[] ys, int[] rs) {
        double r = Math.min(Math.min(x - xL, xR - x), Math.min(y - yB, yT - y));
        if (r <= 0) return 0.0;
        for (int i = 0; i < n; i++) {
            double d = Math.sqrt((x - xs[i]) * (x - xs[i]) + (y - ys[i]) * (y - ys[i]));
            r = Math.min(r, d - rs[i]);
            if (r <= 0) return 0.0;
        }
        return r;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int xL = sc.nextInt(), yB = sc.nextInt(), xR = sc.nextInt(), yT = sc.nextInt();
        int n = sc.nextInt();
        int[] xs = new int[n], ys = new int[n], rs = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = sc.nextInt();
            ys[i] = sc.nextInt();
            rs[i] = sc.nextInt();
        }

        List<Candidate> cands = new ArrayList<>();
        int gridRes = 120;
        for (int i = 0; i <= gridRes; i++) {
            double cx = xL + (xR - xL) * i / (double)gridRes;
            for (int j = 0; j <= gridRes; j++) {
                double cy = yB + (yT - yB) * j / (double)gridRes;
                double r = getRadius(cx, cy, xL, yB, xR, yT, n, xs, ys, rs);
                if (r > 0) cands.add(new Candidate(cx, cy, r));
            }
        }
        
        for (int i = 0; i < n; i++) {
            cands.add(new Candidate(xs[i], yB, getRadius(xs[i], yB, xL, yB, xR, yT, n, xs, ys, rs)));
            cands.add(new Candidate(xs[i], yT, getRadius(xs[i], yT, xL, yB, xR, yT, n, xs, ys, rs)));
            cands.add(new Candidate(xL, ys[i], getRadius(xL, ys[i], xL, yB, xR, yT, n, xs, ys, rs)));
            cands.add(new Candidate(xR, ys[i], getRadius(xR, ys[i], xL, yB, xR, yT, n, xs, ys, rs)));
            for (int j = i+1; j < n; j++) {
                double mx = (xs[i] + xs[j]) / 2.0;
                double my = (ys[i] + ys[j]) / 2.0;
                cands.add(new Candidate(mx, my, getRadius(mx, my, xL, yB, xR, yT, n, xs, ys, rs)));
            }
        }

        double bestR = 0.0;
        if (cands.isEmpty()) {
            bestR = Math.max(bestR, getRadius((xL + xR)/2.0, (yB + yT)/2.0, xL, yB, xR, yT, n, xs, ys, rs));
        } else {
            Collections.sort(cands);
            int count = 0;
            Set<String> seen = new HashSet<>();
            for (Candidate cand : cands) {
                if (count >= 60) break;
                String key = Math.round(cand.x * 10) + "_" + Math.round(cand.y * 10);
                if (seen.contains(key)) continue;
                seen.add(key);
                count++;
                
                double currX = cand.x, currY = cand.y, currR = cand.r;
                double step = Math.max(xR - xL, yT - yB) / (double)gridRes;
                while (step > 1e-13) {
                    boolean improved = false;
                    double[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}, {0.7,0.7}, {0.7,-0.7}, {-0.7,0.7}, {-0.7,-0.7}, {0.3,0.9}, {0.9,0.3}};
                    for (double[] d : dirs) {
                        double nx = currX + d[0] * step, ny = currY + d[1] * step;
                        if (nx >= xL && nx <= xR && ny >= yB && ny <= yT) {
                            double nr = getRadius(nx, ny, xL, yB, xR, yT, n, xs, ys, rs);
                            if (nr > currR) {
                                currR = nr; currX = nx; currY = ny;
                                improved = true;
                            }
                        }
                    }
                    if (!improved) step *= 0.5;
                }
                bestR = Math.max(bestR, currR);
            }
        }
        System.out.printf("%.6f\n", Math.max(0.0, bestR));
        sc.close();
    }
}
