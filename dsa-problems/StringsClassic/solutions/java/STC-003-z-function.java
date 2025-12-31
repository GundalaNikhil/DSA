import java.util.*;

class Solution {
    public int[] zFunction(String s) {
        int n = s.length();
        int[] z = new int[n];
        if (n == 0) return z;
        z[0] = n;
        
        int l = 0, r = 0;
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
        return z;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            int[] z = solution.zFunction(s);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < z.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(z[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
