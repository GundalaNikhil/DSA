import java.util.*;

class Solution {
    public long[] bellmanFord(int n, int s, int[][] edges) {
        long[] dist = new long[n];
        long INF = (long) 1e18;
        Arrays.fill(dist, INF);
        dist[s] = 0;

        // Relax edges N-1 times
        for (int i = 0; i < n - 1; i++) {
            boolean changed = false;
            for (int[] edge : edges) {
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                if (dist[u] != INF && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    changed = true;
                }
            }
            if (!changed) break; // Optimization
        }

        // Check for negative cycle
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if (dist[u] != INF && dist[u] + w < dist[v]) {
                return null; // Negative cycle detected
            }
        }

        // Convert INF to -1 for output
        for (int i = 0; i < n; i++) {
            if (dist[i] == INF) dist[i] = -1;
        }

        return dist;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        long[] dist = solution.bellmanFord(n, s, edges);
        if (dist == null) {
            System.out.print("NEGATIVE CYCLE");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(dist[i]);
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
