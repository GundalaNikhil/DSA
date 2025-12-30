import java.util.*;

class Solution {
    public List<Integer> boundaryWithGaps(int n, int[] values, int[] left, int[] right) {
        List<Integer> result = new ArrayList<>();
        if (n == 0) return result;

        // 1. Root
        if (values[0] >= 0) {
            result.add(values[0]);
        }

        if (left[0] == -1 && right[0] == -1) {
            return result; // Single node, already added
        }

        // 2. Left Boundary
        int curr = left[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break; // Is leaf
            if (values[curr] >= 0) result.add(values[curr]);
            if (left[curr] != -1) curr = left[curr];
            else curr = right[curr];
        }

        // 3. Leaves
        addLeaves(0, values, left, right, result);

        // 4. Right Boundary
        List<Integer> rightBound = new ArrayList<>();
        curr = right[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break; // Is leaf
            if (values[curr] >= 0) rightBound.add(values[curr]);
            if (right[curr] != -1) curr = right[curr];
            else curr = left[curr];
        }
        Collections.reverse(rightBound);
        result.addAll(rightBound);

        return result;
    }

    private void addLeaves(int u, int[] values, int[] left, int[] right, List<Integer> result) {
        if (u == -1) return;
        if (left[u] == -1 && right[u] == -1) {
            if (values[u] >= 0) result.add(values[u]);
            return;
        }
        addLeaves(left[u], values, left, right, result);
        addLeaves(right[u], values, left, right, result);
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
        List<Integer> ans = solution.boundaryWithGaps(n, values, left, right);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
