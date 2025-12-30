import java.util.*;

class Solution {
    public int[] bipartiteColors(int n, List<List<Integer>> adj) {
        int[] colors = new int[n];
        Arrays.fill(colors, -1);

        for (int i = 0; i < n; i++) {
            if (colors[i] == -1) {
                if (!bfs(i, adj, colors)) return null;
            }
        }
        return colors;
    }

    private boolean bfs(int start, List<List<Integer>> adj, int[] colors) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        colors[start] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj.get(u)) {
                if (colors[v] == -1) {
                    colors[v] = 1 - colors[u];
                    q.offer(v);
                } else if (colors[v] == colors[u]) {
                    return false;
                }
            }
        }
        return true;
    }
}

public class Main {
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
            adj.get(v).add(u);
        }

        Solution solution = new Solution();
        int[] colors = solution.bipartiteColors(n, adj);
        if (colors == null) {
            System.out.print("false");
        } else {
            StringBuilder sb = new StringBuilder();
            sb.append("true\n");
            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(colors[i]);
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
