import java.util.*;

class Solution {
    public long minimalProductSplit(long x) {
        String s = Long.toString(x);
        int n = s.length();
        long minProd = Long.MAX_VALUE;
        
        for (int i = 1; i < n; i++) {
            String part1 = s.substring(0, i);
            String part2 = s.substring(i);
            
            long a = Long.parseLong(part1);
            long b = Long.parseLong(part2);
            
            long prod = a * b;
            if (prod > 0) {
                minProd = Math.min(minProd, prod);
            }
        }
        
        return minProd;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long x = sc.nextLong();
            Solution solution = new Solution();
            System.out.println(solution.minimalProductSplit(x));
        }
        sc.close();
    }
}
