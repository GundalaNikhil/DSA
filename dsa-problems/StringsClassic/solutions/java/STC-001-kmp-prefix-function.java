import java.util.*;

class Solution {
    public int[] prefixFunction(String s) {
        int n = s.length();
        int[] pi = new int[n];
        // j is the length of the previous longest prefix
        int j = 0; 
        
        for (int i = 1; i < n; i++) {
            // While we cannot extend the current prefix length j,
            // we backtrack to the next best candidate length.
            while (j > 0 && s.charAt(i) != s.charAt(j)) {
                j = pi[j - 1];
            }
            // If characters match, we extend the prefix length
            if (s.charAt(i) == s.charAt(j)) {
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
            String s = sc.next();
            Solution solution = new Solution();
            int[] pi = solution.prefixFunction(s);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < pi.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(pi[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
