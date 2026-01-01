import java.util.*;

class Solution {
    private int timer;
    private int[] disc, low;
    private List<Integer> criticalIndices;
    
    public List<int[]> criticalEdges(int n, int[][] edges, int T) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int c = edges[i][2];
            if (c < T) {
                adj.get(u).add(new int[]{v, c, i});
                adj.get(v).add(new int[]{u, c, i});
            }
        }

        disc = new int[n];
        low = new int[n];
        Arrays.fill(disc, -1);
        criticalIndices = new ArrayList<>();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, -1, adj, T);
            }
        }
        
        Collections.sort(criticalIndices);
        
        List<int[]> result = new ArrayList<>();
        for (int idx : criticalIndices) {
            result.add(new int[]{edges[idx][0], edges[idx][1]});
        }
        return result;
    }

    private void dfs(int u, int parentEdgeIdx, List<List<int[]>> adj, int T) {
        disc[u] = low[u] = ++timer;
        
        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            int cap = edge[1];
            int idx = edge[2];
            
            if (idx == parentEdgeIdx) continue; // Don't go back via same edge
            
            if (disc[v] != -1) {
                low[u] = Math.min(low[u], disc[v]);
            } else {
                dfs(v, idx, adj, T);
                low[u] = Math.min(low[u], low[v]);
                
                if (low[v] > disc[u]) {
                    // Bridge found
                    if (cap < T) {
                        criticalIndices.add(idx);
                    }
                }
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int T = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<int[]> ans = solution.criticalEdges(n, edges, T);
        StringBuilder sb = new StringBuilder();
        sb.append(ans.size()).append('\n');
        for (int[] e : ans) {
            sb.append(e[0]).append(' ').append(e[1]).append('\n');
        }
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
