import java.util.*;

class Solution {
    public int[] checkFeasibility(int n, int[][] edges) {
        int[] indegree = new int[n];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        // Build graph
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            indegree[edge[1]]++;
        }

        // Count and collect indegree 0 nodes
        int initialZeros = 0;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                initialZeros++;
            }
        }

        // Initialize queue with indegree 0 nodes in sorted order
        List<Integer> zeroIndegreeNodes = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                zeroIndegreeNodes.add(i);
            }
        }
        Collections.sort(zeroIndegreeNodes);

        // Sort neighbors for deterministic processing
        for (List<Integer> neighbors : adj) {
            Collections.sort(neighbors);
        }

        Queue<Integer> queue = new LinkedList<>(zeroIndegreeNodes);
        int processed = 0;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            processed++;

            for (int v : adj.get(u)) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    queue.offer(v);
                }
            }
        }

        if (processed == n) {
            return new int[]{1, initialZeros};
        } else {
            return new int[]{-1};
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.checkFeasibility(n, edges);

        if (result.length == 1) {
            System.out.println(result[0]);
        } else {
            System.out.println(result[0] + " " + result[1]);
        }
        sc.close();
    }
}
