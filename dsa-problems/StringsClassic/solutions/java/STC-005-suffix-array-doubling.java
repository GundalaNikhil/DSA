import java.util.*;

class Solution {
    public int[] suffixArray(String s) {
        int n = s.length();
        Integer[] sa = new Integer[n];
        int[] rank = new int[n];
        int[] newRank = new int[n];
        
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s.charAt(i);
        }
        
        for (int k = 1; k < n; k *= 2) {
            int len = k;
            Arrays.sort(sa, (i, j) -> {
                if (rank[i] != rank[j]) {
                    return rank[i] - rank[j];
                }
                int ri = (i + len < n) ? rank[i + len] : -1;
                int rj = (j + len < n) ? rank[j + len] : -1;
                return ri - rj;
            });
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < n; i++) {
                int prev = sa[i - 1];
                int curr = sa[i];
                
                int r1 = rank[prev];
                int r2 = (prev + len < n) ? rank[prev + len] : -1;
                int r3 = rank[curr];
                int r4 = (curr + len < n) ? rank[curr + len] : -1;
                
                if (r1 == r3 && r2 == r4) {
                    newRank[curr] = newRank[prev];
                } else {
                    newRank[curr] = newRank[prev] + 1;
                }
            }
            System.arraycopy(newRank, 0, rank, 0, n);
            if (rank[sa[n - 1]] == n - 1) break;
        }
        
        return Arrays.stream(sa).mapToInt(Integer::intValue).toArray();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            int[] sa = solution.suffixArray(s);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < sa.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(sa[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
