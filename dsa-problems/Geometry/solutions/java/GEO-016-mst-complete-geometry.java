import java.util.*;
import java.io.*;

class Main {
    static class Point {
        int x, y, id;
        Point(int x, int y, int id) { this.x = x; this.y = y; this.id = id; }
    }

    static class Edge implements Comparable<Edge> {
        int u, v;
        long weight;
        Edge(int u, int v, long weight) { this.u = u; this.v = v; this.weight = weight; }
        @Override
        public int compareTo(Edge other) { return Long.compare(this.weight, other.weight); }
    }

    static class DSU {
        int[] parent;
        DSU(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }
        boolean union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            if (rootI != rootJ) {
                parent[rootI] = rootJ;
                return true;
            }
            return false;
        }
    }

    static class BIT {
        long[] minVal;
        int[] id;
        int size;
        BIT(int n) {
            size = n;
            minVal = new long[n + 1];
            id = new int[n + 1];
            Arrays.fill(minVal, Long.MAX_VALUE);
            Arrays.fill(id, -1);
        }
        void update(int i, long val, int pId) {
            for (; i > 0; i -= i & -i) {
                if (val < minVal[i]) {
                    minVal[i] = val;
                    id[i] = pId;
                }
            }
        }
        int query(int i) {
            long minV = Long.MAX_VALUE;
            int resId = -1;
            for (; i <= size; i += i & -i) {
                if (minVal[i] < minV) {
                    minV = minVal[i];
                    resId = id[i];
                }
            }
            return resId;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        StringTokenizer st = new StringTokenizer(firstLine);
        if (!st.hasMoreTokens()) return;
        int n = Integer.parseInt(st.nextToken());
        
        Point[] pts = new Point[n];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            if (line == null) break;
            st = new StringTokenizer(line);
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pts[i] = new Point(x, y, i);
        }

        if (n <= 1) {
            System.out.println(0);
            return;
        }

        List<Edge> edges = new ArrayList<>();
        for (int s1 = 0; s1 < 2; s1++) {
            for (int s2 = 0; s2 < 2; s2++) {
                for (int swap = 0; swap < 2; swap++) {
                    Arrays.sort(pts, (a, b) -> a.x != b.x ? b.x - a.x : b.y - a.y);
                    
                    int[] ys = new int[n];
                    for (int i = 0; i < n; i++) ys[i] = pts[i].y - pts[i].x;
                    int[] sortedYs = ys.clone();
                    Arrays.sort(sortedYs);
                    Map<Integer, Integer> rank = new HashMap<>();
                    int r = 1;
                    if (n > 0) rank.put(sortedYs[0], r++);
                    for (int i = 1; i < n; i++) if (sortedYs[i] != sortedYs[i-1]) rank.put(sortedYs[i], r++);
                    
                    BIT bit = new BIT(r);
                    for (int i = 0; i < n; i++) {
                        int pos = rank.get(ys[i]);
                        int idx = bit.query(pos);
                        if (idx != -1) {
                            long d = Math.abs((long)pts[i].x - pts[idx].x) + Math.abs((long)pts[i].y - pts[idx].y);
                            edges.add(new Edge(pts[i].id, pts[idx].id, d));
                        }
                        bit.update(pos, (long)pts[i].x + pts[i].y, i);
                    }

                    for (Point p : pts) { int tmp = p.x; p.x = p.y; p.y = tmp; }
                }
                for (Point p : pts) p.y = -p.y;
            }
            for (Point p : pts) p.x = -p.x;
        }

        Collections.sort(edges);
        DSU dsu = new DSU(n);
        long mst = 0;
        int count = 0;
        for (Edge e : edges) {
            if (dsu.union(e.u, e.v)) {
                mst += e.weight;
                count++;
                if (count == n - 1) break;
            }
        }
        System.out.println(mst);
    }
}
