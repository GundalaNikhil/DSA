import java.util.*;

class Solution {
    static class Edge implements Comparable<Edge> {
        int u, v, cost;
        public Edge(int u, int v, int cost) {
            this.u = u;
            this.v = v;
            this.cost = cost;
        }
        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.cost, other.cost);
        }
    }

    static class DSU {
        int[] parent;
        public DSU(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        public int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        public boolean union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY) return false;
            parent[rootX] = rootY;
            return true;
        }
    }

    public long minCost(int n, int[] heights, int[][] existingCables) {
        DSU dsu = new DSU(n);
        int edgesCount = 0;
        
        // Process existing cables (cost 0)
        for (int[] cable : existingCables) {
            if (dsu.union(cable[0], cable[1])) {
                edgesCount++;
            }
        }
        
        // Prepare for sorting
        int[][] sortedBuildings = new int[n][2];
        for (int i = 0; i < n; i++) {
            sortedBuildings[i][0] = heights[i];
            sortedBuildings[i][1] = i; // Original index
        }
        
        Arrays.sort(sortedBuildings, (a, b) -> Integer.compare(a[0], b[0]));
        
        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < n - 1; i++) {
            int u = sortedBuildings[i][1];
            int v = sortedBuildings[i+1][1];
            int cost = sortedBuildings[i+1][0] - sortedBuildings[i][0];
            edges.add(new Edge(u, v, cost));
        }
        
        Collections.sort(edges);
        
        long totalCost = 0;
        for (Edge edge : edges) {
            if (dsu.union(edge.u, edge.v)) {
                totalCost += edge.cost;
                edgesCount++;
            }
        }
        
        return totalCost;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int[] heights = new int[n];
        for (int i = 0; i < n; i++) heights[i] = sc.nextInt();
        
        int m = sc.nextInt();
        int[][] existingCables = new int[m][2];
        for (int i = 0; i < m; i++) {
            existingCables[i][0] = sc.nextInt();
            existingCables[i][1] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.minCost(n, heights, existingCables));
        sc.close();
    }
}
