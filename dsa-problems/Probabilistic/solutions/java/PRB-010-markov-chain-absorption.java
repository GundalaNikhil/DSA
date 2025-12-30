import java.util.*;

class Solution {
    // Gaussian elimination to invert matrix
    public double[][] invert(double[][] A) {
        int n = A.length;
        double[][] B = new double[n][2 * n];

        // Augment with Identity
        for (int i = 0; i < n; i++) {
            System.arraycopy(A[i], 0, B[i], 0, n);
            B[i][n + i] = 1;
        }

        for (int i = 0; i < n; i++) {
            // Pivot
            int pivot = i;
            for (int j = i + 1; j < n; j++) {
                if (Math.abs(B[j][i]) > Math.abs(B[pivot][i])) pivot = j;
            }
            double[] temp = B[i]; B[i] = B[pivot]; B[pivot] = temp;

            double div = B[i][i];
            for (int j = i; j < 2 * n; j++) B[i][j] /= div;

            for (int k = 0; k < n; k++) {
                if (k != i) {
                    double factor = B[k][i];
                    for (int j = i; j < 2 * n; j++) B[k][j] -= factor * B[i][j];
                }
            }
        }

        double[][] res = new double[n][n];
        for (int i = 0; i < n; i++) {
            System.arraycopy(B[i], n, res[i], 0, n);
        }
        return res;
    }

    public double[] absorptionStats(double[][] P, int s) {
        int n = P.length;
        List<Integer> absorbing = new ArrayList<>();
        List<Integer> transientStates = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            boolean isAbsorbing = true;
            for (int j = 0; j < n; j++) {
                if (i != j && P[i][j] > 0) {
                    isAbsorbing = false;
                    break;
                }
            }
            // Or simpler: P[i][i] == 1.0 (assuming rows sum to 1)
            if (Math.abs(P[i][i] - 1.0) < 1e-9) isAbsorbing = true;

            if (isAbsorbing) absorbing.add(i);
            else transientStates.add(i);
        }

        // Base case: Start is absorbing
        if (absorbing.contains(s)) {
            double[] res = new double[1 + absorbing.size()];
            res[0] = 0.0;
            for (int i = 0; i < absorbing.size(); i++) {
                res[i + 1] = (absorbing.get(i) == s) ? 1.0 : 0.0;
            }
            return res;
        }

        int tSize = transientStates.size();
        int aSize = absorbing.size();

        double[][] Q = new double[tSize][tSize];
        double[][] R = new double[tSize][aSize];

        for (int i = 0; i < tSize; i++) {
            int u = transientStates.get(i);
            for (int j = 0; j < tSize; j++) {
                int v = transientStates.get(j);
                Q[i][j] = P[u][v];
            }
            for (int j = 0; j < aSize; j++) {
                int v = absorbing.get(j);
                R[i][j] = P[u][v];
            }
        }

        // I - Q
        double[][] I_minus_Q = new double[tSize][tSize];
        for (int i = 0; i < tSize; i++) {
            for (int j = 0; j < tSize; j++) {
                I_minus_Q[i][j] = (i == j ? 1.0 : 0.0) - Q[i][j];
            }
        }

        double[][] N = invert(I_minus_Q);

        // Find index of s in transient list
        int sIdx = transientStates.indexOf(s);

        // Expected steps: Sum of row sIdx in N
        double expectedSteps = 0;
        for (int j = 0; j < tSize; j++) expectedSteps += N[sIdx][j];

        // Absorption probs: Row sIdx of N * R
        double[] probs = new double[aSize];
        for (int j = 0; j < aSize; j++) {
            for (int k = 0; k < tSize; k++) {
                probs[j] += N[sIdx][k] * R[k][j];
            }
        }

        double[] result = new double[1 + aSize];
        result[0] = expectedSteps;
        System.arraycopy(probs, 0, result, 1, aSize);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int s = sc.nextInt();
            double[][] P = new double[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    P[i][j] = sc.nextDouble();
                }
            }

            Solution solution = new Solution();
            double[] res = solution.absorptionStats(P, s);
            if (res.length > 0) {
                System.out.printf("%.6f\n", res[0]);
                for (int i = 1; i < res.length; i++) {
                    System.out.printf("%.6f", res[i]);
                    if (i + 1 < res.length) System.out.print(" ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
