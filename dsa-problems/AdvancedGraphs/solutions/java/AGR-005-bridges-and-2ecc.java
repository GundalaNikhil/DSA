import java.util.*;

class Solution {
    private int timer;
    private int[] tin, low;
    private boolean[] visited;
    private int[] bridgeFlags; // 1 if edge i is bridge
    private List<List<int[]>> adj; // {neighbor, edgeIndex}

    public int[][] bridgesAndComponents(int n, int[][] edges) {
        int m = edges.length;
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            adj.get(edges[i][0]).add(new int[]{edges[i][1], i});
            adj.get(edges[i][1]).add(new int[]{edges[i][0], i});
        }

        tin = new int[n];
        low = new int[n];
        visited = new boolean[n];
        bridgeFlags = new int[m];
        timer = 0;

        // 1. Find Bridges
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfsBridges(i, -1);
            }
        }

        // 2. Find Components (DFS ignoring bridges)
        int[] comp = new int[n];
        int compCount = 0;
        Arrays.fill(visited, false); // Reuse visited array

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                compCount++;
                dfsComponents(i, compCount, comp);
            }
        }

        return new int[][]{bridgeFlags, comp};
    }

    private void dfsBridges(int u, int pEdgeIndex) {
        visited[u] = true;
        tin[u] = low[u] = timer++;
        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            int idx = edge[1];
            if (idx == pEdgeIndex) continue; // Don't go back through same edge

            if (visited[v]) {
                low[u] = Math.min(low[u], tin[v]);
            } else {
                dfsBridges(v, idx);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > tin[u]) {
                    bridgeFlags[idx] = 1;
                }
            }
        }
    }

    private void dfsComponents(int u, int c, int[] comp) {
        visited[u] = true;
        comp[u] = c;
        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            int idx = edge[1];
            if (bridgeFlags[idx] == 1) continue; // Don't cross bridges
            if (!visited[v]) {
                dfsComponents(v, c, comp);
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[][] result = solution.bridgesAndComponents(n, edges);
        int[] bridgeFlags = result[0];
        int[] comp = result[1];

        int bridgeCount = 0;
        for (int f : bridgeFlags) bridgeCount += f;

        StringBuilder sb = new StringBuilder();
        sb.append(bridgeCount).append('\n');
        for (int i = 0; i < m; i++) {
            if (bridgeFlags[i] == 1) {
                sb.append(edges[i][0]).append(' ').append(edges[i][1]).append('\n');
            }
        }
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(comp[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
