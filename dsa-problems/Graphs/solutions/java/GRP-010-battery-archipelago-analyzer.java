import java.util.*;

class Solution {
    public int shortestPathWithBattery(int n, List<int[]> edges, int source, int dest, int battery) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(new int[]{e[1], e[2]});
            adj.get(e[1]).add(new int[]{e[0], e[2]});
        }

        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[source] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{source, 0});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int u = curr[0];
            int d = curr[1];

            if (d > dist[u]) continue;
            if (u == dest) return d;

            for (int[] neighbor : adj.get(u)) {
                int v = neighbor[0];
                int w = neighbor[1];

                if (w <= battery) { // Constraint Check
                    if (dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                        pq.offer(new int[]{v, dist[v]});
                    }
                }
            }
        }

        return dist[dest] == Integer.MAX_VALUE ? -1 : dist[dest];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            edges.add(new int[]{u, v, w});
        }
        
        int source = sc.nextInt();
        int dest = sc.nextInt();
        int battery = sc.nextInt();
        
        Solution solution = new Solution();
        System.out.println(solution.shortestPathWithBattery(n, edges, source, dest, battery));
        sc.close();
    }
}
