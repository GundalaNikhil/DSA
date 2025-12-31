import java.util.*;

class Solution {
    public double[] poissonApprox(int n, double p, int k) {
        double lambda = n * p;
        
        // Use log-space calculations to avoid overflow
        // ln(P) = -lambda + k * ln(lambda) - ln(k!)
        
        double logP = -lambda;
        if (k > 0 && lambda > 0) {
            logP += k * Math.log(lambda);
        } else if (k == 0) {
            // logP is just -lambda
        } else {
            // k > 0 but lambda = 0 -> Probability is 0 (log is -inf)
            logP = Double.NEGATIVE_INFINITY;
        }
        
        // Subtract ln(k!)
        for (int i = 1; i <= k; i++) {
            logP -= Math.log(i);
        }
        
        double pApprox = Math.exp(logP);
        
        // Handle edge case where lambda=0 and k=0 -> P=1
        if (lambda == 0 && k == 0) pApprox = 1.0;
        
        double err = Math.min(1.0, 2.0 * n * p * p);
        
        return new double[]{pApprox, err};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            double p = sc.nextDouble();
            int k = sc.nextInt();

            Solution solution = new Solution();
            double[] res = solution.poissonApprox(n, p, k);
            System.out.printf("%.6f %.6f\n", res[0], res[1]);
        }
        sc.close();
    }
}
