import java.util.*;

class Solution {
    public int[] findOccurrences(String p, String t) {
        int m = p.length();
        int n = t.length();
        if (m == 0) return new int[0];
        
        // Step 1: Compute prefix function for p
        int[] pi = computePrefixFunction(p);
        
        List<Integer> matches = new ArrayList<>();
        int j = 0; // index for p
        
        // Step 2: Search p in t
        for (int i = 0; i < n; i++) {
            while (j > 0 && t.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (t.charAt(i) == p.charAt(j)) {
                j++;
            }
            if (j == m) {
                matches.add(i - m + 1);
                j = pi[j - 1]; // Prepare for next potential match
            }
        }
        
        return matches.stream().mapToInt(i -> i).toArray();
    }
    
    private int[] computePrefixFunction(String p) {
        int m = p.length();
        int[] pi = new int[m];
        int j = 0;
        for (int i = 1; i < m; i++) {
            while (j > 0 && p.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (p.charAt(i) == p.charAt(j)) {
                j++;
            }
            pi[i] = j;
        }
        return pi;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String p = sc.next();
            String t = sc.next();
            
            Solution solution = new Solution();
            int[] result = solution.findOccurrences(p, t);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
