import java.util.*;

class Solution {
    public double expectedDraws(int N) {
        double harmonicSum = 0.0;
        for (int i = 1; i <= N; i++) {
            harmonicSum += 1.0 / i;
        }
        return N * harmonicSum;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int N = sc.nextInt();
            Solution solution = new Solution();
            System.out.printf("%.6f\n", solution.expectedDraws(N));
        }
        sc.close();
    }
}
