import java.util.*;

class Solution {
    public int[] shortestDistances(int n, List<List<Integer>> adj, int source) {
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        dist[source] = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(source);
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            
            for (int neighbor : adj.get(node)) {
                if (dist[neighbor] == -1) {
                    dist[neighbor] = dist[node] + 1;
                    queue.offer(neighbor);
                }
            }
        }
        
        return dist;
    }
}
