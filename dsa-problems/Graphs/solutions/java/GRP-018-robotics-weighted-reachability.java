import java.util.*;

class Solution {
    public int countReachable(int n, List<List<int[]>> adj, int threshold) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(0);
        visited.add(0);

        while (!queue.isEmpty()) {
            int node = queue.poll();

            // Sort neighbors for deterministic behavior
            List<int[]> neighbors = new ArrayList<>(adj.get(node));
            neighbors.sort((a, b) -> Integer.compare(a[0], b[0]));

            for (int[] edge : neighbors) {
                int neighbor = edge[0];
                int weight = edge[1];

                if (weight <= threshold && !visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }

        return visited.size();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int threshold = sc.nextInt();
        int m = sc.nextInt();

        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();

            if (w <= threshold) {
                adj.get(u).add(new int[]{v, w});
                adj.get(v).add(new int[]{u, w});
            }
        }

        Solution solution = new Solution();
        int result = solution.countReachable(n, adj, threshold);
        System.out.println(result);
        sc.close();
    }
}
