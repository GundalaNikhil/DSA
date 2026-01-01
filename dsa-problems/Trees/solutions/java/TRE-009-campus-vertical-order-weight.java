import java.io.*;
import java.util.*;

class Solution {
    static class NodeInfo {
        int val;
        int weight;
        int depth;
        NodeInfo(int val, int weight, int depth) {
            this.val = val;
            this.weight = weight;
            this.depth = depth;
        }
    }

    public List<List<Integer>> verticalOrderWithWeights(int n, int[] values, int[] weights,
                                                       int[] left, int[] right, int W) {
        if (n == 0) return new ArrayList<>();

        boolean[] hasParent = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (left[i] != -1) hasParent[left[i]] = true;
            if (right[i] != -1) hasParent[right[i]] = true;
        }
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (!hasParent[i]) {
                root = i;
                break;
            }
        }

        Map<Integer, List<NodeInfo>> cols = new HashMap<>();
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{root, 0, 0});
        boolean[] visited = new boolean[n];
        visited[root] = true;

        int minCol = 0;
        int maxCol = 0;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int c = curr[1];
            int d = curr[2];

            cols.computeIfAbsent(c, k -> new ArrayList<>()).add(new NodeInfo(values[u], weights[u], d));
            minCol = Math.min(minCol, c);
            maxCol = Math.max(maxCol, c);

            if (left[u] != -1 && !visited[left[u]]) {
                visited[left[u]] = true;
                q.add(new int[]{left[u], c - 1, d + 1});
            }
            if (right[u] != -1 && !visited[right[u]]) {
                visited[right[u]] = true;
                q.add(new int[]{right[u], c + 1, d + 1});
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int c = minCol; c <= maxCol; c++) {
            List<NodeInfo> list = cols.get(c);
            if (list == null) continue;
            long totalWeight = 0;
            for (NodeInfo node : list) totalWeight += node.weight;
            if (totalWeight >= W) {
                list.sort((a, b) -> {
                    if (a.depth != b.depth) return a.depth - b.depth;
                    if (a.weight != b.weight) return b.weight - a.weight;
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

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> lines = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (!line.isEmpty()) lines.add(line);
        }
        if (lines.isEmpty()) return;

        int n = Integer.parseInt(lines.get(0));
        int[] values = new int[n];
        int[] weights = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n && i + 1 < lines.size(); i++) {
            String[] parts = lines.get(i + 1).split("\\s+");
            if (parts.length < 3) continue;
            values[i] = Integer.parseInt(parts[0]);
            if (parts.length >= 4) {
                weights[i] = Integer.parseInt(parts[1]);
                left[i] = Integer.parseInt(parts[2]);
                right[i] = Integer.parseInt(parts[3]);
            } else {
                weights[i] = 1;
                left[i] = Integer.parseInt(parts[1]);
                right[i] = Integer.parseInt(parts[2]);
            }
        }

        int W = 0;
        if (lines.size() > n + 1) {
            W = Integer.parseInt(lines.get(n + 1));
        }

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
    }
}
