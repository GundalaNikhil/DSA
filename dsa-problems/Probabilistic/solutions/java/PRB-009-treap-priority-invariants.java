import java.util.*;

class Solution {
    public double solve(int n) {
        double h = 0.0;
        for (int i = 1; i <= n; i++) {
            h += 1.0 / i;
        }
        return h;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution solution = new Solution();
            System.out.printf("%.6f\n", solution.solve(n));
        }
        sc.close();
    }
}
