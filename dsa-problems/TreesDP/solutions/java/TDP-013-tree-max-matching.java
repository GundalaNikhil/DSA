import java.util.*;
public class TreeMaxMatching {
    static List<Integer>[] adj;
    static int[][] dp;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        dp = new int[n + 1][2];
        dfs(1, 0);
        System.out.println(Math.max(dp[1][0], dp[1][1]));
    }

    static void dfs(int u, int p) {
        dp[u][0] = 0;
        dp[u][1] = 0;
        int sum = 0;

        for (int v : adj[u]) {
            if (v == p) continue;
            dfs(v, u);
            sum += Math.max(dp[v][0], dp[v][1]);
        }

        dp[u][0] = sum;

        for (int v : adj[u]) {
            if (v == p) continue;
            dp[u][1] = Math.max(dp[u][1], 1 + dp[v][0] + sum - Math.max(dp[v][0], dp[v][1]));
        }
    }
}
