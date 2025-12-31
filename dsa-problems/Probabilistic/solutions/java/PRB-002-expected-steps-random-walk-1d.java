import java.util.*;

class Solution {
    public double expectedSteps(int a, int b, double p) {
        if (Math.abs(p - 0.5) < 1e-9) {
            return (double) a * b;
        }

        double q = 1.0 - p;
        double r = q / p;
        double M = a + b;
        double z = b;

        double term1 = z / (q - p);
        double term2 = (M / (q - p)) * ((1.0 - Math.pow(r, z)) / (1.0 - Math.pow(r, M)));

        return term1 - term2;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            double p = sc.nextDouble();
            Solution solution = new Solution();
            System.out.println(solution.expectedSteps(a, b, p));
        }
        sc.close();
    }
}
