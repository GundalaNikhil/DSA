import java.util.*;

class Solution {
    public long[] dijkstra(int n, List<List<int[]>> adj, int source) {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[source] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[]{0, source});

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long d = curr[0];
            int node = (int)curr[1];

            if (d > dist[node]) continue;

            List<int[]> neighbors = new ArrayList<>(adj.get(node));
            neighbors.sort((a, b) -> {
                if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
                return Integer.compare(a[0], b[0]);
            });

            for (int[] edge : neighbors) {
                int neighbor = edge[0];
                long weight = edge[1];
                long newDist = dist[node] + weight;

                if (newDist < dist[neighbor]) {
                    dist[neighbor] = newDist;
                    pq.offer(new long[]{newDist, neighbor});
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

        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        // Handle optional source input
        int source = 0;
        if (sc.hasNextInt()) {
            source = sc.nextInt();
        }

        Solution solution = new Solution();
        long[] result = solution.dijkstra(n, adj, source);

        for (int i = 0; i < result.length; i++) {
            long val = result[i] == Long.MAX_VALUE ? -1 : result[i];
            System.out.print(val);
            if (i < result.length - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
