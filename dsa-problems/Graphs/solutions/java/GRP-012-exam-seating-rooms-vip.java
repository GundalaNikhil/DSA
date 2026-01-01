import java.util.*;

class Solution {
    private int[] parent;
    private int[] size;

    private int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }

    private void union(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) {
            parent[rootI] = rootJ;
            size[rootJ] += size[rootI];
        }
    }

    public int maxComponentSize(int n, List<int[]> edges, Set<Integer> vips) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }

        // 1. Union all Non-VIP to Non-VIP edges
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            if (!vips.contains(u) && !vips.contains(v)) {
                union(u, v);
            }
        }

        // 2. Calculate max size for purely neutral components
        int maxComp = 0;
        for (int i = 0; i < n; i++) {
            if (!vips.contains(i) && parent[i] == i) {
                maxComp = Math.max(maxComp, size[i]);
            }
        }
        
        // If no VIPs, the answer is just the largest component
        if (vips.isEmpty()) return maxComp;

        // 3. For each VIP, sum up sizes of adjacent neutral components
        // Map VIP -> Set of adjacent neutral roots (Set to avoid double counting)
        Map<Integer, Set<Integer>> vipNeighbors = new HashMap<>();
        for (int vip : vips) vipNeighbors.put(vip, new HashSet<>());

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            boolean uVip = vips.contains(u);
            boolean vVip = vips.contains(v);

            if (uVip && !vVip) {
                vipNeighbors.get(u).add(find(v));
            } else if (!uVip && vVip) {
                vipNeighbors.get(v).add(find(u));
            }
        }

        for (int vip : vips) {
            int currentSize = 1; // The VIP itself
            for (int root : vipNeighbors.get(vip)) {
                currentSize += size[root];
            }
            maxComp = Math.max(maxComp, currentSize);
        }

        return maxComp;
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
            edges.add(new int[]{u, v});
        }
        
        Set<Integer> vips = new HashSet<>();
        if (sc.hasNextLine()) sc.nextLine(); // Consume newline
        if (sc.hasNextLine()) {
            String line = sc.nextLine();
            Scanner lineSc = new Scanner(line);
            while (lineSc.hasNextInt()) {
                vips.add(lineSc.nextInt());
            }
            lineSc.close();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.maxComponentSize(n, edges, vips));
        sc.close();
    }
}
