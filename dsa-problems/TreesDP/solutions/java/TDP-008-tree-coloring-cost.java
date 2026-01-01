import java.util.*;

class Main {
    static List<List<Integer>> adj;
    static int[][] cost;
    static long[][] dp;
    static int n, k;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        cost = new int[n + 1][k + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                cost[i][j] = sc.nextInt();
            }
        }

        adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        dp = new long[n + 1][k + 1];
        boolean[] visited = new boolean[n + 1];

        dfs(1, visited);

        long result = Long.MAX_VALUE;
        for (int c = 1; c <= k; c++) {
            result = Math.min(result, dp[1][c]);
        }

        System.out.println(result);
    }

    static void dfs(int u, boolean[] visited) {
        visited[u] = true;

        // Initialize dp[u][c] with cost of coloring node u with color c
        for (int c = 1; c <= k; c++) {
            dp[u][c] = cost[u][c];
        }

        for (int v : adj.get(u)) {
            if (!visited[v]) {
                dfs(v, visited);

                // Find min and second min for child v
                long min1 = Long.MAX_VALUE, min2 = Long.MAX_VALUE;
                int minColor = -1;
                for (int c = 1; c <= k; c++) {
                    if (dp[v][c] < min1) {
                        min2 = min1;
                        min1 = dp[v][c];
                        minColor = c;
                    } else if (dp[v][c] < min2) {
                        min2 = dp[v][c];
                    }
                }

                // Update dp[u][c] for each color
                for (int c = 1; c <= k; c++) {
                    if (c == minColor) {
                        dp[u][c] += min2;
                    } else {
                        dp[u][c] += min1;
                    }
                }
            }
        }
    }
}
