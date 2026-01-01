import java.util.*;

class Solution {
    public boolean hasCycle(int n, List<List<Integer>> adj) {
        int[] state = new int[n]; // 0: unvisited, 1: visiting, 2: visited
        for (int i = 0; i < n; i++) {
            if (state[i] == 0) {
                if (dfs(i, adj, state)) return true;
            }
        }
        return false;
    }

    private boolean dfs(int u, List<List<Integer>> adj, int[] state) {
        state[u] = 1; // Mark as visiting
        for (int v : adj.get(u)) {
            if (state[v] == 1) return true; // Found a back edge to a node in current stack
            if (state[v] == 0) {
                if (dfs(v, adj, state)) return true;
            }
        }
        state[u] = 2; // Mark as visited
        return false;
    }
}

class Main {
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
        System.out.println(solution.hasCycle(n, adj) ? "1" : "0");
        sc.close();
    }
}
