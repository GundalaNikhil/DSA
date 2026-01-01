import java.util.*;

class Solution {
    public int[] topoSort(int n, List<List<Integer>> adj) {
        int[] indegree = new int[n];
        for (int u = 0; u < n; u++) {
            for (int v : adj.get(u)) {
                indegree[v]++;
            }
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.offer(i);
            }
        }

        int[] result = new int[n];
        int idx = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            result[idx++] = u;

            for (int v : adj.get(u)) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.offer(v);
                }
            }
        }

        return result;
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
        int[] order = solution.topoSort(n, adj);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < order.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(order[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
