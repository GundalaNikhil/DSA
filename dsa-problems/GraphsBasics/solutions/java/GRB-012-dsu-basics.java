import java.util.*;

class Solution {
    class DSU {
        int[] parent;
        int[] rank;

        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        int find(int i) {
            if (parent[i] != i) {
                parent[i] = find(parent[i]); // Path compression
            }
            return parent[i];
        }

        void union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);

            if (rootI != rootJ) {
                // Union by rank
                if (rank[rootI] < rank[rootJ]) {
                    parent[rootI] = rootJ;
                } else if (rank[rootI] > rank[rootJ]) {
                    parent[rootJ] = rootI;
                } else {
                    parent[rootI] = rootJ;
                    rank[rootJ]++;
                }
            }
        }
    }

    public List<Boolean> processQueries(int n, String[] type, int[] u, int[] v) {
        DSU dsu = new DSU(n);
        List<Boolean> results = new ArrayList<>();

        for (int i = 0; i < type.length; i++) {
            if (type[i].equals("union")) {
                dsu.union(u[i], v[i]);
            } else {
                results.add(dsu.find(u[i]) == dsu.find(v[i]));
            }
        }
        return results;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int q = sc.nextInt();
        String[] type = new String[q];
        int[] u = new int[q];
        int[] v = new int[q];
        for (int i = 0; i < q; i++) {
            type[i] = sc.next();
            u[i] = sc.nextInt();
            v[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<Boolean> ans = solution.processQueries(n, type, u, v);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            sb.append(ans.get(i) ? "true" : "false");
            if (i + 1 < ans.size()) sb.append('\n');
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
