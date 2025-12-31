import java.util.*;

class Solution {
    private int timer;
    private int[] tin, low;
    private boolean[] visited;
    private List<List<Integer>> adj;
    private Set<Integer> articulationPoints;
    private List<List<Integer>> bccs;
    private Stack<int[]> edgeStack;

    public Object[] articulationAndBcc(int n, int[][] edges) {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        tin = new int[n];
        low = new int[n];
        visited = new boolean[n];
        articulationPoints = new TreeSet<>(); // Sorted
        bccs = new ArrayList<>();
        edgeStack = new Stack<>();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, -1);
                // If stack not empty after DFS (e.g. isolated edge or component), pop remaining
                if (!edgeStack.isEmpty()) {
                    Set<Integer> component = new HashSet<>();
                    while (!edgeStack.isEmpty()) {
                        int[] e = edgeStack.pop();
                        component.add(e[0]);
                        component.add(e[1]);
                    }
                    bccs.add(new ArrayList<>(component));
                }
            }
        }

        int[] aps = new int[articulationPoints.size()];
        int idx = 0;
        for (int ap : articulationPoints) aps[idx++] = ap;

        return new Object[]{aps, bccs};
    }

    private void dfs(int u, int p) {
        visited[u] = true;
        tin[u] = low[u] = timer++;
        int children = 0;

        for (int v : adj.get(u)) {
            if (v == p) continue;

            if (visited[v]) {
                low[u] = Math.min(low[u], tin[v]);
                if (tin[v] < tin[u]) { // Back-edge
                    edgeStack.push(new int[]{u, v});
                }
            } else {
                edgeStack.push(new int[]{u, v});
                children++;
                dfs(v, u);
                low[u] = Math.min(low[u], low[v]);

                if ((p != -1 && low[v] >= tin[u]) || (p == -1 && children > 1)) {
                    articulationPoints.add(u);
                }

                if (low[v] >= tin[u]) {
                    Set<Integer> bccNodes = new HashSet<>();
                    while (true) {
                        int[] e = edgeStack.pop();
                        bccNodes.add(e[0]);
                        bccNodes.add(e[1]);
                        if (e[0] == u && e[1] == v) break;
                    }
                    bccs.add(new ArrayList<>(bccNodes));
                }
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        Object[] res = solution.articulationAndBcc(n, edges);
        int[] aps = (int[]) res[0];
        @SuppressWarnings("unchecked")
        List<List<Integer>> bccs = (List<List<Integer>>) res[1];

        StringBuilder sb = new StringBuilder();
        sb.append(aps.length);
        if (aps.length > 0) {
            sb.append('\n');
            for (int i = 0; i < aps.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(aps[i]);
            }
        }
        sb.append('\n').append(bccs.size());
        for (List<Integer> bcc : bccs) {
            Collections.sort(bcc);
            sb.append('\n').append(bcc.size());
            for (int v : bcc) sb.append(' ').append(v);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
