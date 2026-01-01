import java.util.*;
import java.io.*;

class Main {
    static class Solution {
        public long solve(int[] xs, int[] ys) {
            int n = xs.length;
            if (n <= 1) return 0;
            
            // Prim's Algorithm for Dense Graph O(N^2)
            // Distances are Manhattan
            
            long[] minDist = new long[n];
            Arrays.fill(minDist, Long.MAX_VALUE);
            minDist[0] = 0;
            boolean[] visited = new boolean[n];
            long totalWeight = 0;
            
            for (int i = 0; i < n; i++) {
                int u = -1;
                for (int j = 0; j < n; j++) {
                    if (!visited[j] && (u == -1 || minDist[j] < minDist[u])) {
                        u = j;
                    }
                }
                
                if (minDist[u] == Long.MAX_VALUE) break;
                visited[u] = true;
                totalWeight += minDist[u];
                
                for (int v = 0; v < n; v++) {
                    if (!visited[v]) {
                        long d = Math.abs((long)xs[u] - xs[v]) + Math.abs((long)ys[u] - ys[v]);
                        if (d < minDist[v]) {
                            minDist[v] = d;
                        }
                    }
                }
            }
            return totalWeight;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        
        // Read all input at once logic or token by token
        // Use a robust tokenizer
        
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(" ");
        }
        st = new StringTokenizer(sb.toString());
        
        if (!st.hasMoreTokens()) return;
        
        int n = Integer.parseInt(st.nextToken());
        int[] xs = new int[n];
        int[] ys = new int[n];
        
        for (int i = 0; i < n; i++) {
            xs[i] = Integer.parseInt(st.nextToken());
            ys[i] = Integer.parseInt(st.nextToken());
        }
        
        Solution sol = new Solution();
        System.out.println(sol.solve(xs, ys));
    }
}
