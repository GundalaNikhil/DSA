import java.util.*;

class Solution {
    static class Edge {
        int u, v;
        Edge(int u, int v) {
            this.u = u;
            this.v = v;
        }
        
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Edge edge = (Edge) o;
            return (u == edge.u && v == edge.v) || (u == edge.v && v == edge.u);
        }
        
        @Override
        public int hashCode() {
            return u < v ? Objects.hash(u, v) : Objects.hash(v, u);
        }
    }

    static class DSU {
        int[] parent;
        int[] rank;
        Stack<int[]> history;

        DSU(int n) {
            parent = new int[n + 1];
            rank = new int[n + 1];
            history = new Stack<>();
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                rank[i] = 1;
            }
        }

        int find(int i) {
            if (parent[i] == i) return i;
            return find(parent[i]); // No path compression for rollback
        }

        void union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            if (rootI != rootJ) {
                if (rank[rootI] < rank[rootJ]) {
                    int temp = rootI;
                    rootI = rootJ;
                    rootJ = temp;
                }
                parent[rootJ] = rootI;
                rank[rootI] += rank[rootJ];
                history.push(new int[]{rootJ, rootI});
            } else {
                history.push(new int[]{-1, -1});
            }
        }

        void rollback() {
            int[] op = history.pop();
            if (op[0] != -1) {
                int child = op[0];
                int parentNode = op[1];
                parent[child] = child;
                rank[parentNode] -= rank[child];
            }
        }
        
        boolean connected(int i, int j) {
            return find(i) == find(j);
        }
    }

    private List<Edge>[] tree;
    private List<String> results;
    private List<String[]> queries; // Store queries by time index

    public List<String> process(int n, List<String[]> events) {
        int m = events.size();
        tree = new ArrayList[4 * m];
        for (int i = 0; i < 4 * m; i++) tree[i] = new ArrayList<>();
        
        queries = new ArrayList<>();
        for(int i=0; i<m; i++) queries.add(null);
        
        Map<String, Integer> activeEdges = new HashMap<>();
        
        for (int i = 0; i < m; i++) {
            String[] ev = events.get(i);
            String type = ev[0];
            int u = Integer.parseInt(ev[1]);
            int v = Integer.parseInt(ev[2]);
            if (u > v) { int temp = u; u = v; v = temp; }
            String key = u + "," + v;
            
            if (type.equals("ADD")) {
                activeEdges.put(key, i);
            } else if (type.equals("REMOVE")) {
                if (activeEdges.containsKey(key)) {
                    int start = activeEdges.remove(key);
                    addEdge(0, 0, m - 1, start, i - 1, new Edge(u, v));
                }
            } else {
                queries.set(i, ev);
            }
        }
        
        for (Map.Entry<String, Integer> entry : activeEdges.entrySet()) {
            int start = entry.getValue();
            String[] parts = entry.getKey().split(",");
            int u = Integer.parseInt(parts[0]);
            int v = Integer.parseInt(parts[1]);
            addEdge(0, 0, m - 1, start, m - 1, new Edge(u, v));
        }
        
        results = new ArrayList<>();
        DSU dsu = new DSU(n);
        dfs(0, 0, m - 1, dsu);
        
        return results;
    }

    private void addEdge(int node, int start, int end, int l, int r, Edge e) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node].add(e);
            return;
        }
        int mid = (start + end) / 2;
        addEdge(2 * node + 1, start, mid, l, r, e);
        addEdge(2 * node + 2, mid + 1, end, l, r, e);
    }

    private void dfs(int node, int start, int end, DSU dsu) {
        int ops = 0;
        for (Edge e : tree[node]) {
            dsu.union(e.u, e.v);
            ops++;
        }
        
        if (start == end) {
            String[] q = queries.get(start);
            if (q != null) {
                int u = Integer.parseInt(q[1]);
                int v = Integer.parseInt(q[2]);
                results.add(dsu.connected(u, v) ? "true" : "false");
            }
        } else {
            int mid = (start + end) / 2;
            dfs(2 * node + 1, start, mid, dsu);
            dfs(2 * node + 2, mid + 1, end, dsu);
        }
        
        while (ops-- > 0) {
            dsu.rollback();
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            List<String[]> events = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                String type = sc.next();
                events.add(new String[]{type, sc.next(), sc.next()});
            }
            Solution sol = new Solution();
            List<String> results = sol.process(n, events);
            for (String res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
