import java.util.*;

class Solution {
    public long[] cmsParams(double epsilon, double delta) {
        long w = (long) Math.ceil(Math.E / epsilon);
        long d = (long) Math.ceil(Math.log(1.0 / delta));
        return new long[]{w, d};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextDouble()) {
            double epsilon = sc.nextDouble();
            double delta = sc.nextDouble();

            Solution solution = new Solution();
            long[] res = solution.cmsParams(epsilon, delta);
            System.out.println(res[0] + " " + res[1]);
        }
        sc.close();
    }
}
