import java.util.*;

public class PathQueriesRMQ {
    static int n, timer;
    static List<int[]>[] adj;
    static int[] first, depth, dist, euler, parent;
    static int[][] st;
    static int logSize;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt(), w = sc.nextInt();
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        first = new int[n + 1];
        depth = new int[n + 1];
        dist = new int[n + 1];
        euler = new int[2 * n];
        timer = 0;

        dfs(1, 0, 0, 0);

        buildSparseTable();

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            System.out.println(queryDistance(u, v));
        }
    }

    static void dfs(int u, int p, int d, int distance) {
        depth[u] = d;
        dist[u] = distance;
        first[u] = timer;
        euler[timer++] = u;

        for (int[] edge : adj[u]) {
            int v = edge[0], w = edge[1];
            if (v != p) {
                dfs(v, u, d + 1, distance + w);
                euler[timer++] = u;
            }
        }
    }

    static void buildSparseTable() {
        int size = timer;
        logSize = (int)(Math.log(size) / Math.log(2)) + 1;
        st = new int[size][logSize];

        for (int i = 0; i < size; i++) {
            st[i][0] = i;
        }

        for (int j = 1; j < logSize; j++) {
            for (int i = 0; i + (1 << j) <= size; i++) {
                int left = st[i][j - 1];
                int right = st[i + (1 << (j - 1))][j - 1];
                st[i][j] = (depth[euler[left]] <= depth[euler[right]]) ? left : right;
            }
        }
    }

    static int queryLCA(int u, int v) {
        int l = first[u], r = first[v];
        if (l > r) {
            int temp = l; l = r; r = temp;
        }

        int len = r - l + 1;
        int k = (int)(Math.log(len) / Math.log(2));

        int left = st[l][k];
        int right = st[r - (1 << k) + 1][k];

        int lcaIdx = (depth[euler[left]] <= depth[euler[right]]) ? left : right;
        return euler[lcaIdx];
    }

    static int queryDistance(int u, int v) {
        int lca = queryLCA(u, v);
        return dist[u] + dist[v] - 2 * dist[lca];
    }
}
