import java.util.*;

class Solution {
    public Object[] xorFilterStats(long n, int b) {
        long cells = (long) Math.ceil(1.23 * n);
        long mem = cells * b;
        double fpr = Math.pow(2.0, -b);
        return new Object[]{mem, fpr};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            int b = sc.nextInt();
    
            Solution solution = new Solution();
            Object[] res = solution.xorFilterStats(n, b);
            System.out.println(res[0] + " " + String.format("%.6f", (double)res[1]));
        }
        sc.close();
    }
}
