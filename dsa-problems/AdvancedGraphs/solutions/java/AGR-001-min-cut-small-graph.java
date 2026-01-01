import java.util.*;

class Solution {
    public long minCut(int n, List<int[]> edges) {
        long[][] adj = new long[n][n];
        for (int[] e : edges) {
            adj[e[0]][e[1]] += e[2];
            adj[e[1]][e[0]] += e[2];
        }

        long globalMinCut = Long.MAX_VALUE;
        boolean[] merged = new boolean[n]; // Tracks if node is merged into another
        int nodesRemaining = n;

        while (nodesRemaining > 1) {
            // Minimum Cut Phase
            long[] weights = new long[n];
            boolean[] inSet = new boolean[n]; // In the growing set of the phase
            int prev = -1, curr = -1;

            // We need to add 'nodesRemaining' nodes to the set
            for (int step = 0; step < nodesRemaining; step++) {
                prev = curr;
                curr = -1;
                long maxWeight = -1;

                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        if (weights[i] > maxWeight) {
                            maxWeight = weights[i];
                            curr = i;
                        }
                    }
                }

                if (curr == -1) break; // Should not happen
                inSet[curr] = true;

                // Update weights of neighbors
                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        weights[i] += adj[curr][i];
                    }
                }
            }

            // The cut of the phase is the weight of the last added node 'curr'
            // 'weights[curr]' contains the sum of edges from 'curr' to the set (all other nodes)
            // At the end, weights[curr] is exactly the cut value of separating 'curr' from the rest.
            
            globalMinCut = Math.min(globalMinCut, weights[curr]);

            // Merge curr (t) into prev (s)
            for (int i = 0; i < n; i++) {
                if (i != curr && i != prev && !merged[i]) {
                    adj[prev][i] += adj[curr][i];
                    adj[i][prev] += adj[curr][i];
                }
            }
            merged[curr] = true;
            nodesRemaining--;
        }

        return globalMinCut == Long.MAX_VALUE ? 0 : globalMinCut;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            edges.add(new int[]{u, v, w});
        }

        Solution solution = new Solution();
        System.out.println(solution.minCut(n, edges));
        sc.close();
    }
}
