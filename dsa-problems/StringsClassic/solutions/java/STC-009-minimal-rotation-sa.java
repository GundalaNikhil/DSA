import java.util.*;

class Solution {
    public int minimalRotationIndex(String s) {
        int n = s.length();
        if (n == 0) return 0;
        String text = s + s;
        int m = text.length();
        
        // Build Suffix Array for s + s
        Integer[] sa = new Integer[m];
        int[] rank = new int[m];
        int[] newRank = new int[m];
        
        for (int i = 0; i < m; i++) {
            sa[i] = i;
            rank[i] = text.charAt(i);
        }
        
        for (int k = 1; k < m; k *= 2) {
            int len = k;
            Arrays.sort(sa, (i, j) -> {
                if (rank[i] != rank[j]) return rank[i] - rank[j];
                int ri = (i + len < m) ? rank[i + len] : -1;
                int rj = (j + len < m) ? rank[j + len] : -1;
                return ri - rj;
            });
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < m; i++) {
                int prev = sa[i - 1];
                int curr = sa[i];
                int r1 = rank[prev];
                int r2 = (prev + len < m) ? rank[prev + len] : -1;
                int r3 = rank[curr];
                int r4 = (curr + len < m) ? rank[curr + len] : -1;
                
                if (r1 == r3 && r2 == r4) newRank[curr] = newRank[prev];
                else newRank[curr] = newRank[prev] + 1;
            }
            System.arraycopy(newRank, 0, rank, 0, m);
            if (rank[sa[m - 1]] == m - 1) break;
        }
        
        // Find first index < n
        for (int i = 0; i < m; i++) {
            if (sa[i] < n) {
                return sa[i];
            }
        }
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.minimalRotationIndex(s));
        }
        sc.close();
    }
}
