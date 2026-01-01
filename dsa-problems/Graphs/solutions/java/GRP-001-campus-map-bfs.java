import java.util.*;

class Solution {
    public List<Integer> bfsTraversal(int n, List<List<Integer>> adj) {
        List<Integer> result = new ArrayList<>();
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        
        // Start BFS from node 0
        queue.offer(0);
        visited[0] = true;
        
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            result.add(curr);
            
            // Visit all unvisited neighbors
            for (int neighbor : adj.get(curr)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }
        
        return result;
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
        List<Integer> result = solution.bfsTraversal(n, adj);
        
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i < result.size() - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
