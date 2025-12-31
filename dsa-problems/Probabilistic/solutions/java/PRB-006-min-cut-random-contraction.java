import java.util.*;

class Solution {
    public long minTrials(long n, double P) {
        if (n < 2) return 0; // Should not happen based on constraints
        
        double pSuccess = 2.0 / (n * (n - 1.0));
        
        // We want 1 - (1 - pSuccess)^t >= P
        // (1 - pSuccess)^t <= 1 - P
        // t * ln(1 - pSuccess) <= ln(1 - P)
        // t >= ln(1 - P) / ln(1 - pSuccess)
        
        double numerator = Math.log(1.0 - P);
        double denominator = Math.log(1.0 - pSuccess);
        
        return (long) Math.ceil(numerator / denominator);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            double P = sc.nextDouble();

            Solution solution = new Solution();
            System.out.println(solution.minTrials(n, P));
        }
        sc.close();
    }
}
