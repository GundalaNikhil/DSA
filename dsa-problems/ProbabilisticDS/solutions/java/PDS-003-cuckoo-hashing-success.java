import java.util.*;

class Solution {
    public double successProbability(long m, double alpha) {
        double val = 1.0 - alpha;
        double exponent = -(val * val * m) / 2.0;
        double pFail = Math.exp(exponent);
        return 1.0 - pFail;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long m = sc.nextLong();
            double alpha = sc.nextDouble();

            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.successProbability(m, alpha)));
        }
        sc.close();
    }
}
