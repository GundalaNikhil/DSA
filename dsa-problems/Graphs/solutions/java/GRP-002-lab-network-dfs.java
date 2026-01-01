import java.util.*;

class Solution {
    private List<Integer> result;
    private boolean[] visited;
    
    public List<Integer> dfsTraversal(int n, List<List<Integer>> adj) {
        result = new ArrayList<>();
        visited = new boolean[n];
        
        // Start DFS from node 0
        dfs(0, adj);
        
        return result;
    }
    
    private void dfs(int node, List<List<Integer>> adj) {
        // Mark as visited and add to result (preorder)
        visited[node] = true;
        result.add(node);
        
        // Recursively visit all unvisited neighbors
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj);
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

        // Sort neighbors for deterministic traversal
        for (int i = 0; i < n; i++) {
            Collections.sort(adj.get(i));
        }

        Solution solution = new Solution();
        List<Integer> result = solution.dfsTraversal(n, adj);
        
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i < result.size() - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
