import java.util.*;

class Solution {
    private int[] parent;

    public List<Integer> courseSchedule(int n, List<int[]> prerequisites, List<int[]> pairs) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        // Union pairs
        for (int[] pair : pairs) {
            union(pair[0], pair[1]);
        }

        // Build contracted graph
        Map<Integer, List<Integer>> contracted = new HashMap<>();
        Map<Integer, Integer> inDegree = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int root = find(i);
            contracted.putIfAbsent(root, new ArrayList<>());
            inDegree.putIfAbsent(root, 0);
        }

        for (int[] pre : prerequisites) {
            int from = find(pre[0]);
            int to = find(pre[1]);
            if (from != to) {
                contracted.get(from).add(to);
                inDegree.put(to, inDegree.get(to) + 1);
            }
        }

        // Topological sort (Kahn's algorithm)
        List<Integer> sortedRoots = new ArrayList<>(inDegree.keySet());
        Collections.sort(sortedRoots);
        Queue<Integer> queue = new LinkedList<>();
        for (int node : sortedRoots) {
            if (inDegree.get(node) == 0) {
                queue.offer(node);
            }
        }

        List<Integer> topoOrder = new ArrayList<>();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            topoOrder.add(node);

            List<Integer> neighbors = new ArrayList<>(contracted.get(node));
            Collections.sort(neighbors);
            for (int neighbor : neighbors) {
                inDegree.put(neighbor, inDegree.get(neighbor) - 1);
                if (inDegree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        if (topoOrder.size() != contracted.size()) {
            return new ArrayList<>(); // Cycle detected
        }

        // Expand super-nodes
        List<Integer> result = new ArrayList<>();
        for (int superNode : topoOrder) {
            List<Integer> members = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (find(i) == superNode) {
                    members.add(i);
                }
            }
            Collections.sort(members);
            result.addAll(members);
        }

        return result;
    }

    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    private void union(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            parent[px] = py;
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<int[]> prerequisites = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            prerequisites.add(new int[]{u, v});
        }

        // Handle optional pairs input
        List<int[]> pairs = new ArrayList<>();
        if (sc.hasNextInt()) {
            int p = sc.nextInt();
            for (int i = 0; i < p; i++) {
                if (sc.hasNextInt()) {
                    int a = sc.nextInt();
                    if (sc.hasNextInt()) {
                        int b = sc.nextInt();
                        pairs.add(new int[]{a, b});
                    }
                }
            }
        }

        Solution solution = new Solution();
        List<Integer> result = solution.courseSchedule(n, prerequisites, pairs);

        if (result.isEmpty()) {
            System.out.println(-1);
        } else {
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i));
                if (i < result.size() - 1) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
