import java.util.*;

class Solution {
    public Object[] bloomierStats(long m, int r) {
        long mem = m * r;
        double fpr = Math.pow(2.0, -r);
        return new Object[]{mem, fpr};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long m = sc.nextLong();
            int r = sc.nextInt();
    
            Solution solution = new Solution();
            Object[] res = solution.bloomierStats(m, r);
            System.out.println(res[0] + " " + String.format("%.6f", (double)res[1]));
        }
        sc.close();
    }
}
