import java.util.*;

class Solution {
    public double kmvEstimate(double[] hashes) {
        int k = hashes.length;
        if (k == 0) return 0.0;
        double hk = hashes[k-1];
        return (k - 1) / hk;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            double[] hashes = new double[k];
            for (int i = 0; i < k; i++) hashes[i] = sc.nextDouble();
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.kmvEstimate(hashes)));
        }
        sc.close();
    }
}
