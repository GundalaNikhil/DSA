import java.util.*;

class Solution {
    public List<Integer> bottomViewWithLimit(int n, int[] values, int[] left, int[] right, int D) {
        if (n == 0) return new ArrayList<>();

        Map<Integer, Integer> map = new TreeMap<>();
        Queue<int[]> q = new LinkedList<>(); // {u, col, depth}
        q.offer(new int[]{0, 0, 0});

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int c = curr[1];
            int d = curr[2];

            // Update map since d <= D (guaranteed by check before adding to queue)
            map.put(c, values[u]);

            // Only add children if current depth < D
            if (d < D) {
                if (left[u] != -1) q.offer(new int[]{left[u], c - 1, d + 1});
                if (right[u] != -1) q.offer(new int[]{right[u], c + 1, d + 1});
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int val : map.values()) {
            result.add(val);
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
        int D = 0;
        if (sc.hasNextInt()) D = sc.nextInt();

        Solution solution = new Solution();
        List<Integer> ans = solution.bottomViewWithLimit(n, values, left, right, D);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
