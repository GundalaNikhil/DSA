import java.util.*;

class Solution {
    public int[] lcpArray(String s, int[] sa) {
        int n = s.length();
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) {
            rank[sa[i]] = i;
        }
        
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
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (sc.hasNextInt()) {
                int n = sc.nextInt();
                int[] sa = new int[n];
                for (int i = 0; i < n; i++) sa[i] = sc.nextInt();
                
                Solution solution = new Solution();
                int[] lcp = solution.lcpArray(s, sa);
                
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < lcp.length; i++) {
                    if (i > 0) sb.append(' ');
                    sb.append(lcp[i]);
                }
                System.out.println(sb.toString());
            }
        }
        sc.close();
    }
}
