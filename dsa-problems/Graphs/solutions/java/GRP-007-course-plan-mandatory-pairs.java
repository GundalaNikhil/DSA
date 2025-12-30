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
        Queue<Integer> queue = new LinkedList<>();
        for (int node : inDegree.keySet()) {
            if (inDegree.get(node) == 0) {
                queue.offer(node);
            }
        }
        
        List<Integer> topoOrder = new ArrayList<>();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            topoOrder.add(node);
            
            for (int neighbor : contracted.get(node)) {
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
            for (int i = 0; i < n; i++) {
                if (find(i) == superNode) {
                    result.add(i);
                }
            }
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
