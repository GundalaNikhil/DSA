import java.util.*;

class Solution {
    public long[] dijkstra(int n, List<List<int[]>> adj, int source) {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[source] = 0;
        
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[]{0, source});
        
        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long d = curr[0];
            int node = (int)curr[1];
            
            if (d > dist[node]) continue;
            
            for (int[] edge : adj.get(node)) {
                int neighbor = edge[0];
                long weight = edge[1];
                long newDist = dist[node] + weight;
                
                if (newDist < dist[neighbor]) {
                    dist[neighbor] = newDist;
                    pq.offer(new long[]{newDist, neighbor});
                }
            }
        }
        
        return dist;
    }
}
