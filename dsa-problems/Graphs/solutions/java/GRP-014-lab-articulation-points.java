import java.util.*;

class Solution {
    private int time = 0;
    private Set<Integer> ap;
    
    public List<Integer> findArticulationPoints(int n, List<List<Integer>> adj) {
        int[] disc = new int[n];
        int[] low = new int[n];
        int[] parent = new int[n];
        Arrays.fill(disc, -1);
        Arrays.fill(parent, -1);
        ap = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, adj, disc, low, parent);
            }
        }
        
        return new ArrayList<>(ap);
    }
    
    private void dfs(int u, List<List<Integer>> adj, int[] disc, int[] low, int[] parent) {
        int children = 0;
        disc[u] = low[u] = time++;
        
        for (int v : adj.get(u)) {
            if (disc[v] == -1) {
                children++;
                parent[v] = u;
                dfs(v, adj, disc, low, parent);
                
                low[u] = Math.min(low[u], low[v]);
                
                if (parent[u] != -1 && low[v] >= disc[u]) {
                    ap.add(u);
                }
            } else if (v != parent[u]) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
        
        if (parent[u] == -1 && children > 1) {
            ap.add(u);
        }
    }
}
