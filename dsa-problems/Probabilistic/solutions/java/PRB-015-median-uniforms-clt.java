import java.util.*;

class Solution {
    public double[] medianClt(int n) {
        double mean = 0.5;
        double variance = 1.0 / (4.0 * n);
        return new double[]{mean, variance};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();

            Solution solution = new Solution();
            double[] res = solution.medianClt(n);
            System.out.printf("%.6f %.6f\n", res[0], res[1]);
        }
        sc.close();
    }
}
