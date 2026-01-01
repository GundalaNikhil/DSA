import java.util.*;

class Solution {
    public double largest_eigenvalue_power(int n, int maxIter, double[][] matrix, double epsilon) {
        double[] v = new double[n];
        Arrays.fill(v, 1.0); // Initial guess
        
        double lambda = 0.0;
        
        for (int iter = 0; iter < maxIter; iter++) {
            // w = A * v
            double[] w = new double[n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    w[i] += matrix[i][j] * v[j];
                }
            }
            
            // Rayleigh Quotient: num = v dot w, den = v dot v
            double num = 0.0;
            double den = 0.0;
            for (int i = 0; i < n; i++) {
                num += v[i] * w[i];
                den += v[i] * v[i];
            }
            
            double newLambda = (den == 0) ? 0 : num / den;
            
            if (Math.abs(newLambda - lambda) < epsilon) {
                return newLambda;
            }
            lambda = newLambda;
            
            // Normalize w
            double maxVal = 0.0;
            for (double val : w) maxVal = Math.max(maxVal, Math.abs(val));
            
            if (maxVal < 1e-9) break; // Zero vector
            
            for (int i = 0; i < n; i++) {
                v[i] = w[i] / maxVal;
            }
        }
        
        return lambda;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int maxIter = sc.nextInt();
        
        double[][] matrix = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextDouble();
            }
        }
        
        double epsilon = sc.nextDouble();
        
        Solution solution = new Solution();
        double res = solution.largest_eigenvalue_power(n, maxIter, matrix, epsilon);
        
        System.out.printf("%.6f\n", res);
        sc.close();
    }
}
