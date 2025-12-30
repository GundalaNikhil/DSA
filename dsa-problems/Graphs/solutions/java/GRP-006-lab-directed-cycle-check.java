import java.util.*;

class Solution {
    public boolean hasCycle(int n, List<List<Integer>> adj) {
        boolean[] visited = new boolean[n];
        boolean[] recStack = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (dfs(i, adj, visited, recStack)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    private boolean dfs(int node, List<List<Integer>> adj, boolean[] visited, boolean[] recStack) {
        visited[node] = true;
        recStack[node] = true;
        
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, adj, visited, recStack)) {
                    return true;
                }
            } else if (recStack[neighbor]) {
                return true; // Back edge - cycle detected
            }
        }
        
        recStack[node] = false;
        return false;
    }
}
