import java.util.*;

class Solution {
    public int[] components(int n, List<List<Integer>> adj) {
        int[] comp = new int[n];
        int count = 0;
        int[] stack = new int[n];

        for (int i = 0; i < n; i++) {
            if (comp[i] != 0) continue;
            count++;
            int top = 0;
            stack[top++] = i;
            comp[i] = count;
            while (top > 0) {
                int u = stack[--top];
                for (int v : adj.get(u)) {
                    if (comp[v] == 0) {
                        comp[v] = count;
                        stack[top++] = v;
                    }
                }
            }
        }
        return comp;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        Solution solution = new Solution();
        int[] comp = solution.components(n, adj);
        int maxComp = 0;
        for (int id : comp) maxComp = Math.max(maxComp, id);

        System.out.println(maxComp);
        sc.close();
    }
}
