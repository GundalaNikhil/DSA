import java.util.*;

class Solution {
    public boolean canColorBipartite(int n, List<List<Integer>> adj, int[] locked) {
        int[] color = new int[n];
        Arrays.fill(color, -1);
        
        // Pre-color locked nodes
        for (int i = 0; i < n; i++) {
            if (locked[i] != 0) {
                color[i] = locked[i];
            }
        }
        
        // Check each component
        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {
                if (!bfs(i, adj, color, locked)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean bfs(int start, List<List<Integer>> adj, int[] color, int[] locked) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        color[start] = (locked[start] == 0) ? 1 : locked[start];
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            int requiredNeighborColor = 3 - color[node]; // Toggle between 1 and 2
            
            for (int neighbor : adj.get(node)) {
                if (color[neighbor] == -1) {
                    // Uncolored neighbor
                    if (locked[neighbor] != 0 && locked[neighbor] != requiredNeighborColor) {
                        return false; // Locked to wrong color
                    }
                    color[neighbor] = requiredNeighborColor;
                    queue.offer(neighbor);
                } else if (color[neighbor] != requiredNeighborColor) {
                    return false; // Color conflict
                }
            }
        }
        
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        
        int[] locked = new int[n];
        for (int i = 0; i < n; i++) {
            locked[i] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.canColorBipartite(n, adj, locked));
        sc.close();
    }
}
