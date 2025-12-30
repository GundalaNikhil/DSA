import java.util.*;

class Solution {
    static class NodeInfo {
        int val, weight, depth;
        NodeInfo(int v, int w, int d) {
            this.val = v;
            this.weight = w;
            this.depth = d;
        }
    }

    public List<List<Integer>> verticalOrderWithWeights(int n, int[] values, int[] weights,
                                                       int[] left, int[] right, long W) {
        if (n == 0) return new ArrayList<>();

        Map<Integer, List<NodeInfo>> cols = new TreeMap<>();
        Queue<int[]> q = new LinkedList<>(); // {u, col, depth}
        q.offer(new int[]{0, 0, 0});

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int c = curr[1];
            int d = curr[2];

            cols.computeIfAbsent(c, k -> new ArrayList<>()).add(new NodeInfo(values[u], weights[u], d));

            if (left[u] != -1) q.offer(new int[]{left[u], c - 1, d + 1});
            if (right[u] != -1) q.offer(new int[]{right[u], c + 1, d + 1});
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int c : cols.keySet()) {
            List<NodeInfo> list = cols.get(c);
            long totalWeight = 0;
            for (NodeInfo node : list) totalWeight += node.weight;

            if (totalWeight >= W) {
                Collections.sort(list, (a, b) -> {
                    if (a.depth != b.depth) return a.depth - b.depth;
                    if (a.weight != b.weight) return b.weight - a.weight; // Descending
                    return a.val - b.val;
                });

                List<Integer> colValues = new ArrayList<>();
                for (NodeInfo node : list) colValues.add(node.val);
                result.add(colValues);
            }
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
        int[] weights = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            weights[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        long W = 0;
        if (sc.hasNextLong()) W = sc.nextLong();

        Solution solution = new Solution();
        List<List<Integer>> cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
        if (cols.isEmpty()) {
            System.out.println();
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < cols.size(); i++) {
                List<Integer> col = cols.get(i);
                for (int j = 0; j < col.size(); j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(col.get(j));
                }
                if (i + 1 < cols.size()) sb.append('\n');
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
