import java.io.*;
import java.util.*;

class Solution {
    private long maxDiameter = 0;

    public long weightedDiameter(int n, int[] left, int[] right, long[] lw, long[] rw) {
        if (n == 0) return 0;
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

        maxDiameter = 0;
        dfs(root, left, right, lw, rw);
        return maxDiameter;
    }

    private long dfs(int u, int[] left, int[] right, long[] lw, long[] rw) {
        if (u == -1) return 0;
        long lPath = 0;
        long rPath = 0;
        if (left[u] != -1) {
            lPath = lw[u] + dfs(left[u], left, right, lw, rw);
        }
        if (right[u] != -1) {
            rPath = rw[u] + dfs(right[u], left, right, lw, rw);
        }
        if (lPath + rPath > maxDiameter) {
            maxDiameter = lPath + rPath;
        }
        return Math.max(lPath, rPath);
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
        int[] left = new int[n];
        int[] right = new int[n];
        long[] lw = new long[n];
        long[] rw = new long[n];

        for (int i = 0; i < n && i + 1 < lines.size(); i++) {
            String[] parts = lines.get(i + 1).split("\\s+");
            if (parts.length < 3) continue;
            left[i] = Integer.parseInt(parts[1]);
            right[i] = Integer.parseInt(parts[2]);
            if (parts.length >= 5) {
                lw[i] = Long.parseLong(parts[3]);
                rw[i] = Long.parseLong(parts[4]);
            } else {
                lw[i] = 1;
                rw[i] = 1;
            }
        }

        Solution solution = new Solution();
        System.out.println(solution.weightedDiameter(n, left, right, lw, rw));
    }
}
