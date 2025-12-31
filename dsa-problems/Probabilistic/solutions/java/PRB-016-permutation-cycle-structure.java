import java.util.*;

class Solution {
    public double[] cycleExpectations(int n, int k) {
        double expectedCyclesK = 1.0 / k;
        double expectedLongest = n * 0.624330;
        return new double[]{expectedCyclesK, expectedLongest};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();

            Solution solution = new Solution();
            double[] res = solution.cycleExpectations(n, k);
            System.out.printf("%.6f %.6f\n", res[0], res[1]);
        }
        sc.close();
    }
}
