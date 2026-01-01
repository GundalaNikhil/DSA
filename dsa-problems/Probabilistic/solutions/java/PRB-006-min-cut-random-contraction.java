import java.util.*;

class Solution {
    static class Edge {
        int u, v;
        Edge(int u, int v) { this.u = u; this.v = v; }
    }

    static class DSU {
        int[] parent;
        int components;

        DSU(int n) {
            parent = new int[n + 1];
            for (int i = 0; i <= n; i++) parent[i] = i;
            components = n;
        }

        int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }

        void unite(int i, int j) {
            int root_i = find(i);
            int root_j = find(j);
            if (root_i != root_j) {
                parent[root_i] = root_j;
                components--;
            }
        }
    }

    public int kargerMinCut(int n, List<Edge> edges, Random rng) {
        DSU dsu = new DSU(n);
        List<Edge> currentEdges = new ArrayList<>(edges);
        Collections.shuffle(currentEdges, rng);

        for (Edge edge : currentEdges) {
            if (dsu.components <= 2) break;
            dsu.unite(edge.u, edge.v);
        }

        int cutSize = 0;
        for (Edge edge : edges) {
            if (dsu.find(edge.u) != dsu.find(edge.v)) {
                cutSize++;
            }
        }
        return cutSize;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            List<Solution.Edge> edges = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                edges.add(new Solution.Edge(sc.nextInt(), sc.nextInt()));
            }

            int trials;
            if (n <= 20) trials = 100;
            else trials = (int) (n * n * 0.5);

            Solution sol = new Solution();
            Random rng = new Random(42); // Fixed seed for determinism
            
            int minCut = m + 1;
            for (int i = 0; i < trials; i++) {
                int cut = sol.kargerMinCut(n, edges, rng);
                if (cut < minCut) minCut = cut;
            }
            
            System.out.println(minCut);
        }
        sc.close();
    }
}
