import java.util.*;

class Solution {
    public long minTrials(long n, double C) {
        // p is probability of detection per trial
        double p = 1.0 / (n * n);
        
        // We want 1 - (1-p)^t >= C
        // (1-p)^t <= 1 - C
        // t * ln(1-p) <= ln(1-C)
        // t >= ln(1-C) / ln(1-p)  (since ln(1-p) is negative)
        
        double num = Math.log(1.0 - C);
        double den = Math.log(1.0 - p);
        
        return (long) Math.ceil(num / den);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            double C = sc.nextDouble();

            Solution solution = new Solution();
            System.out.println(solution.minTrials(n, C));
        }
        sc.close();
    }
}
