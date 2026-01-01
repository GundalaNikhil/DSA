import java.util.*;

class Solution {
    int[][] st;
    int[] logs;
    int[] rank;
    int n;

    public int[] lcpQueries(String s, int[][] queries) {
        n = s.length();
        buildSA(s);
        int[] lcp = buildLCP(s);
        buildSparseTable(lcp);
        
        int[] ans = new int[queries.length];
        for (int k = 0; k < queries.length; k++) {
            int i = queries[k][0];
            int j = queries[k][1];
            if (i == j) {
                ans[k] = n - i;
            } else {
                int r1 = rank[i];
                int r2 = rank[j];
                if (r1 > r2) {
                    int temp = r1; r1 = r2; r2 = temp;
                }
                ans[k] = query(r1, r2 - 1);
            }
        }
        return ans;
    }

    int[] sa;
    
    void buildSA(String s) {
        Integer[] saObj = new Integer[n];
        rank = new int[n];
        int[] newRank = new int[n];
        
        for (int i = 0; i < n; i++) {
            saObj[i] = i;
            rank[i] = s.charAt(i);
        }
        
        for (int k = 1; k < n; k *= 2) {
            int len = k;
            Arrays.sort(saObj, (i, j) -> {
                if (rank[i] != rank[j]) return rank[i] - rank[j];
                int ri = (i + len < n) ? rank[i + len] : -1;
                int rj = (j + len < n) ? rank[j + len] : -1;
                return ri - rj;
            });
            
            newRank[saObj[0]] = 0;
            for (int i = 1; i < n; i++) {
                int prev = saObj[i - 1];
                int curr = saObj[i];
                int r1 = rank[prev];
                int r2 = (prev + len < n) ? rank[prev + len] : -1;
                int r3 = rank[curr];
                int r4 = (curr + len < n) ? rank[curr + len] : -1;
                
                if (r1 == r3 && r2 == r4) newRank[curr] = newRank[prev];
                else newRank[curr] = newRank[prev] + 1;
            }
            System.arraycopy(newRank, 0, rank, 0, n);
            if (rank[saObj[n - 1]] == n - 1) break;
        }
        sa = new int[n];
        for(int i=0; i<n; i++) sa[i] = saObj[i];
    }

    int[] buildLCP(String s) {
        int[] lcp = new int[n - 1];
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == n - 1) {
                k = 0;
                continue;
            }
            int j = sa[rank[i] + 1];
            while (i + k < n && j + k < n && s.charAt(i + k) == s.charAt(j + k)) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        return lcp;
    }

    void buildSparseTable(int[] arr) {
        int m = arr.length;
        if (m == 0) return;
        logs = new int[m + 1];
        for (int i = 2; i <= m; i++) logs[i] = logs[i / 2] + 1;
        
        int K = logs[m];
        st = new int[K + 1][m];
        for (int i = 0; i < m; i++) st[0][i] = arr[i];
        
        for (int k = 1; k <= K; k++) {
            for (int i = 0; i + (1 << k) <= m; i++) {
                st[k][i] = Math.min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
            }
        }
    }

    int query(int L, int R) {
        if (L > R) return 0;
        int j = logs[R - L + 1];
        return Math.min(st[j][L], st[j][R - (1 << j) + 1]);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        if (!sc.hasNextInt()) return;
        int q = sc.nextInt();
        int[][] queries = new int[q][2];
        for (int k = 0; k < q; k++) {
            queries[k][0] = sc.nextInt();
            queries[k][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] ans = solution.lcpQueries(s, queries);
        StringBuilder sb = new StringBuilder();
        for (int k = 0; k < ans.length; k++) {
            sb.append(ans[k]);
            if (k + 1 < ans.length) sb.append('\n');
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
