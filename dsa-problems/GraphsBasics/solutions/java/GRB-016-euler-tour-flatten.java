import java.util.*;

class Solution {
    private int timer;
    private int[] tin;
    private int[] tout;

    public int[][] eulerTour(int n, List<List<Integer>> adj, int root) {
        tin = new int[n];
        tout = new int[n];
        timer = 0;
        
        dfs(root, -1, adj);
        
        return new int[][]{tin, tout};
    }

    private void dfs(int u, int p, List<List<Integer>> adj) {
        tin[u] = timer++;
        
        for (int v : adj.get(u)) {
            if (v != p) {
                dfs(v, u, adj);
            }
        }
        
        // tout[u] is the max tin in the subtree.
        // Since timer increments monotonically, the current (timer-1) is the max tin seen so far.
        tout[u] = timer - 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        int root = sc.nextInt();

        Solution solution = new Solution();
        int[][] res = solution.eulerTour(n, adj, root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(res[0][i]);
        }
        sb.append('\n');
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(res[1][i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
