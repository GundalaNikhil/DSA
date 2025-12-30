import java.util.*;

class Solution {
    public double lshCandidateProb(int b, int r, double s) {
        double probBandMatch = Math.pow(s, r);
        double probAllBandsMismatch = Math.pow(1.0 - probBandMatch, b);
        return 1.0 - probAllBandsMismatch;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int b = sc.nextInt();
            int r = sc.nextInt();
            double s = sc.nextDouble();
    
            Solution solution = new Solution();
            System.out.println(String.format("%.6f", solution.lshCandidateProb(b, r, s)));
        }
        sc.close();
    }
}
