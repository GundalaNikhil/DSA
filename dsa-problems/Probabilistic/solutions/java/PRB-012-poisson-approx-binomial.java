import java.util.*;

class Solution {
    static class Result {
        double binomial;
        double approx;
        double error;
        Result(double b, double a, double e) { binomial = b; approx = a; error = e; }
    }

    private double logFactorial(int n) {
        double res = 0.0;
        for (int i = 1; i <= n; i++) res += Math.log(i);
        return res;
    }

    public Result solve(int n, double p, int k) {
        double lambda = n * p;

        // 1. Exact Binomial
        double binomialProb = 0.0;
        if (k <= n) {
            double logBinom = logFactorial(n) - logFactorial(k) - logFactorial(n - k);
            
            if (p > 0) logBinom += k * Math.log(p);
            else if (k > 0) logBinom = Double.NEGATIVE_INFINITY;

            if (p < 1) logBinom += (n - k) * Math.log(1.0 - p);
            else if (n - k > 0) logBinom = Double.NEGATIVE_INFINITY;

            if (logBinom > -1e14) binomialProb = Math.exp(logBinom);
        }

        // 2. Poisson Approx
        double approxProb = 0.0;
        if (lambda == 0) {
            approxProb = (k == 0) ? 1.0 : 0.0;
        } else {
            double logP = -lambda + k * Math.log(lambda) - logFactorial(k);
            if (logP > -1e14) approxProb = Math.exp(logP);
        }

        double error = Math.abs(binomialProb - approxProb);
        return new Result(binomialProb, approxProb, error);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            int n = (int) sc.nextLong();
            double p = sc.nextDouble();
            int k = (int) sc.nextLong();

            Solution solution = new Solution();
            Solution.Result res = solution.solve(n, p, k);
            
            // Output order: Approx Exact Error
            System.out.printf("%.9f %.9f %.9f\n", res.approx, res.binomial, res.error);
        }
        sc.close();
    }
}
