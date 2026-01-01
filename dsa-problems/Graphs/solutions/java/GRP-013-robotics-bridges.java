import java.util.*;

class Solution {
    private int time = 0;
    private List<int[]> bridges;

    public List<int[]> findBridges(int n, List<List<Integer>> adj) {
        int[] disc = new int[n];
        int[] low = new int[n];
        int[] parent = new int[n];
        Arrays.fill(disc, -1);
        Arrays.fill(parent, -1);
        bridges = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, adj, disc, low, parent);
            }
        }

        return bridges;
    }

    private void dfs(int u, List<List<Integer>> adj, int[] disc, int[] low, int[] parent) {
        disc[u] = low[u] = time++;

        // Sort neighbors for deterministic traversal
        List<Integer> neighbors = new ArrayList<>(adj.get(u));
        Collections.sort(neighbors);

        for (int v : neighbors) {
            if (disc[v] == -1) {
                parent[v] = u;
                dfs(v, adj, disc, low, parent);

                low[u] = Math.min(low[u], low[v]);

                if (low[v] > disc[u]) {
                    bridges.add(new int[]{u, v});
                }
            } else if (v != parent[u]) {
                low[u] = Math.min(low[u], disc[v]);
            }
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
        List<int[]> bridges = solution.findBridges(n, adj);

        // Sort bridges for deterministic output
        bridges.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });

        System.out.println(bridges.size());
        for (int[] bridge : bridges) {
            System.out.println(bridge[0] + " " + bridge[1]);
        }
        sc.close();
    }
}
