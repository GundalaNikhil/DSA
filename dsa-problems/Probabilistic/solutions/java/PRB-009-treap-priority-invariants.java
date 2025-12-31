import java.util.*;

class Solution {
    public double[] treapExpectations(int n) {
        double H = 0.0;
        for (int i = 1; i <= n; i++) {
            H += 1.0 / i;
        }
        
        double eDepth = 2 * H - 2;
        // Note: For n=1, H=1, E_depth = 0. Correct.
        //         // If n=0? Loop doesn't run, H=0. E_depth = -2. 
        // Problem constraints n >= 1.
        
        double ePath = 2 * (n + 1) * H - 4 * n;
        
        return new double[]{eDepth, ePath};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution solution = new Solution();
            double[] res = solution.treapExpectations(n);
            System.out.printf("%.6f %.6f\n", res[0], res[1]);
        }
        sc.close();
    }
}
