import java.util.*;

class Solution {
    static class NodeEntry {
        int val;
        int depth;
        NodeEntry(int v, int d) {
            this.val = v;
            this.depth = d;
        }
    }

    public List<Integer> topView(int n, int[] values, int[] left, int[] right) {
        if (n == 0) return new ArrayList<>();

        Map<Integer, NodeEntry> map = new TreeMap<>();
        Queue<int[]> q = new LinkedList<>(); // {u, col, depth}
        q.offer(new int[]{0, 0, 0});

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int c = curr[1];
            int d = curr[2];

            if (!map.containsKey(c)) {
                map.put(c, new NodeEntry(values[u], d));
            } else {
                NodeEntry existing = map.get(c);
                if (d < existing.depth) {
                    // Should not happen with BFS unless we revisit? BFS is level-order.
                    map.put(c, new NodeEntry(values[u], d));
                } else if (d == existing.depth) {
                    if (values[u] > existing.val) {
                        existing.val = values[u];
                    }
                }
            }

            if (left[u] != -1) q.offer(new int[]{left[u], c - 1, d + 1});
            if (right[u] != -1) q.offer(new int[]{right[u], c + 1, d + 1});
        }

        List<Integer> result = new ArrayList<>();
        for (int c : map.keySet()) {
            result.add(map.get(c).val);
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<Integer> ans = solution.topView(n, values, left, right);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
