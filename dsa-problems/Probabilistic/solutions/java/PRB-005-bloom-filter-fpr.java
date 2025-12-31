import java.util.*;

class Solution {
    public double bloomFpr(double m, double k, double n) {
        // P = (1 - exp(-k * n / m))^k
        double exponent = -k * n / m;
        double term = 1.0 - Math.exp(exponent);
        return Math.pow(term, k);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextDouble()) {
            double m = sc.nextDouble();
            double k = sc.nextDouble();
            double n = sc.nextDouble();

            Solution solution = new Solution();
            System.out.printf("%.6f\n", solution.bloomFpr(m, k, n));
        }
        sc.close();
    }
}
