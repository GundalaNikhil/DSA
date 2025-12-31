import java.util.*;

class Solution {
    static class Edge {
        int to;
        int rev;
        long cap;
        long flow;
        long cost;
        Edge(int to, int rev, long cap, long cost) {
            this.to = to;
            this.rev = rev;
            this.cap = cap;
            this.cost = cost;
            this.flow = 0;
        }
    }

    private List<List<Edge>> adj;
    private long[] dist;
    private long[] h;
    private int[] parentNode;
    private int[] parentEdge;
    private int N;
    private final long INF = Long.MAX_VALUE / 2;

    public Long minCostFlow(int n, long[] b, int[][] edges) {
        // 1. Handle Lower Bounds
        long baseCost = 0;
        long[] supply = Arrays.copyOf(b, n);
        
        // We need to construct the graph first to handle multi-edges properly?
        // Nodes 0..n-1 are original. S=n, T=n+1.
        int S = n;
        int T = n + 1;
        N = n + 2;
        adj = new ArrayList<>();
        for (int i = 0; i < N; i++) adj.add(new ArrayList<>());

        for (int[] e : edges) {
            int u = e[0];
            int v = e[1];
            int low = e[2];
            int high = e[3];
            int cost = e[4];

            if (high < low) return null; // Invalid

            baseCost += (long) low * cost;
            supply[u] -= low;
            supply[v] += low;

            addEdge(u, v, high - low, cost);
        }

        long totalSupply = 0;
        for (int i = 0; i < n; i++) {
            if (supply[i] > 0) {
                addEdge(S, i, supply[i], 0);
                totalSupply += supply[i];
            } else if (supply[i] < 0) {
                addEdge(i, T, -supply[i], 0);
            }
        }

        // 2. Min Cost Max Flow
        long[] res = mcmf(S, T);
        
        if (res[0] != totalSupply) return null; // Infeasible

        return baseCost + res[1];
    }

    private void addEdge(int u, int v, long cap, long cost) {
        Edge a = new Edge(v, adj.get(v).size(), cap, cost);
        Edge b = new Edge(u, adj.get(u).size(), 0, -cost);
        adj.get(u).add(a);
        adj.get(v).add(b);
    }

    private long[] mcmf(int s, int t) {
        long flow = 0;
        long cost = 0;
        h = new long[N];
        
        // Initial potentials with SPFA (Bellman-Ford) to handle negative costs
        if (!spfa(s)) {
             // If SPFA fails (negative cycle reachable from S), problem is unbounded or tricky.
             // But here capacities are finite, so we saturate negative cycles?
             // Standard MCMF assumes no negative cycles initially or handles them.
             // For this problem, we assume no negative cycles in the residual graph of 0 flow?
             // Or we just run SPFA.
        }

        while (dijkstra(s, t)) {
            long push = INF;
            int curr = t;
            while (curr != s) {
                int p = parentNode[curr];
                int idx = parentEdge[curr];
                push = Math.min(push, adj.get(p).get(idx).cap - adj.get(p).get(idx).flow);
                curr = p;
            }

            flow += push;
            curr = t;
            while (curr != s) {
                int p = parentNode[curr];
                int idx = parentEdge[curr];
                adj.get(p).get(idx).flow += push;
                int revIdx = adj.get(p).get(idx).rev;
                adj.get(curr).get(revIdx).flow -= push;
                cost += push * adj.get(p).get(idx).cost;
                curr = p;
            }
            
            // Update potentials
            for (int i = 0; i < N; i++) {
                if (dist[i] != INF) h[i] += dist[i];
            }
        }
        return new long[]{flow, cost};
    }

    private boolean spfa(int s) {
        Arrays.fill(h, INF);
        h[s] = 0;
        boolean[] inQueue = new boolean[N];
        Queue<Integer> q = new ArrayDeque<>();
        q.add(s);
        inQueue[s] = true;
        
        while (!q.isEmpty()) {
            int u = q.poll();
            inQueue[u] = false;
            for (Edge e : adj.get(u)) {
                if (e.cap - e.flow > 0 && h[e.to] > h[u] + e.cost) {
                    h[e.to] = h[u] + e.cost;
                    if (!inQueue[e.to]) {
                        q.add(e.to);
                        inQueue[e.to] = true;
                    }
                }
            }
        }
        return h[s] != INF; // Just return true usually
    }

    private boolean dijkstra(int s, int t) {
        dist = new long[N];
        Arrays.fill(dist, INF);
        parentNode = new int[N];
        parentEdge = new int[N];
        dist[s] = 0;
        
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.add(new long[]{0, s});

        while (!pq.isEmpty()) {
            long[] top = pq.poll();
            long d = top[0];
            int u = (int) top[1];

            if (d > dist[u]) continue;

            for (int i = 0; i < adj.get(u).size(); i++) {
                Edge e = adj.get(u).get(i);
                long reducedCost = e.cost + h[u] - h[e.to];
                if (e.cap - e.flow > 0 && dist[e.to] > dist[u] + reducedCost) {
                    dist[e.to] = dist[u] + reducedCost;
                    parentNode[e.to] = u;
                    parentEdge[e.to] = i;
                    pq.add(new long[]{dist[e.to], e.to});
                }
            }
        }
        return dist[t] != INF;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        long[] b = new long[n];
        for (int i = 0; i < n; i++) b[i] = sc.nextLong();
        int[][] edges = new int[m][5];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
            edges[i][3] = sc.nextInt();
            edges[i][4] = sc.nextInt();
        }

        Solution solution = new Solution();
        Long ans = solution.minCostFlow(n, b, edges);
        if (ans == null) {
            System.out.print("INFEASIBLE");
        } else {
            System.out.print("FEASIBLE\n" + ans);
        }
        sc.close();
    }
}
