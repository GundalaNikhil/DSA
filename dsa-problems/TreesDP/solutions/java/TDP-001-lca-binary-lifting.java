import java.util.*;

class Solution {
    private int LOG = 20; // log2(200000) ≈ 18
    private List<Integer>[] tree;
    private int[][] up;
    private int[] depth;
    private int n;

    public void preprocess(int root, int n, int[][] edges) {
        this.n = n;
        tree = new ArrayList[n + 1];
        up = new int[n + 1][LOG];
        depth = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            tree[i] = new ArrayList<>();
            Arrays.fill(up[i], -1);
        }

        // Build adjacency list
        for (int[] edge : edges) {
            tree[edge[0]].add(edge[1]);
            tree[edge[1]].add(edge[0]);
        }

        // DFS to compute depths and immediate parents
        dfs(root, -1, 0);

        // Binary lifting preprocessing
        for (int j = 1; j < LOG; j++) {
            for (int i = 1; i <= n; i++) {
                if (up[i][j - 1] != -1) {
                    up[i][j] = up[up[i][j - 1]][j - 1];
                }
            }
        }
    }

    private void dfs(int node, int parent, int d) {
        up[node][0] = parent;
        depth[node] = d;
        for (int child : tree[node]) {
            if (child != parent) {
                dfs(child, node, d + 1);
            }
        }
    }

    public int lca(int u, int v) {
        // Make u deeper
        if (depth[u] < depth[v]) {
            int temp = u;
            u = v;
            v = temp;
        }

        // Lift u to same level as v
        int diff = depth[u] - depth[v];
        for (int j = 0; j < LOG; j++) {
            if ((diff & (1 << j)) != 0) {
                u = up[u][j];
            }
        }

        if (u == v) return u;

        // Lift both simultaneously
        for (int j = LOG - 1; j >= 0; j--) {
            if (up[u][j] != -1 && up[u][j] != up[v][j]) {
                u = up[u][j];
                v = up[v][j];
            }
        }

        return up[u][0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        solution.preprocess(1, n, edges);

        for (int i = 0; i < q; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            System.out.println(solution.lca(u, v));
        }

        sc.close();
    }
}
