import java.util.*;

class Main {
    static List<int[]>[] adj;
    static int n;

    static long bfs(int start, Map<Integer, Long> marked) {
        long[] dist = new long[n + 1];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[start] = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int[] edge : adj[u]) {
                int v = edge[0];
                long w = edge[1];
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    q.add(v);
                }
            }
        }
        long minCost = Long.MAX_VALUE;
        for (Map.Entry<Integer, Long> e : marked.entrySet()) {
            int node = e.getKey();
            long val = e.getValue();
            if (dist[node] != Long.MAX_VALUE) {
                minCost = Math.min(minCost, dist[node] + val);
            }
        }
        return minCost;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int D = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt(), w = sc.nextInt();
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        int q = sc.nextInt();
        Map<Integer, Long> marked = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        while (q-- > 0) {
            int type = sc.nextInt();
            if (type == 1) {
                int v = sc.nextInt();
                long val = sc.nextLong();
                int t = sc.nextInt();
                marked.put(v, val);
            } else {
                int v = sc.nextInt();
                int t = sc.nextInt();
                sb.append(bfs(v, marked)).append("\n");
            }
        }
        System.out.print(sb);
    }
}
