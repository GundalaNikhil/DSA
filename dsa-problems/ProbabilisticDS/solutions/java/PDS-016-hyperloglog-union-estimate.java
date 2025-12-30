import java.util.*;

class Solution {
    public double hllUnionEstimate(int m, int[] a, int[] b) {
        double alpha;
        if (m == 16) alpha = 0.673;
        else if (m == 32) alpha = 0.697;
        else if (m == 64) alpha = 0.709;
        else alpha = 0.7213 / (1.0 + 1.079 / m);
        
        double sum = 0.0;
        for (int i = 0; i < m; i++) {
            int val = Math.max(a[i], b[i]);
            sum += Math.pow(2.0, -val);
        }
        
        return alpha * m * m / sum;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int[] a = new int[m];
            int[] b = new int[m];
            for (int i = 0; i < m; i++) a[i] = sc.nextInt();
            for (int i = 0; i < m; i++) b[i] = sc.nextInt();
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.hllUnionEstimate(m, a, b)));
        }
        sc.close();
    }
}
