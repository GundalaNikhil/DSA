import java.util.*;

class Solution {
    public int treeHeight(int n, int[] left, int[] right) {
        if (n == 0) return -1;
        return dfs(0, left, right);
    }

    private int dfs(int u, int[] left, int[] right) {
        if (u == -1) return -1;
        int lHeight = dfs(left[u], left, right);
        int rHeight = dfs(right[u], left, right);
        return 1 + Math.max(lHeight, rHeight);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            int val = sc.nextInt(); // Value is unused for height
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.treeHeight(n, left, right));
        sc.close();
    }
}
