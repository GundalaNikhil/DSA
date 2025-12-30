import java.util.*;

class Solution {
    public String turningTurtles(int n, int k, String s) {
        long xorSum = 0;
        long mod = k + 1;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'H') {
                xorSum ^= ((i % mod) + 1);
            }
        }
        return xorSum > 0 ? "First" : "Second";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            String s = sc.next();

            Solution solution = new Solution();
            System.out.println(solution.turningTurtles(n, k, s));
        }
        sc.close();
    }
}
