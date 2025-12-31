import java.util.*;

public class RerootingWeightedVariance {
    static class Edge {
        int to;
        Edge(int to) {
            this.to = to;
        }
    }

    static List<Edge>[] graph;
    static long[] weight;
    static long[] subtreeWeight;
    static long[] down;
    static long[] up;
    static long totalWeight;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        weight = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            weight[i] = sc.nextLong();
            totalWeight += weight[i];
        }

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(new Edge(v));
            graph[v].add(new Edge(u));
        }

        subtreeWeight = new long[n + 1];
        down = new long[n + 1];
        up = new long[n + 1];

        // Phase 1: Compute downward DP
        dfsDown(1, -1);

        // Phase 2: Compute upward DP (rerooting)
        dfsUp(1, -1, 0, 0);

        // Find minimum cost node
        long minCost = Long.MAX_VALUE;
        int bestNode = 1;

        for (int i = 1; i <= n; i++) {
            long totalCost = down[i] + up[i];
            if (totalCost < minCost) {
                minCost = totalCost;
                bestNode = i;
            }
        }

        System.out.println(bestNode);
        sc.close();
    }

    static void dfsDown(int u, int parent) {
        subtreeWeight[u] = weight[u];
        down[u] = 0;

        for (Edge e : graph[u]) {
            int v = e.to;
            if (v == parent) continue;

            dfsDown(v, u);

            // Add contribution of child's subtree
            // When moving down one level, distances increase by 1
            long childContribution = down[v] +
                                    2 * subtreeWeight[v] +
                                    subtreeWeight[v];
            down[u] += childContribution;
            subtreeWeight[u] += subtreeWeight[v];
        }
    }

    static void dfsUp(int u, int parent, long parentUp, long parentSubtreeWeight) {
        // Compute up[u] based on parent's info
        if (parent != -1) {
            // Total weight outside u's subtree when rooted at parent
            long outsideWeight = totalWeight - subtreeWeight[u];

            // Contribution from moving from parent to u
            long parentTotalDown = down[parent];
            long uContribution = down[u] + 2 * subtreeWeight[u] + subtreeWeight[u];
            long parentDownWithoutU = parentTotalDown - uContribution;

            up[u] = parentUp + parentDownWithoutU +
                   2 * outsideWeight + outsideWeight;
        }

        // Recur for children
        for (Edge e : graph[u]) {
            int v = e.to;
            if (v == parent) continue;

            dfsUp(v, u, up[u], subtreeWeight[u]);
        }
    }
}
