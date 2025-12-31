import java.util.*;
public class KthAncestorColorFilter {
    static int n, LOG;
    static int[] color, depth;
    static int[][] up;
    static List<Integer>[] adj;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        LOG = 20;

        color = new int[n + 1];
        for (int i = 1; i <= n; i++) color[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        up = new int[n + 1][LOG];
        depth = new int[n + 1];
        dfs(1, 0);

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int v = sc.nextInt(), c = sc.nextInt(), k = sc.nextInt();
            System.out.println(findKthColoredAncestor(v, c, k));
        }
    }

    static void dfs(int u, int p) {
        up[u][0] = p;
        for (int i = 1; i < LOG; i++) {
            up[u][i] = up[up[u][i - 1]][i - 1];
        }
        for (int v : adj[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
            }
        }
    }

    static int findKthColoredAncestor(int v, int c, int k) {
        int count = 0;
        while (v != 0) {
            if (color[v] == c) {
                count++;
                if (count == k) return v;
            }
            v = up[v][0];
        }
        return -1;
    }
}
