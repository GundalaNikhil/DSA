import java.util.*;

class Main {
    static List<Integer>[] adj;
    static int[] values, lis;
    static ArrayList<Integer> active;

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
            adj[u].add(v);
            adj[v].add(u);
        }

        active = new ArrayList<>();
        dfs(1, 0);

        for (int i = 1; i <= n; i++) {
            System.out.print(lis[i] + (i < n ? " " : "\n"));
        }
    }

    static void dfs(int u, int p) {
        int pos = Collections.binarySearch(active, values[u]);
        if (pos < 0) pos = -(pos + 1);
        
        Integer saved = (pos < active.size()) ? active.get(pos) : null;

        if (pos < active.size()) {
            active.set(pos, values[u]);
        } else {
            active.add(values[u]);
        }

        lis[u] = active.size();

        for (int v : adj[u]) {
            if (v != p) dfs(v, u);
        }

        if (saved != null) {
            active.set(pos, saved);
        } else {
            active.remove(active.size() - 1);
        }
    }
}
