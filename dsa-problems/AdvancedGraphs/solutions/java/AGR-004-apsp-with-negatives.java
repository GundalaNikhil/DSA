import java.util.*;

class Solution {
    static class Edge {
        int to;
        long weight;
        Edge(int to, long weight) { this.to = to; this.weight = weight; }
    }

    public long[][] allPairsShortestPaths(int n, int[][] edges) {
        List<List<Edge>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(new Edge(e[1], e[2]));
        }

        long INF = 1_000_000_000_000_000_000L; // 1e18

        // 1. Bellman-Ford to find potentials h[]
        // Virtual source connected to all nodes with 0 weight
        long[] h = new long[n + 1];
        Arrays.fill(h, INF);
        h[n] = 0; // Virtual source index n
        
        // We don't explicitly add node n to adj, we just simulate edges n->i
        // Edges: original edges + (n, i, 0) for all i
        
        boolean changed = true;
        for (int i = 0; i < n; i++) { // n+1 nodes, so n iterations
            changed = false;
            // Edges from virtual source
            for (int u = 0; u < n; u++) {
                if (h[n] + 0 < h[u]) {
                    h[u] = h[n] + 0;
                    changed = true;
                }
            }
            // Original edges
            for (int u = 0; u < n; u++) {
                if (h[u] == INF) continue;
                for (Edge e : adj.get(u)) {
                    if (h[u] + e.weight < h[e.to]) {
                        h[e.to] = h[u] + e.weight;
                        changed = true;
                    }
                }
            }
            if (!changed) break;
        }

        // 2. Reweight edges
        // w'(u,v) = w(u,v) + h[u] - h[v]
        // We compute this on the fly during Dijkstra

        long[][] result = new long[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(result[i], INF);

        // 3. Run Dijkstra from each node
        for (int s = 0; s < n; s++) {
            PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
            long[] d = new long[n];
            Arrays.fill(d, INF);
            
            d[s] = 0;
            pq.add(new long[]{0, s});

            while (!pq.isEmpty()) {
                long[] top = pq.poll();
                long distU = top[0];
                int u = (int) top[1];

                if (distU > d[u]) continue;

                for (Edge e : adj.get(u)) {
                    long newWeight = e.weight + h[u] - h[e.to];
                    if (d[u] + newWeight < d[e.to]) {
                        d[e.to] = d[u] + newWeight;
                        pq.add(new long[]{d[e.to], e.to});
                    }
                }
            }

            // 4. Adjust distances back
            for (int v = 0; v < n; v++) {
                if (d[v] != INF) {
                    result[s][v] = d[v] - h[s] + h[v];
                }
            }
        }

        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        long[][] dist = solution.allPairsShortestPaths(n, edges);
        long INF = 1_000_000_000_000_000_000L;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j > 0) sb.append(' ');
                if (dist[i][j] >= INF / 2) sb.append("INF");
                else sb.append(dist[i][j]);
            }
            if (i + 1 < n) sb.append('\n');
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
