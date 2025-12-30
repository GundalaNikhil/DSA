import java.util.*;

class Solution {
    public double expectedHeight(int n, double p) {
        // H = log_{1/p}(n) = ln(n) / ln(1/p)
        return Math.log(n) / Math.log(1.0 / p);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            double p = sc.nextDouble();

            Solution solution = new Solution();
            System.out.println(solution.expectedHeight(n, p));
        }
        sc.close();
    }
}
