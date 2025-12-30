import java.util.*;

class Solution {
    public double[] estimatePi(long N, long C) {
        double pHat = (double) C / N;
        double piHat = 4.0 * pHat;

        // Standard error of proportion p
        double stdErrP = Math.sqrt(pHat * (1.0 - pHat) / N);

        // 95% Confidence Interval half-width for Pi
        // Error for Pi is 4 * Error for p
        double error = 1.96 * stdErrP * 4.0;

        return new double[]{piHat, error};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long N = sc.nextLong();
            long C = sc.nextLong();

            Solution solution = new Solution();
            double[] res = solution.estimatePi(N, C);
            System.out.printf("%.6f %.6f\n", res[0], res[1]);
        }
        sc.close();
    }
}
