import java.util.*;

class Solution {
    public List<List<Integer>> allOrderings(int n, int[][] edges) {
        List<List<Integer>> result = new ArrayList<>();
        int[] indegree = new int[n];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            indegree[edge[1]]++;
        }
        
        boolean[] visited = new boolean[n];
        backtrack(n, adj, indegree, visited, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int n, List<List<Integer>> adj, int[] indegree, boolean[] visited, 
                           List<Integer> path, List<List<Integer>> result) {
        if (path.size() == n) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i] && indegree[i] == 0) {
                // Choose i
                visited[i] = true;
                path.add(i);
                for (int neighbor : adj.get(i)) {
                    indegree[neighbor]--;
                }

                backtrack(n, adj, indegree, visited, path, result);

                // Backtrack
                for (int neighbor : adj.get(i)) {
                    indegree[neighbor]++;
                }
                path.remove(path.size() - 1);
                visited[i] = false;
            }
        }
    }
}
