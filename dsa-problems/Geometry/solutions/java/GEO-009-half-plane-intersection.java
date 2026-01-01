import java.util.*;
import java.io.*;

class Main {
    static class Solution {
        private static final double EPS = 1e-9;

        private static class Line {
            double a, b, c, ang;
            Line(double a, double b, double c) {
                this.a = a;
                this.b = b;
                this.c = c;
                this.ang = Math.atan2(b, a);
            }
        }

        private double norm(Line l) {
            return Math.hypot(l.a, l.b);
        }

        private double[] intersect(Line l1, Line l2) {
            double det = l1.a * l2.b - l2.a * l1.b;
            if (Math.abs(det) < EPS) return null;
            double x = (l1.c * l2.b - l2.c * l1.b) / det;
            double y = (l1.a * l2.c - l2.a * l1.c) / det;
            return new double[]{x, y};
        }

        private boolean outside(double[] p, Line l) {
            return l.a * p[0] + l.b * p[1] - l.c > EPS;
        }

        private Line secondLast(Deque<Line> dq) {
            Iterator<Line> it = dq.descendingIterator();
            it.next();
            return it.next();
        }

        private Line secondFirst(Deque<Line> dq) {
            Iterator<Line> it = dq.iterator();
            it.next();
            return it.next();
        }

        public List<double[]> halfPlaneIntersection(long[] A, long[] B, long[] C) {
            int n = A.length;
            List<Line> lines = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                lines.add(new Line(A[i], B[i], C[i]));
            }
            lines.sort((l1, l2) -> {
                if (Math.abs(l1.ang - l2.ang) > EPS) return Double.compare(l1.ang, l2.ang);
                double o1 = l1.c / norm(l1);
                double o2 = l2.c / norm(l2);
                return Double.compare(o1, o2);
            });

            List<Line> pruned = new ArrayList<>();
            for (Line l : lines) {
                if (!pruned.isEmpty() && Math.abs(l.ang - pruned.get(pruned.size() - 1).ang) < EPS) {
                    Line prev = pruned.get(pruned.size() - 1);
                    if (l.c / norm(l) < prev.c / norm(prev)) {
                        pruned.set(pruned.size() - 1, l);
                    }
                } else {
                    pruned.add(l);
                }
            }
            lines = pruned;

            Deque<Line> dq = new ArrayDeque<>();
            for (Line l : lines) {
                while (dq.size() >= 2) {
                    double[] p = intersect(secondLast(dq), dq.peekLast());
                    if (p == null || !outside(p, l)) break;
                    dq.removeLast();
                }
                while (dq.size() >= 2) {
                    double[] p = intersect(dq.peekFirst(), secondFirst(dq));
                    if (p == null || !outside(p, l)) break;
                    dq.removeFirst();
                }
                dq.addLast(l);
            }

            while (dq.size() >= 3) {
                double[] p = intersect(secondLast(dq), dq.peekLast());
                if (p == null || !outside(p, dq.peekFirst())) break;
                dq.removeLast();
            }
            while (dq.size() >= 3) {
                double[] p = intersect(dq.peekFirst(), secondFirst(dq));
                if (p == null || !outside(p, dq.peekLast())) break;
                dq.removeFirst();
            }

            if (dq.size() < 3) return Collections.emptyList();

            List<Line> dqList = new ArrayList<>(dq);
            List<double[]> pts = new ArrayList<>();
            for (int i = 0; i < dqList.size(); i++) {
                Line l1 = dqList.get(i);
                Line l2 = dqList.get((i + 1) % dqList.size());
                double[] p = intersect(l1, l2);
                if (p == null) return Collections.emptyList();
                pts.add(p);
            }

            List<double[]> unique = new ArrayList<>();
            for (double[] p : pts) {
                if (unique.isEmpty()) {
                    unique.add(p);
                } else {
                    double[] last = unique.get(unique.size() - 1);
                    if (Math.hypot(p[0] - last[0], p[1] - last[1]) > EPS) {
                        unique.add(p);
                    }
                }
            }
            if (unique.size() > 1) {
                double[] first = unique.get(0);
                double[] last = unique.get(unique.size() - 1);
                if (Math.hypot(first[0] - last[0], first[1] - last[1]) < EPS) {
                    unique.remove(unique.size() - 1);
                }
            }
            if (unique.size() < 3) return Collections.emptyList();

            int idx = 0;
            for (int i = 1; i < unique.size(); i++) {
                double[] p = unique.get(i);
                double[] best = unique.get(idx);
                if (p[0] < best[0] - EPS || (Math.abs(p[0] - best[0]) < EPS && p[1] < best[1])) {
                    idx = i;
                }
            }
            List<double[]> res = new ArrayList<>();
            for (int i = 0; i < unique.size(); i++) {
                res.add(unique.get((idx + i) % unique.size()));
            }
            return res;
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int m = sc.nextInt();
        long[] A = new long[m]; long[] B = new long[m]; long[] C = new long[m];
        for(int i=0; i<m; i++) { A[i] = sc.nextLong(); B[i] = sc.nextLong(); C[i] = sc.nextLong(); }
        List<double[]> res = new Solution().halfPlaneIntersection(A, B, C);
        if(res.isEmpty()) System.out.println("EMPTY");
        else {
            System.out.println(res.size());
            for(double[] p : res) {
                double x = Math.abs(p[0]) < 1e-9 ? 0.0 : p[0];
                double y = Math.abs(p[1]) < 1e-9 ? 0.0 : p[1];
                System.out.printf("%.6f %.6f\n", x, y);
            }
        }
    }
}
