import java.util.*;

class Solution {
    public double decayedDistinct(int T, double lambda, int[] times) {
        double sum = 0.0;
        for (int t : times) {
            sum += Math.exp(-lambda * (T - t));
        }
        return sum;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int T = sc.nextInt();
            double lambda = sc.nextDouble();
            int m = sc.nextInt();
            int[] times = new int[m];
            for (int i = 0; i < m; i++) times[i] = sc.nextInt();
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.decayedDistinct(T, lambda, times)));
        }
        sc.close();
    }
}
