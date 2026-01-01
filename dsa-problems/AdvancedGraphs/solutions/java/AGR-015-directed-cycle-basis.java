import java.util.*;

class Solution {
    public List<List<Integer>> cycleBasis(int n, int[][] edges) {
        int m = edges.length;
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            adj.get(edges[i][0]).add(new int[]{edges[i][1], i});
        }

        // Calc basis size
        int c = 0;
        boolean[] visited = new boolean[n];
        List<List<Integer>> undirAdj = new ArrayList<>();
        for (int i = 0; i < n; i++) undirAdj.add(new ArrayList<>());
        for (int[] e : edges) {
            undirAdj.get(e[0]).add(e[1]);
            undirAdj.get(e[1]).add(e[0]);
        }
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                c++;
                dfs(i, visited, undirAdj);
            }
        }
        int D = m - n + c;

        BitSet[] basis = new BitSet[m]; // basis[i] has pivot at i
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < m; i++) {
            if (result.size() == D) break;
            
            int u = edges[i][0];
            int v = edges[i][1];
            
            List<Integer> path = bfs(v, u, n, adj);
            if (path == null) continue;
            
            BitSet vec = new BitSet(m);
            vec.set(i);
            for (int eIdx : path) vec.set(eIdx);
            
            if (insert(basis, vec)) {
                List<Integer> cycle = new ArrayList<>();
                cycle.add(u);
                int curr = v;
                cycle.add(curr);
                for (int eIdx : path) {
                    curr = edges[eIdx][1];
                    cycle.add(curr);
                }
                result.add(cycle);
            }
        }
        return result;
    }
    
    private void dfs(int u, boolean[] visited, List<List<Integer>> adj) {
        visited[u] = true;
        for (int v : adj.get(u)) {
            if (!visited[v]) dfs(v, visited, adj);
        }
    }
    
    private List<Integer> bfs(int start, int target, int n, List<List<int[]>> adj) {
        if (start == target) return new ArrayList<>();
        int[] parentEdge = new int[n];
        int[] parentNode = new int[n];
        Arrays.fill(parentEdge, -1);
        Arrays.fill(parentNode, -1);
        
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        parentNode[start] = start;
        
        while (!q.isEmpty()) {
            int u = q.poll();
            if (u == target) break;
            for (int[] edge : adj.get(u)) {
                int v = edge[0];
                int idx = edge[1];
                if (parentNode[v] == -1) {
                    parentNode[v] = u;
                    parentEdge[v] = idx;
                    q.add(v);
                }
            }
        }
        
        if (parentNode[target] == -1) return null;
        
        List<Integer> path = new ArrayList<>();
        int curr = target;
        while (curr != start) {
            path.add(parentEdge[curr]);
            curr = parentNode[curr];
        }
        Collections.reverse(path);
        return path;
    }
    
    private boolean insert(BitSet[] basis, BitSet vec) {
        for (int i = vec.nextSetBit(0); i >= 0; i = vec.nextSetBit(i + 1)) {
            if (basis[i] == null) {
                basis[i] = (BitSet) vec.clone();
                return true;
            }
            vec.xor(basis[i]);
        }
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<List<Integer>> cycles = solution.cycleBasis(n, edges);
        StringBuilder sb = new StringBuilder();
        sb.append(cycles.size()).append('\n');
        for (List<Integer> cyc : cycles) {
            sb.append(cyc.size());
            for (int v : cyc) sb.append(' ').append(v);
            sb.append('\n');
        }
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
