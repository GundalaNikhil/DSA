import java.util.*;

class Solution {
    public double jaccardEstimate(double[] a, double[] b) {
        int matches = 0;
        for (int i = 0; i < a.length; i++) {
            // Use Double.compare or epsilon for robustness, 
            // but problem implies exact hash values.
            if (Double.compare(a[i], b[i]) == 0) {
                matches++;
            }
        }
        return (double) matches / a.length;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            double[] a = new double[k];
            double[] b = new double[k];
            for (int i = 0; i < k; i++) a[i] = sc.nextDouble();
            for (int i = 0; i < k; i++) b[i] = sc.nextDouble();
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.jaccardEstimate(a, b)));
        }
        sc.close();
    }
}
