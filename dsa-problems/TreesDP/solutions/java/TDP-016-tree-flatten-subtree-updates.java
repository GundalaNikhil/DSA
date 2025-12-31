import java.util.*;
public class TreeFlattenUpdates {
    static int timer;
    static int[] in, out, values;
    static List<Integer>[] adj;
    static long[] fenwick;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        values = new int[n + 1];
        for (int i = 1; i <= n; i++) values[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        in = new int[n + 1];
        out = new int[n + 1];
        timer = 0;
        dfs(1, 0);

        fenwick = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            update(in[i], values[i]);
            update(in[i] + 1, -values[i]);
        }

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int type = sc.nextInt();
            if (type == 1) {
                int u = sc.nextInt(), val = sc.nextInt();
                rangeUpdate(in[u], out[u], val);
            } else {
                int u = sc.nextInt();
                System.out.println(query(in[u]));
            }
        }
    }

    static void dfs(int u, int p) {
        in[u] = ++timer;
        for (int v : adj[u]) {
            if (v != p) dfs(v, u);
        }
        out[u] = timer;
    }

    static void update(int i, long val) {
        while (i < fenwick.length) {
            fenwick[i] += val;
            i += i & (-i);
        }
    }

    static long query(int i) {
        long sum = 0;
        while (i > 0) {
            sum += fenwick[i];
            i -= i & (-i);
        }
        return sum;
    }

    static void rangeUpdate(int l, int r, int val) {
        update(l, val);
        update(r + 1, -val);
    }
}
