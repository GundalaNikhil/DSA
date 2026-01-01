import java.util.*;

class Main {
    static int n, timer;
    static List<int[]>[] adj;
    static int[] parent, depth, heavy, head, pos, values;
    static long[] segTree;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        values = new int[n + 1];
        for (int i = 1; i <= n; i++) values[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(new int[]{v});
            adj[v].add(new int[]{u});
        }

        parent = new int[n + 1];
        depth = new int[n + 1];
        heavy = new int[n + 1];
        head = new int[n + 1];
        pos = new int[n + 1];

        Arrays.fill(heavy, -1);

        dfs1(1, 0);
        timer = 0;
        dfs2(1, 1);

        segTree = new long[4 * n];
        build(1, 0, n - 1);

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            System.out.println(queryPath(u, v));
        }
    }

    static int dfs1(int u, int p) {
        int size = 1, maxSize = 0;
        parent[u] = p;
        depth[u] = (p == 0) ? 0 : depth[p] + 1;

        for (int[] edge : adj[u]) {
            int v = edge[0];
            if (v == p) continue;
            int subtreeSize = dfs1(v, u);
            size += subtreeSize;
            if (subtreeSize > maxSize) {
                maxSize = subtreeSize;
                heavy[u] = v;
            }
        }
        return size;
    }

    static void dfs2(int u, int h) {
        head[u] = h;
        pos[u] = timer++;

        if (heavy[u] != -1) {
            dfs2(heavy[u], h);
        }

        for (int[] edge : adj[u]) {
            int v = edge[0];
            if (v != parent[u] && v != heavy[u]) {
                dfs2(v, v);
            }
        }
    }

    static void build(int node, int l, int r) {
        if (l == r) {
            for (int i = 1; i <= n; i++) {
                if (pos[i] == l) {
                    segTree[node] = values[i];
                    break;
                }
            }
            return;
        }
        int mid = (l + r) / 2;
        build(2 * node, l, mid);
        build(2 * node + 1, mid + 1, r);
        segTree[node] = segTree[2 * node] + segTree[2 * node + 1];
    }

    static long query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return segTree[node];
        int mid = (l + r) / 2;
        return query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr);
    }

    static long queryPath(int u, int v) {
        long result = 0;
        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]]) {
                int temp = u; u = v; v = temp;
            }
            result += query(1, 0, n - 1, pos[head[u]], pos[u]);
            u = parent[head[u]];
        }
        if (depth[u] > depth[v]) {
            int temp = u; u = v; v = temp;
        }
        result += query(1, 0, n - 1, pos[u], pos[v]);
        return result;
    }
}
