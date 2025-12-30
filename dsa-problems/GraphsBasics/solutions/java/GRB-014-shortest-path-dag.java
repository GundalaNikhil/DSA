import java.util.*;

class Solution {
    private Stack<Integer> stack;
    private boolean[] visited;

    public long[] shortestPathDAG(int n, List<List<int[]>> adj, int s) {
        stack = new Stack<>();
        visited = new boolean[n];

        // 1. Topological Sort
        for (int i = 0; i < n; i++) {
            if (!visited[i]) dfs(i, adj);
        }

        // 2. Initialize Distances
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[s] = 0;

        // 3. Relax in Topological Order
        while (!stack.isEmpty()) {
            int u = stack.pop();
            
            if (dist[u] != Long.MAX_VALUE) {
                for (int[] edge : adj.get(u)) {
                    int v = edge[0];
                    int w = edge[1];
                    if (dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }
        }

        // Convert unreachable to -1
        for (int i = 0; i < n; i++) {
            if (dist[i] == Long.MAX_VALUE) dist[i] = -1;
        }
        
        return dist;
    }

    private void dfs(int u, List<List<int[]>> adj) {
        visited[u] = true;
        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            if (!visited[v]) dfs(v, adj);
        }
        stack.push(u);
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
        long[] dist = solution.shortestPathDAG(n, adj, s);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(dist[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
