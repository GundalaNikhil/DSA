import java.util.*;

class Solution {
    static class Edge {
        int to;
        long capacity;
        long flow;
        int rev; // index of reverse edge

        Edge(int to, long capacity, int rev) {
            this.to = to;
            this.capacity = capacity;
            this.rev = rev;
            this.flow = 0;
        }
    }

    private List<List<Edge>> adj;
    private int[] level;
    private int[] ptr;

    public long maxFlowVertexCap(int n, int s, int t, long[] cap, int[][] edges) {
        int numNodes = 2 * n;
        int sNode = 2 * s; // Start at s_in
        int tNode = 2 * t + 1; // End at t_out

        adj = new ArrayList<>();
        for (int i = 0; i < numNodes; i++) adj.add(new ArrayList<>());

        long INF = 1_000_000_000_000_000L;

        // 1. Add Vertex Capacity Edges (u_in -> u_out)
        for (int i = 0; i < n; i++) {
            long c = (cap[i] == -1 || i == s || i == t) ? INF : cap[i];
            addEdge(2 * i, 2 * i + 1, c);
        }

        // 2. Add Original Edges (u_out -> v_in)
        for (int[] e : edges) {
            int u = e[0];
            int v = e[1];
            int c = e[2];
            addEdge(2 * u + 1, 2 * v, c);
        }

        // 3. Dinic's Algorithm
        long maxFlow = 0;
        while (bfs(sNode, tNode, numNodes)) {
            ptr = new int[numNodes];
            while (true) {
                long pushed = dfs(sNode, tNode, INF);
                if (pushed == 0) break;
                maxFlow += pushed;
            }
        }

        return maxFlow;
    }

    private void addEdge(int from, int to, long cap) {
        Edge a = new Edge(to, cap, adj.get(to).size());
        Edge b = new Edge(from, 0, adj.get(from).size()); // Residual
        adj.get(from).add(a);
        adj.get(to).add(b);
    }

    private boolean bfs(int s, int t, int n) {
        level = new int[n];
        Arrays.fill(level, -1);
        level[s] = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(s);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (Edge e : adj.get(u)) {
                if (e.capacity - e.flow > 0 && level[e.to] == -1) {
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
            if (level[u] + 1 != level[e.to] || e.capacity - e.flow == 0) continue;
            long tr = dfs(e.to, t, Math.min(pushed, e.capacity - e.flow));
            if (tr == 0) continue;
            e.flow += tr;
            adj.get(e.to).get(e.rev).flow -= tr;
            return tr;
        }
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        long[] cap = new long[n];
        for (int i = 0; i < n; i++) cap[i] = sc.nextLong();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxFlowVertexCap(n, s, t, cap, edges));
        sc.close();
    }
}
