import java.util.*;
public class SubtreeLIS {
    static List<Integer>[] adj;
    static int[] values, lis;
    static TreeMap<Integer, Integer> active;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        values = new int[n + 1];
        lis = new int[n + 1];

        for (int i = 1; i <= n; i++) values[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        active = new TreeMap<>();
        dfs(1, 0);

        for (int i = 1; i <= n; i++) {
            System.out.print(lis[i] + (i < n ? " " : "\n"));
        }
    }

    static void dfs(int u, int p) {
        Integer prev = active.floorKey(values[u]);
        int prevLen = (prev == null) ? 0 : active.get(prev);
        lis[u] = prevLen + 1;

        Integer next = active.ceilingKey(values[u]);
        int savedLen = (next != null && next == values[u]) ? active.get(next) : -1;

        if (savedLen == -1 || lis[u] > savedLen) {
            active.put(values[u], lis[u]);
        }

        for (int v : adj[u]) {
            if (v != p) dfs(v, u);
        }

        if (savedLen == -1) {
            active.remove(values[u]);
        } else {
            active.put(values[u], savedLen);
        }
    }
}
