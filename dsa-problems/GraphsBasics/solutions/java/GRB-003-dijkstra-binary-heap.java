import java.util.*;

class Solution {
    public long[] dijkstra(int n, List<List<int[]>> adj, int s) {
        long[] dist = new long[n];
        Arrays.fill(dist, -1);
        
        // PriorityQueue stores {distance, node}
        // Use Long for distance to prevent overflow
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        
        dist[s] = 0;
        pq.offer(new long[]{0, s});
        
        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long d = curr[0];
            int u = (int) curr[1];
            
            // Lazy deletion: if we found a shorter path to u before processing this entry, skip
            if (d > dist[u] && dist[u] != -1) continue;
            
            for (int[] edge : adj.get(u)) {
                int v = edge[0];
                int w = edge[1];
                
                if (dist[v] == -1 || dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.offer(new long[]{dist[v], v});
                }
            }
        }
        
        return dist;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        Solution solution = new Solution();
        long[] dist = solution.dijkstra(n, adj, s);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(dist[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
