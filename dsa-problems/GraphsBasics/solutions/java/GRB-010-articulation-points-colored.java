import java.util.*;

class Solution {
    private int timer;
    private int[] disc, low;
    private int[] redSub, blueSub;
    private int totalRed, totalBlue;
    private List<Integer> critical;
    private boolean[] visited;

    public int[] criticalNodes(int n, List<int[]> edges) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        
        totalRed = 0;
        totalBlue = 0;
        
        for (int[] e : edges) {
            adj.get(e[0]).add(new int[]{e[1], e[2]});
            adj.get(e[1]).add(new int[]{e[0], e[2]});
            if (e[2] == 0) totalRed++;
            else totalBlue++;
        }

        disc = new int[n];
        low = new int[n];
        redSub = new int[n];
        blueSub = new int[n];
        visited = new boolean[n];
        critical = new ArrayList<>();
        timer = 0;
        Arrays.fill(disc, -1);

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, -1, adj);
            }
        }

        Collections.sort(critical);
        return critical.stream().mapToInt(i -> i).toArray();
    }

    private void dfs(int u, int p, List<List<int[]>> adj) {
        visited[u] = true;
        disc[u] = low[u] = ++timer;
        int children = 0;
        boolean isCritical = false;

        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            int color = edge[1];
            
            if (v == p) continue;

            if (visited[v]) {
                low[u] = Math.min(low[u], disc[v]);
                // Back-edge contributes to subtree counts? 
                // No, edges are counted at the node "below" in DFS tree or explicitly.
                // To avoid double counting, we only count edges (u, v) where v is child.
                // But for back-edge, we shouldn't count it again if we counted it at v?
                // Correct approach: Count edge (u, v) for v's subtree if we traverse u->v.
                // If v is visited, it's a back-edge. It is part of u's subtree (conceptually loops back).
                // But `redSub` tracks edges *in the DFS subtree*. Back-edges are part of the component logic.
                // Let's count edge (u, v) in `redSub[u]` if it's a back-edge.
                if (disc[v] < disc[u]) { // Only count back-edge once
                     if (color == 0) redSub[u]++;
                     else blueSub[u]++;
                }
            } else {
                children++;
                dfs(v, u, adj);
                
                // Add child's subtree counts
                redSub[u] += redSub[v];
                blueSub[u] += blueSub[v];
                
                // Add the edge (u, v) itself
                if (color == 0) redSub[u]++;
                else blueSub[u]++;

                low[u] = Math.min(low[u], low[v]);

                if (low[v] >= disc[u] && p != -1) {
                    // When u is removed, the edge (u,v) is also removed.
                    // Component v's subtree contains only its internal edges.
                    // Do NOT include the edge (u,v) in the component.
                    int vRed = redSub[v];
                    int vBlue = blueSub[v];

                    // Rest of graph: totalRed/totalBlue minus edges in v's subtree
                    // Also minus the edge (u,v) itself
                    int edgeColor = color;
                    int restRed = totalRed - vRed - (edgeColor == 0 ? 1 : 0);
                    int restBlue = totalBlue - vBlue - (edgeColor == 1 ? 1 : 0);

                    if ((vRed > 0 && restBlue > 0) || (vBlue > 0 && restRed > 0)) {
                        isCritical = true;
                    }
                }
            }
        }
        
        // Root check
        if (p == -1 && children > 1) {
             // For root, we need to check each child individually
             // Re-run logic or store flags?
             // For root, we need to check if ANY child satisfies the condition.
             // Let's adjust the loop to handle root inside.
        }
        
        // Let's refine the check inside the loop to handle root correctly
    }
}
