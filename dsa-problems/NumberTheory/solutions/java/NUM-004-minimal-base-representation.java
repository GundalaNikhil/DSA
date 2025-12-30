import java.util.*;

class Solution {
    private long getDigitSum(long x, int b) {
        long sum = 0;
        while (x > 0) {
            sum += x % b;
            x /= b;
        }
        return sum;
    }

    public long[] minimalBase(long x) {
        long minSum = Long.MAX_VALUE;
        long bestBase = 2;
        
        for (int b = 2; b <= 36; b++) {
            long currentSum = getDigitSum(x, b);
            if (currentSum < minSum) {
                minSum = currentSum;
                bestBase = b;
            }
        }
        
        return new long[]{bestBase, minSum};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long x = sc.nextLong();
            Solution solution = new Solution();
            long[] res = solution.minimalBase(x);
            System.out.println(res[0] + " " + res[1]);
        }
        sc.close();
    }
}
