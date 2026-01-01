import java.util.*;

class Solution {
    static class Edge {
        int to;
        int rev;
        long cap;
        long flow;
        Edge(int to, int rev, long cap) {
            this.to = to;
            this.rev = rev;
            this.cap = cap;
            this.flow = 0;
        }
    }

    private List<List<Edge>> adj;
    private int[] level;
    private int[] ptr;
    private int N;

    public long minVertexCoverCost(int nU, int nV, long[] wU, long[] wV, int[][] edges) {
        int S = 0;
        int T = nU + nV + 1;
        N = T + 1;
        adj = new ArrayList<>();
        for (int i = 0; i < N; i++) adj.add(new ArrayList<>());

        long INF = 1_000_000_000_000_000_000L; // 1e18

        // S -> U
        for (int i = 0; i < nU; i++) {
            addEdge(S, i + 1, wU[i]);
        }

        // V -> T
        for (int i = 0; i < nV; i++) {
            addEdge(nU + 1 + i, T, wV[i]);
        }

        // U -> V
        for (int[] e : edges) {
            int u = e[0] + 1;
            int v = nU + 1 + e[1];
            addEdge(u, v, INF);
        }

        return dinic(S, T);
    }

    private void addEdge(int from, int to, long cap) {
        Edge a = new Edge(to, adj.get(to).size(), cap);
        Edge b = new Edge(from, adj.get(from).size(), 0);
        adj.get(from).add(a);
        adj.get(to).add(b);
    }

    private boolean bfs(int s, int t) {
        level = new int[N];
        Arrays.fill(level, -1);
        level[s] = 0;
        Queue<Integer> q = new ArrayDeque<>();
        q.add(s);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (Edge e : adj.get(u)) {
                if (e.cap - e.flow > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.add(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    private long dfs(int u, int t, long pushed) {
        if (pushed == 0) return 0;
        if (u == t) return pushed;
        for (; ptr[u] < adj.get(u).size(); ptr[u]++) {
            Edge e = adj.get(u).get(ptr[u]);
            if (level[u] + 1 != level[e.to] || e.cap - e.flow == 0) continue;
            long tr = dfs(e.to, t, Math.min(pushed, e.cap - e.flow));
            if (tr == 0) continue;
            e.flow += tr;
            adj.get(e.to).get(e.rev).flow -= tr;
            return tr;
        }
        return 0;
    }

    private long dinic(int s, int t) {
        long flow = 0;
        while (bfs(s, t)) {
            ptr = new int[N];
            while (true) {
                long pushed = dfs(s, t, Long.MAX_VALUE);
                if (pushed == 0) break;
                flow += pushed;
            }
        }
        return flow;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int nU = sc.nextInt();
        int nV = sc.nextInt();
        int m = sc.nextInt();
        long[] wU = new long[nU];
        long[] wV = new long[nV];
        for (int i = 0; i < nU; i++) wU[i] = sc.nextLong();
        for (int i = 0; i < nV; i++) wV[i] = sc.nextLong();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.minVertexCoverCost(nU, nV, wU, wV, edges));
        sc.close();
    }
}
