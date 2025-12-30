import java.util.*;

class Solution {
    private List<Integer>[] tree;
    private int[] values;
    private int[] subtreeSize;
    private long[] subtreeSum;

    public void computeSubtreeMetrics(int n, int[] nodeValues, int[][] edges) {
        tree = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            tree[i] = new ArrayList<>();
        }

        values = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            values[i] = nodeValues[i - 1];
        }

        for (int[] edge : edges) {
            tree[edge[0]].add(edge[1]);
            tree[edge[1]].add(edge[0]);
        }

        subtreeSize = new int[n + 1];
        subtreeSum = new long[n + 1];

        dfs(1, -1);
    }

    private void dfs(int node, int parent) {
        subtreeSize[node] = 1;
        subtreeSum[node] = values[node];

        for (int child : tree[node]) {
            if (child == parent) continue;

            dfs(child, node);
            subtreeSize[node] += subtreeSize[child];
            subtreeSum[node] += subtreeSum[child];
        }
    }

    public int[] getSubtreeSizes() {
        return subtreeSize;
    }

    public long[] getSubtreeSums() {
        return subtreeSum;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
        }

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        solution.computeSubtreeMetrics(n, values, edges);

        long[] sums = solution.getSubtreeSums();
        for (int i = 1; i <= n; i++) {
            System.out.println(sums[i]);
        }

        sc.close();
    }
}
