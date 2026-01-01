import java.util.*;

class Solution {
    public int[] findOccurrences(String p, String t) {
        String s = p + "#" + t;
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        
        // Compute Z-array
        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        
        // Collect matches
        List<Integer> matches = new ArrayList<>();
        int pLen = p.length();
        for (int i = pLen + 1; i < n; i++) {
            if (z[i] == pLen) {
                matches.add(i - (pLen + 1));
            }
        }
        
        return matches.stream().mapToInt(i -> i).toArray();
    }
}

class Main {
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
