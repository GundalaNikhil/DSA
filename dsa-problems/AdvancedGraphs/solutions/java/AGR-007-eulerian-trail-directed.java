import java.util.*;

class Solution {
    private List<Deque<Integer>> adj;
    private List<Integer> trail;

    public int[] eulerTrail(int n, int[][] edges) {
        int m = edges.length;
        if (m == 0) return new int[]{0};

        int[] in = new int[n];
        int[] out = new int[n];
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayDeque<>());

        for (int[] e : edges) {
            out[e[0]]++;
            in[e[1]]++;
            adj.get(e[0]).add(e[1]);
        }

        int startNode = -1;
        int endNode = -1;
        int diffCount = 0;

        for (int i = 0; i < n; i++) {
            if (out[i] == in[i] + 1) {
                if (startNode != -1) return null; // More than one start
                startNode = i;
                diffCount++;
            } else if (in[i] == out[i] + 1) {
                if (endNode != -1) return null; // More than one end
                endNode = i;
                diffCount++;
            } else if (in[i] != out[i]) {
                return null; // Invalid degree
            }
        }

        if (diffCount == 0) {
            // Circuit: find first node with edges
            for (int i = 0; i < n; i++) {
                if (out[i] > 0) {
                    startNode = i;
                    break;
                }
            }
        } else if (diffCount != 2) {
            return null;
        }

        if (startNode == -1) return null; // Should not happen if m > 0

        trail = new ArrayList<>();
        dfs(startNode);

        if (trail.size() != m + 1) return null; // Disconnected components

        int[] res = new int[trail.size()];
        for (int i = 0; i < trail.size(); i++) {
            res[i] = trail.get(trail.size() - 1 - i);
        }
        return res;
    }

    private void dfs(int u) {
        Deque<Integer> neighbors = adj.get(u);
        while (!neighbors.isEmpty()) {
            int v = neighbors.pollLast();
            dfs(v);
        }
        trail.add(u);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] trail = solution.eulerTrail(n, edges);
        if (trail == null) {
            System.out.print("NO");
        } else {
            StringBuilder sb = new StringBuilder();
            sb.append("YES\n");
            for (int i = 0; i < trail.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(trail[i]);
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
