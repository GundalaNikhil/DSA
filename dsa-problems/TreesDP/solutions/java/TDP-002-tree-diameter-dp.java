import java.util.*;

class Solution {
    private List<Integer>[] tree;
    private int diameter = 0;

    public int treeDiameter(int n, int[][] edges) {
        tree = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            tree[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            tree[edge[0]].add(edge[1]);
            tree[edge[1]].add(edge[0]);
        }

        dfs(1, -1);
        return diameter;
    }

    private int dfs(int node, int parent) {
        int max1 = 0, max2 = 0;

        for (int child : tree[node]) {
            if (child == parent) continue;

            int childDepth = dfs(child, node);

            if (childDepth > max1) {
                max2 = max1;
                max1 = childDepth;
            } else if (childDepth > max2) {
                max2 = childDepth;
            }
        }

        diameter = Math.max(diameter, max1 + max2);
        return max1 + 1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.treeDiameter(n, edges);

        System.out.println(result);
        sc.close();
    }
}
