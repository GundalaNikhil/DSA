import java.util.*;

public class MaxPathSumLengthLimit {
    static class Edge {
        int to;
        Edge(int to) {
            this.to = to;
        }
    }

    static List<Edge>[] graph;
    static long[] value;
    static long[][] dp;
    static long maxSum;
    static int n, L;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        L = sc.nextInt();

        value = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            value[i] = sc.nextLong();
        }

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

        dp = new long[n + 1][L + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], Long.MIN_VALUE / 2);
        }

        maxSum = Long.MIN_VALUE;

        dfs(1, -1);

        // Also consider single node paths
        for (int i = 1; i <= n; i++) {
            maxSum = Math.max(maxSum, value[i]);
        }

        System.out.println(maxSum);
        sc.close();
    }

    static void dfs(int u, int parent) {
        dp[u][0] = value[u];
        maxSum = Math.max(maxSum, value[u]);

        List<long[]> childPaths = new ArrayList<>();

        for (Edge e : graph[u]) {
            int v = e.to;
            if (v == parent) continue;

            dfs(v, u);

            // Extend paths from child
            long[] childBest = new long[L + 1];
            Arrays.fill(childBest, Long.MIN_VALUE / 2);

            for (int len = 0; len < L; len++) {
                if (dp[v][len] > Long.MIN_VALUE / 2) {
                    long extended = dp[v][len] + value[u];
                    dp[u][len + 1] = Math.max(dp[u][len + 1], extended);
                    childBest[len] = dp[v][len];
                }
            }

            childPaths.add(childBest);
        }

        // Update max with single downward path
        for (int len = 0; len <= L; len++) {
            maxSum = Math.max(maxSum, dp[u][len]);
        }

        // Combine two paths through this node
        for (int i = 0; i < childPaths.size(); i++) {
            for (int j = i + 1; j < childPaths.size(); j++) {
                long[] path1 = childPaths.get(i);
                long[] path2 = childPaths.get(j);

                for (int len1 = 0; len1 <= L; len1++) {
                    for (int len2 = 0; len2 <= L; len2++) {
                        // Total edges: len1 + 1 (to u) + 1 (from u) + len2
                        if (len1 + len2 + 2 > L) continue;
                        if (path1[len1] > Long.MIN_VALUE / 2 &&
                            path2[len2] > Long.MIN_VALUE / 2) {
                            long combined = path1[len1] + path2[len2] + value[u];
                            maxSum = Math.max(maxSum, combined);
                        }
                    }
                }
            }
        }
    }
}
