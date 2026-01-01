import java.io.*;
import java.util.*;

class Solution {
    public int lcaBlocked(int n, int[] values, int[] blocked, int[] left, int[] right, int u, int v) {
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        for (int i = 0; i < n; i++) {
            if (left[i] != -1) parent[left[i]] = i;
            if (right[i] != -1) parent[right[i]] = i;
        }

        Set<Integer> ancestors = new HashSet<>();
        int curr = u;
        int steps = 0;
        while (curr != -1 && steps < n + 5) {
            ancestors.add(curr);
            curr = parent[curr];
            steps++;
        }

        int lca = -1;
        curr = v;
        steps = 0;
        while (curr != -1 && steps < n + 5) {
            if (ancestors.contains(curr)) {
                lca = curr;
                break;
            }
            curr = parent[curr];
            steps++;
        }

        if (lca == -1) return -1;

        steps = 0;
        while (lca != -1 && blocked[lca] == 1 && steps < n + 5) {
            lca = parent[lca];
            steps++;
        }

        return lca != -1 ? values[lca] : -1;
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
        int[] blocked = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n && i + 1 < lines.size(); i++) {
            String[] parts = lines.get(i + 1).split("\\s+");
            if (parts.length < 3) continue;
            values[i] = Integer.parseInt(parts[0]);
            if (parts.length >= 4) {
                blocked[i] = Integer.parseInt(parts[1]);
                left[i] = Integer.parseInt(parts[2]);
                right[i] = Integer.parseInt(parts[3]);
            } else {
                blocked[i] = 0;
                left[i] = Integer.parseInt(parts[1]);
                right[i] = Integer.parseInt(parts[2]);
            }
        }

        if (lines.size() <= n + 1) return;
        String[] uv = lines.get(n + 1).split("\\s+");
        if (uv.length < 2) return;
        int u = Integer.parseInt(uv[0]);
        int v = Integer.parseInt(uv[1]);

        Solution solution = new Solution();
        System.out.println(solution.lcaBlocked(n, values, blocked, left, right, u, v));
    }
}
