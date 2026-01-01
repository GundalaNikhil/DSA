import java.util.*;

class Solution {
    public double overflowProbability(int m, int k, int c, int n) {
        double lambda = (double) k * n / m;
        long maxVal = (1L << c) - 1;
        
        double term = Math.exp(-lambda);
        double sum = term;
        
        for (int i = 1; i <= maxVal; i++) {
            term *= (lambda / i);
            sum += term;
        }
        
        return 1.0 - sum;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int k = sc.nextInt();
            int c = sc.nextInt();
            int n = sc.nextInt();

            Solution solution = new Solution();
            System.out.println(String.format("%.15f", solution.overflowProbability(m, k, c, n)));
        }
        sc.close();
    }
}
