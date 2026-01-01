import java.util.*;

class Solution {
    public double[][] invert(double[][] A) {
        int n = A.length;
        double[][] B = new double[n][2 * n];
        for (int i = 0; i < n; i++) {
            System.arraycopy(A[i], 0, B[i], 0, n);
            B[i][n + i] = 1;
        }
        for (int i = 0; i < n; i++) {
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

    static class Result {
        double expectedSteps;
        double[] probs;
        Result(double e, double[] p) { expectedSteps = e; probs = p; }
    }

    public Result absorptionStats(double[][] P, int s) {
        int n = P.length;
        List<Integer> absorbing = new ArrayList<>();
        List<Integer> transientStates = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (Math.abs(P[i][i] - 1.0) < 1e-9) absorbing.add(i);
            else transientStates.add(i);
        }

        if (absorbing.contains(s)) {
            double[] probs = new double[absorbing.size()];
            for (int i = 0; i < absorbing.size(); i++) {
                probs[i] = (absorbing.get(i) == s) ? 1.0 : 0.0;
            }
            return new Result(0.0, probs);
        }

        int tSize = transientStates.size();
        int aSize = absorbing.size();
        double[][] Q = new double[tSize][tSize];
        double[][] R = new double[tSize][aSize];

        for (int i = 0; i < tSize; i++) {
            int u = transientStates.get(i);
            for (int j = 0; j < tSize; j++) Q[i][j] = P[u][transientStates.get(j)];
            for (int j = 0; j < aSize; j++) R[i][j] = P[u][absorbing.get(j)];
        }

        double[][] I_minus_Q = new double[tSize][tSize];
        for (int i = 0; i < tSize; i++) {
            for (int j = 0; j < tSize; j++) I_minus_Q[i][j] = (i == j ? 1.0 : 0.0) - Q[i][j];
        }

        double[][] N = invert(I_minus_Q);
        int sIdx = transientStates.indexOf(s);
        double expectedSteps = 0;
        for (int j = 0; j < tSize; j++) expectedSteps += N[sIdx][j];

        double[] probs = new double[aSize];
        for (int j = 0; j < aSize; j++) {
            for (int k = 0; k < tSize; k++) {
                probs[j] += N[sIdx][k] * R[k][j];
            }
        }
        return new Result(expectedSteps, probs);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            double[][] P = new double[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) P[i][j] = sc.nextDouble();
            }

            int numQueries = sc.nextInt();
            List<Integer> queryStates = new ArrayList<>();
            for (int i = 0; i < numQueries; i++) queryStates.add(sc.nextInt());

            int numAbsorbing = sc.nextInt();
            List<Integer> absorbingIndices = new ArrayList<>();
            for (int i = 0; i < numAbsorbing; i++) absorbingIndices.add(sc.nextInt());

            Solution sol = new Solution();
            
            // Reconstruct absorbing list used in logic to map indices
            List<Integer> funcAbsorbing = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (Math.abs(P[i][i] - 1.0) < 1e-9) funcAbsorbing.add(i);
            }

            List<String> finalProbs = new ArrayList<>();
            List<String> finalSteps = new ArrayList<>();

            for (int s : queryStates) {
                Solution.Result res = sol.absorptionStats(P, s);
                finalSteps.add(String.format("%.6f", res.expectedSteps));
                
                for (int aIdx : absorbingIndices) {
                    int pos = funcAbsorbing.indexOf(aIdx);
                    if (pos != -1) {
                        finalProbs.add(String.format("%.6f", res.probs[pos]));
                    }
                }
            }

            System.out.println(String.join(" ", finalProbs));
            System.out.println(String.join(" ", finalSteps));
        }
        sc.close();
    }
}
