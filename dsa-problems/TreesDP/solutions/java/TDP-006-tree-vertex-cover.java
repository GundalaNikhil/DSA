import java.util.*;

public class TreeVertexCover {
    static class Edge {
        int to;
        Edge(int to) {
            this.to = to;
        }
    }

    static List<Edge>[] graph;
    static int[][] dp;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(new Edge(v));
            graph[v].add(new Edge(u));
        }

        dp = new int[n + 1][2];

        dfs(1, -1);

        int result = Math.min(dp[1][0], dp[1][1]);
        System.out.println(result);

        sc.close();
    }

    static void dfs(int u, int parent) {
        dp[u][0] = 0;  // Not including u
        dp[u][1] = 1;  // Including u

        for (Edge e : graph[u]) {
            int v = e.to;
            if (v == parent) continue;

            dfs(v, u);

            // If u is not included, all children must be included
            dp[u][0] += dp[v][1];

            // If u is included, children can be included or not
            dp[u][1] += Math.min(dp[v][0], dp[v][1]);
        }
    }
}
