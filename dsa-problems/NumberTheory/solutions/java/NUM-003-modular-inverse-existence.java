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

    public boolean hasInverse(long a, long m) {
        return gcd(a, m) == 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            Solution solution = new Solution();
            for (int i = 0; i < q; i++) {
                long a = sc.nextLong();
                long m = sc.nextLong();
                System.out.println(solution.hasInverse(a, m) ? "true" : "false");
            }
        }
        sc.close();
    }
}
