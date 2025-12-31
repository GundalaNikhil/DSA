import java.util.*;

class Solution {
    private int timer;
    private int[] tin, low;
    private boolean[] onStack;
    private Stack<Integer> stack;
    private List<List<Integer>> sccs;
    private List<List<Integer>> adj;

    public Object[] sccCompress(int n, List<List<Integer>> adjList) {
        this.adj = adjList;
        tin = new int[n];
        low = new int[n];
        Arrays.fill(tin, -1);
        onStack = new boolean[n];
        stack = new Stack<>();
        sccs = new ArrayList<>();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (tin[i] == -1) {
                dfs(i);
            }
        }

        int k = sccs.size();
        int[] comp = new int[n];
        // Assign component IDs (reverse topological order usually, but here arbitrary 0..k-1)
        for (int i = 0; i < k; i++) {
            for (int node : sccs.get(i)) {
                comp[node] = i; // Or k - 1 - i for topo order
            }
        }

        // Build Condensation Graph
        Set<String> seenEdges = new HashSet<>();
        List<int[]> dagEdges = new ArrayList<>();

        for (int u = 0; u < n; u++) {
            for (int v : adj.get(u)) {
                if (comp[u] != comp[v]) {
                    String key = comp[u] + "," + comp[v];
                    if (!seenEdges.contains(key)) {
                        seenEdges.add(key);
                        dagEdges.add(new int[]{comp[u], comp[v]});
                    }
                }
            }
        }

        // Sort edges for consistent output
        dagEdges.sort((a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));

        return new Object[]{k, comp, dagEdges};
    }

    private void dfs(int u) {
        tin[u] = low[u] = timer++;
        stack.push(u);
        onStack[u] = true;

        for (int v : adj.get(u)) {
            if (tin[v] == -1) {
                dfs(v);
                low[u] = Math.min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = Math.min(low[u], tin[v]);
            }
        }

        if (low[u] == tin[u]) {
            List<Integer> component = new ArrayList<>();
            while (true) {
                int v = stack.pop();
                onStack[v] = false;
                component.add(v);
                if (u == v) break;
            }
            sccs.add(component);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
        }

        Solution solution = new Solution();
        Object[] res = solution.sccCompress(n, adj);
        int k = (int) res[0];
        int[] comp = (int[]) res[1];
        @SuppressWarnings("unchecked")
        List<int[]> edges = (List<int[]>) res[2];

        StringBuilder sb = new StringBuilder();
        sb.append(k).append('\n');
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(comp[i]);
        }
        sb.append('\n').append(edges.size()).append('\n');
        for (int[] e : edges) sb.append(e[0]).append(' ').append(e[1]).append('\n');
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
