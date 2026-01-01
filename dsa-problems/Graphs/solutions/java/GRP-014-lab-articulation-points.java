import java.util.*;

class Solution {
    private int time = 0;
    private Set<Integer> ap;

    public List<Integer> findArticulationPoints(int n, List<List<Integer>> adj) {
        int[] disc = new int[n];
        int[] low = new int[n];
        int[] parent = new int[n];
        Arrays.fill(disc, -1);
        Arrays.fill(parent, -1);
        ap = new HashSet<>();

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, adj, disc, low, parent);
            }
        }

        return new ArrayList<>(ap);
    }

    private void dfs(int u, List<List<Integer>> adj, int[] disc, int[] low, int[] parent) {
        int children = 0;
        disc[u] = low[u] = time++;

        // Sort neighbors for deterministic traversal
        List<Integer> neighbors = new ArrayList<>(adj.get(u));
        Collections.sort(neighbors);

        for (int v : neighbors) {
            if (disc[v] == -1) {
                children++;
                parent[v] = u;
                dfs(v, adj, disc, low, parent);

                low[u] = Math.min(low[u], low[v]);

                if (parent[u] != -1 && low[v] >= disc[u]) {
                    ap.add(u);
                }
            } else if (v != parent[u]) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }

        if (parent[u] == -1 && children > 1) {
            ap.add(u);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        Solution solution = new Solution();
        List<Integer> aps = solution.findArticulationPoints(n, adj);

        // Sort for deterministic output
        Collections.sort(aps);

        System.out.println(aps.size());
        if (!aps.isEmpty()) {
            for (int i = 0; i < aps.size(); i++) {
                System.out.print(aps.get(i));
                if (i < aps.size() - 1) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
