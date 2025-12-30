import java.util.*;

class Solution {
    public List<Integer> reachableNodes(int n, List<List<int[]>> adj, int source, int threshold) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        
        queue.offer(source);
        visited.add(source);
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            
            for (int[] edge : adj.get(node)) {
                int neighbor = edge[0];
                int weight = edge[1];
                
                if (weight <= threshold && !visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }
        
        return new ArrayList<>(visited);
    }
}
