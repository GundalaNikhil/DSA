import java.util.*;

class Solution {
    public int[] shortestDistances(int n, List<List<Integer>> adj, int source) {
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        dist[source] = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(source);

        while (!queue.isEmpty()) {
            int node = queue.poll();

            // Sort neighbors for deterministic traversal
            List<Integer> neighbors = new ArrayList<>(adj.get(node));
            Collections.sort(neighbors);
            for (int neighbor : neighbors) {
                if (dist[neighbor] == -1) {
                    dist[neighbor] = dist[node] + 1;
                    queue.offer(neighbor);
                }
            }
        }

        return dist;
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

        // Handle optional source input
        int source = 0;
        if (sc.hasNextInt()) {
            source = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.shortestDistances(n, adj, source);

        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
