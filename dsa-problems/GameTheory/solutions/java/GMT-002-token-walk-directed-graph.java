import java.util.*;

class Solution {
    List<Integer>[] adj;
    int[] memo; // -1: unknown, 0: Losing, 1: Winning

    public List<String> determineWinningNodes(int n, int[][] edges) {
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
        }

        memo = new int[n];
        Arrays.fill(memo, -1);

        List<String> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (dfs(i)) result.add("Winning");
            else result.add("Losing");
        }
        return result;
    }

    private boolean dfs(int u) {
        if (memo[u] != -1) return memo[u] == 1;

        boolean canReachLosing = false;
        for (int v : adj[u]) {
            if (!dfs(v)) { // If v is Losing
                canReachLosing = true;
                break;
            }
        }

        memo[u] = canReachLosing ? 1 : 0;
        return canReachLosing;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] edges = new int[m][2];
            for (int i = 0; i < m; i++) {
                edges[i][0] = sc.nextInt();
                edges[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            List<String> result = solution.determineWinningNodes(n, edges);
            
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
            }
            System.out.println();
        }
        sc.close();
    }
}
