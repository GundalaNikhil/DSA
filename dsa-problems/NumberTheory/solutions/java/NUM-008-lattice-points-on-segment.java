import java.util.*;

class Solution {
    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public long latticePoints(long x1, long y1, long x2, long y2) {
        long dx = Math.abs(x1 - x2);
        long dy = Math.abs(y1 - y2);
        return gcd(dx, dy) + 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long x1 = sc.nextLong();
            long y1 = sc.nextLong();
            long x2 = sc.nextLong();
            long y2 = sc.nextLong();
            
            Solution solution = new Solution();
            System.out.println(solution.latticePoints(x1, y1, x2, y2));
        }
        sc.close();
    }
}
