import java.util.*;

class Main {
    static List<List<Integer>> adj;
    static int[] color;
    static int n, K, F;
    static long answer = 0;
    static int[][][] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt(); K = sc.nextInt(); F = sc.nextInt();

        color = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            color[i] = sc.nextInt();
        }

        adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        dp = new int[n + 1][K + 1][2];
        dfs(1, 0);
        System.out.println(answer);
    }

    static void dfs(int u, int p) {
        dp[u][0][color[u] == F ? 1 : 0] = 1;

        for (int v : adj.get(u)) {
            if (v == p) continue;
            dfs(v, u);

            // Save current dp[u] before merging
            int[][] temp = new int[K + 1][2];
            for (int d = 0; d <= K; d++) {
                for (int h = 0; h < 2; h++) {
                    temp[d][h] = dp[u][d][h];
                }
            }

            // Merge contributions
            for (int d1 = 0; d1 < K; d1++) {
                for (int d2 = 0; d1 + d2 + 1 <= K; d2++) {
                    for (int h1 = 0; h1 < 2; h1++) {
                        for (int h2 = 0; h2 < 2; h2++) {
                            if (d1 + d2 + 1 == K) {
                                // Count pairs only if path is clean
                                if (h1 == 0 && h2 == 0 && color[u] != F) {
                                    answer += (long)temp[d1][h1] * dp[v][d2][h2];
                                }
                            }

                            // Merge: path has forbidden if any segment has it or u has it
                            int newHas = h1 | h2 | (color[u] == F ? 1 : 0);
                            if (d1 + d2 + 1 <= K) {
                                dp[u][d1 + d2 + 1][newHas] += temp[d1][h1] * dp[v][d2][h2];
                            }
                        }
                    }
                }
            }
        }
    }
}
