import java.util.*;

class Solution {
    public List<Integer> findOrder(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        int[] inDegree = new int[n];

        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            inDegree[edge[1]]++;
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                q.offer(i);
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.poll();
            result.add(u);

            for (int v : adj.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    q.offer(v);
                }
            }
        }

        if (result.size() == n) {
            return result;
        } else {
            return new ArrayList<>();
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
        for(int i=0; i<m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }
        
        Solution sol = new Solution();
        List<Integer> res = sol.findOrder(n, edges);
        if(res.isEmpty()) {
            System.out.println("IMPOSSIBLE");
        } else {
            for(int i=0; i<res.size(); i++) {
                System.out.print(res.get(i) + (i==res.size()-1?"":" "));
            }
            System.out.println();
        }
        sc.close();
    }
}
