import java.util.*;

class Solution {
    static class LCG {
        long state;
        LCG(long seed) {
            this.state = seed & 0xFFFFFFFFL;
        }
        double nextFloat() {
            state = (state * 1664525 + 1013904223) & 0xFFFFFFFFL;
            return state / 4294967296.0;
        }
    }

    public double[] estimatePi(long N, long seed) {
        LCG rng = new LCG(seed);
        long countInside = 0;
        
        for (long i = 0; i < N; i++) {
            double x = rng.nextFloat();
            double y = rng.nextFloat();
            if (x * x + y * y <= 1.0) {
                countInside++;
            }
        }
        
        double pHat = (double) countInside / N;
        double piHat = 4.0 * pHat;
        
        double error = 0.0;
        if (N > 0) {
            double stdErrP = Math.sqrt(pHat * (1.0 - pHat) / N);
            error = 1.96 * stdErrP * 4.0;
        }
        
        return new double[]{piHat, error};
    }
}

class Main {
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
