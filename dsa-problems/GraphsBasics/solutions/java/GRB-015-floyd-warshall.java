import java.util.*;

class Solution {
    public long[][] floydWarshall(long[][] dist) {
        int n = dist.length;
        long INF = 1_000_000_000_000_000L; // 1e15

        // Preprocess: Convert -1 to INF
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && dist[i][j] == -1) {
                    dist[i][j] = INF;
                }
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][k] != INF && dist[k][j] != INF) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }

        // Check for negative cycles
        for (int i = 0; i < n; i++) {
            if (dist[i][i] < 0) return null;
        }

        // Postprocess: Convert INF back to -1
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] >= INF / 2) { // Check for large values
                     dist[i][j] = -1;
                }
            }
        }

        return dist;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[][] dist = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = sc.nextLong();
            }
        }

        Solution solution = new Solution();
        long[][] ans = solution.floydWarshall(dist);
        if (ans == null) {
            System.out.print("NEGATIVE CYCLE");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(ans[i][j]);
                }
                if (i + 1 < n) sb.append('\n');
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
