import java.util.*;

class Solution {
    public Object[] designBloom(long n, double f) {
        double ln2 = Math.log(2);
        
        // Calculate m
        double mDouble = -(n * Math.log(f)) / (ln2 * ln2);
        long m = (long) Math.ceil(mDouble);
        
        // Calculate k
        double kDouble = (m / (double)n) * ln2;
        long k = Math.round(kDouble);
        
        // Calculate actual FPR
        double exponent = -((double)k * n) / m;
        double fpr = Math.pow(1 - Math.exp(exponent), k);
        
        return new Object[]{m, k, fpr};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            double f = sc.nextDouble();

            Solution solution = new Solution();
            Object[] res = solution.designBloom(n, f);
            System.out.println(res[0] + " " + res[1] + " " + String.format("%.6f", (double)res[2]));
        }
        sc.close();
    }
}
