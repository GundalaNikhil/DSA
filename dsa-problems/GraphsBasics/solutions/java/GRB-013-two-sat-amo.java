import java.util.*;

class Solution {
    private List<List<Integer>> adj;
    private List<List<Integer>> revAdj;
    private List<Integer> order;
    private boolean[] visited;
    private int[] component;
    private int numVars;

    public int[] solveTwoSat(int n, int[][] clauses, List<int[]> groups) {
        // Estimate total nodes needed including auxiliary
        // Base: 2*n nodes (1..n and n+1..2n for negations)
        // Aux: For each group of size k, we add k prefix variables.
        // Each prefix var has a negation. So 2*k aux nodes per group.
        
        int totalGroupSize = 0;
        for (int[] g : groups) totalGroupSize += g.length;
        
        int baseVars = n;
        int auxStart = n + 1;
        int totalVars = n + totalGroupSize;
        int totalNodes = 2 * totalVars + 2; // +2 for 1-based indexing safety
        
        adj = new ArrayList<>();
        revAdj = new ArrayList<>();
        for (int i = 0; i < totalNodes; i++) {
            adj.add(new ArrayList<>());
            revAdj.add(new ArrayList<>());
        }

        // Helper to get node index
        // x_i (1..n) -> i
        // ¬x_i -> i + totalVars
        // aux_j -> j
        // ¬aux_j -> j + totalVars
        int N = totalVars;
        
        // Add Clauses
        for (int[] clause : clauses) {
            addClause(clause[0], clause[1], N);
        }

        // Add AMO Constraints with Prefix Optimization
        int currentAux = auxStart;
        for (int[] group : groups) {
            int k = group.length;
            if (k <= 1) continue;
            
            // Prefix variables: currentAux ... currentAux + k - 1
            // P_i corresponds to variable group[i]
            
            for (int i = 0; i < k; i++) {
                int x = group[i]; // Literal index (could be negative? Problem says indices 1-based, usually positive for AMO)
                // Assuming AMO inputs are variable indices (positive).
                // If input can be literals, we handle sign.
                // Problem says "integer k followed by k variable indices". Indices usually mean x_i.
                
                int p = currentAux + i;
                
                // 1. x_i -> P_i
                addImplication(x, p, N);
                
                // 2. P_i -> P_{i+1}
                if (i < k - 1) {
                    addImplication(p, p + 1, N);
                }
                
                // 3. P_{i-1} -> ¬x_i
                if (i > 0) {
                    addImplication(p - 1, -x, N);
                }
            }
            currentAux += k;
        }

        // SCC (Kosaraju's)
        order = new ArrayList<>();
        visited = new boolean[totalNodes];
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) dfs1(i);
            if (!visited[i + N]) dfs1(i + N);
        }
        
        Collections.reverse(order);
        component = new int[totalNodes];
        Arrays.fill(component, -1);
        int compCount = 0;
        
        for (int u : order) {
            if (component[u] == -1) {
                dfs2(u, compCount++);
            }
        }

        // Check Satisfiability
        int[] result = new int[n];
        for (int i = 1; i <= n; i++) {
            if (component[i] == component[i + N]) return null;
            result[i - 1] = component[i] > component[i + N] ? 1 : 0;
        }
        
        return result;
    }

    private void addClause(int a, int b, int N) {
        // a OR b  <=>  ¬a -> b  AND  ¬b -> a
        addEdge(neg(a, N), map(b, N));
        addEdge(neg(b, N), map(a, N));
    }
    
    private void addImplication(int a, int b, int N) {
        // a -> b  <=>  ¬b -> ¬a
        addEdge(map(a, N), map(b, N));
        addEdge(neg(b, N), neg(a, N));
    }

    private void addEdge(int u, int v) {
        adj.get(u).add(v);
        revAdj.get(v).add(u);
    }

    private int map(int literal, int N) {
        if (literal > 0) return literal;
        return -literal + N;
    }

    private int neg(int literal, int N) {
        if (literal > 0) return literal + N;
        return -literal;
    }

    private void dfs1(int u) {
        visited[u] = true;
        for (int v : adj.get(u)) {
            if (!visited[v]) dfs1(v);
        }
        order.add(u);
    }

    private void dfs2(int u, int c) {
        component[u] = c;
        for (int v : revAdj.get(u)) {
            if (component[v] == -1) dfs2(v, c);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] clauses = new int[m][2];
        for (int i = 0; i < m; i++) {
            clauses[i][0] = sc.nextInt();
            clauses[i][1] = sc.nextInt();
        }
        int g = sc.nextInt();
        List<int[]> groups = new ArrayList<>();
        for (int i = 0; i < g; i++) {
            int k = sc.nextInt();
            int[] vars = new int[k];
            for (int j = 0; j < k; j++) vars[j] = sc.nextInt();
            groups.add(vars);
        }

        Solution solution = new Solution();
        int[] assign = solution.solveTwoSat(n, clauses, groups);
        if (assign == null) {
            System.out.print("UNSAT");
        } else {
            StringBuilder sb = new StringBuilder();
            sb.append("SAT\n");
            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(assign[i]);
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
