import java.util.*;

public class Distance2IndependentSet {
    static List<Integer>[] graph;
    static long[] weight;
    static long[][] dp;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        weight = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            weight[i] = sc.nextLong();
        }

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        dp = new long[n + 1][3];

        dfs(1, -1);

        long result = Math.max(dp[1][0], Math.max(dp[1][1], dp[1][2]));
        System.out.println(result);

        sc.close();
    }

    static void dfs(int u, int parent) {
        dp[u][0] = 0;
        dp[u][1] = 0;
        dp[u][2] = weight[u];

        long sumWithoutSelected = 0;
        long maxGain = Long.MIN_VALUE;

        for (int v : graph[u]) {
            if (v == parent) continue;

            dfs(v, u);

            long bestNotSelected = Math.max(dp[v][0], dp[v][1]);
            sumWithoutSelected += bestNotSelected;

            long gain = dp[v][2] - bestNotSelected;
            maxGain = Math.max(maxGain, gain);

            dp[u][2] += dp[v][0];
        }

        dp[u][0] = sumWithoutSelected;

        if (maxGain > Long.MIN_VALUE) {
            dp[u][1] = sumWithoutSelected + maxGain;
        }
    }
}
