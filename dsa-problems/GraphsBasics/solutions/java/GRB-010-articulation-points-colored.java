import java.util.*;

class Solution {
    public int[] criticalNodes(int n, int[][] edges) {
        // Build adjacency list
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        
        for (int[] e : edges) {
            adj.get(e[0]).add(new int[]{e[1], e[2]});
            adj.get(e[1]).add(new int[]{e[0], e[2]});
        }
        
        List<Integer> critical = new ArrayList<>();
        
        // Brute force: try removing each node
        for (int removed = 0; removed < n; removed++) {
            boolean[] visited = new boolean[n];
            visited[removed] = true;
            
            List<boolean[]> components = new ArrayList<>();
            
            for (int start = 0; start < n; start++) {
                if (!visited[start]) {
                    boolean hasRed = false;
                    boolean hasBlue = false;
                    
                    List<Integer> compNodes = new ArrayList<>();
                    Stack<Integer> stack = new Stack<>();
                    stack.push(start);
                    visited[start] = true;
                    
                    while (!stack.isEmpty()) {
                        int u = stack.pop();
                        compNodes.add(u);
                        for (int[] edge : adj.get(u)) {
                            int v = edge[0];
                            
                            if (v == removed) continue;
                            
                            if (!visited[v]) {
                                visited[v] = true;
                                stack.push(v);
                            }
                        }
                    }
                    
                    // Check edges within this component
                    Set<Integer> compSet = new HashSet<>(compNodes);
                    for (int u : compNodes) {
                        for (int[] edge : adj.get(u)) {
                            int v = edge[0];
                            int color = edge[1];
                            
                            if (compSet.contains(v) && v != removed) {
                                if (color == 0) hasRed = true;
                                else hasBlue = true;
                            }
                        }
                    }
                    
                    components.add(new boolean[]{hasRed, hasBlue});
                }
            }
            
            // Check if critical
            List<Integer> redComps = new ArrayList<>();
            List<Integer> blueComps = new ArrayList<>();
            
            for (int i = 0; i < components.size(); i++) {
                if (components.get(i)[0]) redComps.add(i);
                if (components.get(i)[1]) blueComps.add(i);
            }
            
            boolean isCritical = false;
            if (!redComps.isEmpty() && !blueComps.isEmpty()) {
                if (redComps.size() > 1 || blueComps.size() > 1) {
                    isCritical = true;
                } else if (!redComps.get(0).equals(blueComps.get(0))) {
                    isCritical = true;
                }
            }
            
            if (isCritical) {
                critical.add(removed);
            }
        }
        
        return critical.stream().mapToInt(i -> i).toArray();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            String color = sc.next();
            edges[i][2] = color.equals("R") ? 0 : 1;
        }
        
        Solution solution = new Solution();
        int[] result = solution.criticalNodes(n, edges);
        
        System.out.println(result.length);
        if (result.length > 0) {
            for (int i = 0; i < result.length; i++) {
                System.out.print(result[i]);
                if (i < result.length - 1) System.out.print(" ");
            }
            System.out.println();
        } else {
            System.out.println();
        }
        
        sc.close();
    }
}
