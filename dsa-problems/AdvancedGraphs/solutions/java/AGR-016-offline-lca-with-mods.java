import java.util.*;

class Solution {
    private int[] parent;
    private int[] depth;
    private int[][] up;
    private int LOG;
    private List<List<Integer>> adj;

    // DSU
    private int[] dsuParent;
    private int[] dsuSz;
    private Stack<int[]> history;

    public int[] offlineLca(int n, int[][] edges, String[] type, int[][] args) {
        // 1. Precompute Static LCA
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        LOG = 20;
        up = new int[n][LOG];
        depth = new int[n];
        parent = new int[n]; // Just for BFS/DFS

        dfsLCA(0, 0, -1); // Assume 0 is root

        // 2. Map Edges to Intervals
        Map<String, Integer> edgeStart = new HashMap<>();
        // Initial edges active from -1 (or 0)
        for (int[] e : edges) {
            int u = Math.min(e[0], e[1]);
            int v = Math.max(e[0], e[1]);
            edgeStart.put(u + "," + v, 0);
        }

        int q = type.length;
        List<EdgeInterval> intervals = new ArrayList<>();
        List<Query> queries = new ArrayList<>();

        for (int i = 0; i < q; i++) {
            String t = type[i];
            int u = args[i][0];
            int v = args[i][1];
            if (u > v) { int temp = u; u = v; v = temp; }

            if (t.equals("cut")) {
                String key = u + "," + v;
                if (edgeStart.containsKey(key)) {
                    int start = edgeStart.remove(key);
                    intervals.add(new EdgeInterval(start, i, u, v));
                }
            } else if (t.equals("link")) {
                edgeStart.put(u + "," + v, i + 1); // Active from next step.
            } else {
                queries.add(new Query(i, args[i][0], args[i][1])); // Use original u,v for query
            }
        }

        // Close open intervals
        for (Map.Entry<String, Integer> entry : edgeStart.entrySet()) {
            String[] parts = entry.getKey().split(",");
            int u = Integer.parseInt(parts[0]);
            int v = Integer.parseInt(parts[1]);
            intervals.add(new EdgeInterval(entry.getValue(), q, u, v));
        }

        // 3. Segment Tree
        // Range [0, q]
        seg = new ArrayList[4 * (q + 1)];
        for(int i=0; i<seg.length; i++) seg[i] = new ArrayList<>();

        for (EdgeInterval ei : intervals) {
            if (ei.l <= ei.r) {
                addRange(1, 0, q, ei.l, ei.r, ei.u, ei.v);
            }
        }

        // 4. Process
        dsuParent = new int[n];
        dsuSz = new int[n];
        for (int i = 0; i < n; i++) {
            dsuParent[i] = i;
            dsuSz[i] = 1;
        }
        history = new Stack<>();

        int[] results = new int[queries.size()];
        // Map query time to index
        int[] queryMap = new int[q + 1];
        Arrays.fill(queryMap, -1);
        for(int i=0; i<queries.size(); i++) queryMap[queries.get(i).time] = i;

        solve(1, 0, q, queryMap, results, queries);

        return results;
    }

    private List<int[]>[] seg;

    private void addRange(int node, int start, int end, int l, int r, int u, int v) {
        if (r < start || end < l) return;
        if (l <= start && end <= r) {
            seg[node].add(new int[]{u, v});
            return;
        }
        int mid = (start + end) / 2;
        addRange(node * 2, start, mid, l, r, u, v);
        addRange(node * 2 + 1, mid + 1, end, l, r, u, v);
    }

    private void solve(int node, int start, int end, int[] queryMap, int[] results, List<Query> queries) {
        int ops = 0;
        for (int[] edge : seg[node]) {
            if (union(edge[0], edge[1])) ops++;
        }

        if (start == end) {
            if (queryMap[start] != -1) {
                Query q = queries.get(queryMap[start]);
                if (find(q.u) == find(q.v)) {
                    results[queryMap[start]] = getLCA(q.u, q.v);
                } else {
                    results[queryMap[start]] = -1;
                }
            }
        } else {
            int mid = (start + end) / 2;
            solve(node * 2, start, mid, queryMap, results, queries);
            solve(node * 2 + 1, mid + 1, end, queryMap, results, queries);
        }

        // Rollback
        while (ops-- > 0) rollback();
    }

    private void dfsLCA(int u, int d, int p) {
        depth[u] = d;
        up[u][0] = p;
        for (int i = 1; i < LOG; i++) {
            if (up[u][i-1] != -1) up[u][i] = up[up[u][i-1]][i-1];
            else up[u][i] = -1;
        }
        for (int v : adj.get(u)) {
            if (v != p) dfsLCA(v, d + 1, u);
        }
    }

    private int getLCA(int u, int v) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        for (int i = LOG - 1; i >= 0; i--) {
            if (depth[u] - (1 << i) >= depth[v]) u = up[u][i];
        }
        if (u == v) return u;
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        return up[u][0];
    }

    private int find(int i) {
        while (i != dsuParent[i]) i = dsuParent[i];
        return i;
    }

    private boolean union(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            if (dsuSz[root_i] < dsuSz[root_j]) { int t = root_i; root_i = root_j; root_j = t; }
            dsuParent[root_j] = root_i;
            dsuSz[root_i] += dsuSz[root_j];
            history.push(new int[]{root_j, root_i});
            return true;
        }
        return false;
    }

    private void rollback() {
        int[] op = history.pop();
        int child = op[0];
        int parent = op[1];
        dsuParent[child] = child;
        dsuSz[parent] -= dsuSz[child];
    }

    static class EdgeInterval {
        int l, r, u, v;
        EdgeInterval(int l, int r, int u, int v) { this.l = l; this.r = r; this.u = u; this.v = v; }
    }

    static class Query {
        int time, u, v;
        Query(int t, int u, int v) { this.time = t; this.u = u; this.v = v; }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }
        int q = sc.nextInt();
        String[] type = new String[q];
        int[][] queryArgs = new int[q][2];
        for (int i = 0; i < q; i++) {
            type[i] = sc.next();
            queryArgs[i][0] = sc.nextInt();
            queryArgs[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] results = solution.offlineLca(n, edges, type, queryArgs);

        for (int res : results) {
            System.out.println(res);
        }
        sc.close();
    }
}
