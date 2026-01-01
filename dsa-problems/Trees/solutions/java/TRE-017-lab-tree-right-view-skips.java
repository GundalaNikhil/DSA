import java.util.*;

class Solution {
    public List<Integer> rightViewWithSkips(int n, int[] values, int[] left, int[] right) {
        if (n == 0) return new ArrayList<>();
        
        Map<Integer, Integer> view = new HashMap<>();
        int maxDepth = dfs(0, 0, values, left, right, view);
        
        List<Integer> result = new ArrayList<>();
        for (int d = 0; d <= maxDepth; d++) {
            if (view.containsKey(d)) {
                result.add(view.get(d));
            }
        }
        return result;
    }

    private int dfs(int u, int depth, int[] values, int[] left, int[] right, Map<Integer, Integer> view) {
        if (u == -1) return -1;

        // If valid and first time seeing this depth (since we go Right -> Left)
        if (values[u] >= 0 && !view.containsKey(depth)) {
            view.put(depth, values[u]);
        }

        int d1 = dfs(right[u], depth + 1, values, left, right, view);
        int d2 = dfs(left[u], depth + 1, values, left, right, view);
        
        return Math.max(depth, Math.max(d1, d2));
    }
}

class Main {
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
        List<Integer> ans = solution.rightViewWithSkips(n, values, left, right);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
