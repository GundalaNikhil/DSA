import java.util.*;

class Solution {
    public long[] processTemperatureQueries(int[] temps, List<Main.Query> queries) {
        int n = temps.length;
        long[] diff = new long[n + 1];
        List<Main.Query> sumQueries = new ArrayList<>();

        // 1. Process Updates
        for (Main.Query q : queries) {
            if ("add".equals(q.type)) {
                diff[q.l] += q.x;
                if (q.r + 1 < n + 1) {
                    diff[q.r + 1] -= q.x;
                }
            } else {
                sumQueries.add(q);
            }
        }

        // 2. Reconstruct & Build Prefix Sums
        // P[i] stores sum of final_temps[0...i-1]
        long[] P = new long[n + 1];
        long currentAdd = 0;
        
        for (int i = 0; i < n; i++) {
            currentAdd += diff[i];
            long finalVal = temps[i] + currentAdd;
            P[i + 1] = P[i] + finalVal;
        }

        // 3. Answer Sum Queries
        long[] results = new long[sumQueries.size()];
        for (int i = 0; i < sumQueries.size(); i++) {
            Main.Query q = sumQueries.get(i);
            results[i] = P[q.r + 1] - P[q.l];
        }

        return results;
    }
}

public class Main {
    static class Query {
        String type;
        int l, r, x;
        Query(String type, int l, int r, int x) {
            this.type = type;
            this.l = l; this.r = r; this.x = x;
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] temps = new int[n];
        for (int i = 0; i < n; i++) temps[i] = sc.nextInt();
        
        int q = sc.nextInt();
        List<Query> queries = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            String type = sc.next();
            if ("add".equals(type)) {
                queries.add(new Query(type, sc.nextInt(), sc.nextInt(), sc.nextInt()));
            } else {
                queries.add(new Query(type, sc.nextInt(), sc.nextInt(), 0));
            }
        }

        Solution solution = new Solution();
        long[] result = solution.processTemperatureQueries(temps, queries);
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]).append(i == result.length - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
