import java.util.*;

class Solution {
    public List<List<Integer>> oddDepthLevels(int n, int[] left, int[] right, int[] values) {
        List<List<Integer>> result = new ArrayList<>();
        if (n == 0) return result;

        Queue<Integer> q = new LinkedList<>();
        q.offer(0);
        int depth = 0;

        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> currentLevel = new ArrayList<>();
            boolean isOdd = (depth % 2 != 0);

            for (int i = 0; i < size; i++) {
                int u = q.poll();
                if (isOdd) {
                    currentLevel.add(values[u]);
                }
                
                if (left[u] != -1) q.offer(left[u]);
                if (right[u] != -1) q.offer(right[u]);
            }

            if (isOdd) {
                result.add(currentLevel);
            }
            depth++;
        }
        return result;
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
        List<List<Integer>> levels = solution.oddDepthLevels(n, left, right, values);
        if (levels.isEmpty()) {
            System.out.println();
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < levels.size(); i++) {
                List<Integer> lvl = levels.get(i);
                for (int j = 0; j < lvl.size(); j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(lvl.get(j));
                }
                if (i + 1 < levels.size()) sb.append('\n');
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
