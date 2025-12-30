import java.util.*;

class Solution {
    static class Edge {
        int to;
        int weight;
        Edge(int to, int weight) { this.to = to; this.weight = weight; }
    }

    static class Path implements Comparable<Path> {
        List<Integer> nodes;
        long cost;

        Path(List<Integer> nodes, long cost) {
            this.nodes = new ArrayList<>(nodes);
            this.cost = cost;
        }

        @Override
        public int compareTo(Path other) {
            return Long.compare(this.cost, other.cost);
        }
    }

    public long[] kShortestPaths(int n, List<List<int[]>> adjList, int s, int t, int k) {
        // Convert to easier format
        List<List<Edge>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int u = 0; u < n; u++) {
            for (int[] e : adjList.get(u)) {
                adj.get(u).add(new Edge(e[0], e[1]));
            }
        }

        List<Path> A = new ArrayList<>();
        PriorityQueue<Path> B = new PriorityQueue<>();

        // 1. First shortest path
        Path p0 = getShortestPath(n, adj, s, t, new HashSet<>(), new HashSet<>());
        if (p0 == null) return new long[0];
        A.add(p0);

        // 2. Find k-1 more
        for (int i = 1; i < k; i++) {
            Path prevPath = A.get(i - 1);
            
            // Spur node ranges from first node to second-to-last node
            for (int j = 0; j < prevPath.nodes.size() - 1; j++) {
                int spurNode = prevPath.nodes.get(j);
                List<Integer> rootPathNodes = prevPath.nodes.subList(0, j + 1);
                long rootPathCost = 0;
                // Calculate root path cost (could optimize)
                // We assume prevPath is valid, so we can just sum edges? 
                // Better: store costs in Path or recompute. Recomputing is safer.
                
                // Constraints
                Set<Integer> forbiddenNodes = new HashSet<>(rootPathNodes);
                forbiddenNodes.remove(spurNode); // Spur node is allowed as start
                
                Set<String> forbiddenEdges = new HashSet<>();
                for (Path p : A) {
                    if (p.nodes.size() > j && p.nodes.subList(0, j + 1).equals(rootPathNodes)) {
                        int u = p.nodes.get(j);
                        int v = p.nodes.get(j + 1);
                        forbiddenEdges.add(u + "," + v);
                    }
                }

                Path spurPath = getShortestPath(n, adj, spurNode, t, forbiddenNodes, forbiddenEdges);
                
                if (spurPath != null) {
                    List<Integer> totalNodes = new ArrayList<>(rootPathNodes);
                    totalNodes.remove(totalNodes.size() - 1); // Remove duplicate spurNode
                    totalNodes.addAll(spurPath.nodes);
                    
                    // Calculate total cost
                    // We need exact cost. getShortestPath returns cost of spur part.
                    // We need cost of root part.
                    long currentRootCost = 0;
                    for(int x=0; x<j; x++) {
                        int u = prevPath.nodes.get(x);
                        int v = prevPath.nodes.get(x+1);
                        for(Edge e : adj.get(u)) if(e.to == v) { currentRootCost += e.weight; break; }
                    }
                    
                    Path totalPath = new Path(totalNodes, currentRootCost + spurPath.cost);
                    
                    // Avoid duplicates in B
                    boolean exists = false;
                    for(Path p : B) {
                        if (p.nodes.equals(totalPath.nodes)) { exists = true; break; }
                    }
                    if (!exists) B.add(totalPath);
                }
            }

            if (B.isEmpty()) break;
            A.add(B.poll());
        }

        long[] result = new long[A.size()];
        for (int i = 0; i < A.size(); i++) result[i] = A.get(i).cost;
        return result;
    }

    private Path getShortestPath(int n, List<List<Edge>> adj, int s, int t, 
                                 Set<Integer> forbiddenNodes, Set<String> forbiddenEdges) {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        dist[s] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.add(new long[]{0, s});

        while (!pq.isEmpty()) {
            long[] top = pq.poll();
            long d = top[0];
            int u = (int) top[1];

            if (d > dist[u]) continue;
            if (u == t) break;

            for (Edge e : adj.get(u)) {
                if (forbiddenNodes.contains(e.to)) continue;
                if (forbiddenEdges.contains(u + "," + e.to)) continue;

                if (dist[u] + e.weight < dist[e.to]) {
                    dist[e.to] = dist[u] + e.weight;
                    parent[e.to] = u;
                    pq.add(new long[]{dist[e.to], e.to});
                }
            }
        }

        if (dist[t] == Long.MAX_VALUE) return null;

        List<Integer> nodes = new ArrayList<>();
        int curr = t;
        while (curr != -1) {
            nodes.add(curr);
            curr = parent[curr];
        }
        Collections.reverse(nodes);
        return new Path(nodes, dist[t]);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        int k = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        Solution solution = new Solution();
        long[] paths = solution.kShortestPaths(n, adj, s, t, k);
        StringBuilder sb = new StringBuilder();
        sb.append(paths.length).append('\n');
        for (int i = 0; i < paths.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(paths[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
