import java.util.*;

class Solution {
    public long mstPrim(int n, List<List<int[]>> adj) {
        long mstWeight = 0;
        boolean[] visited = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        
        // {weight, node}
        pq.offer(new int[]{0, 0});
        
        int nodesCount = 0;
        
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int w = curr[0];
            int u = curr[1];
            
            if (visited[u]) continue;
            
            visited[u] = true;
            mstWeight += w;
            nodesCount++;
            
            if (nodesCount == n) break; // Optimization
            
            for (int[] edge : adj.get(u)) {
                int v = edge[0];
                int weight = edge[1];
                if (!visited[v]) {
                    pq.offer(new int[]{weight, v});
                }
            }
        }
        
        return mstWeight;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
            adj.get(v).add(new int[]{u, w});
        }

        Solution solution = new Solution();
        System.out.println(solution.mstPrim(n, adj));
        sc.close();
    }
}
