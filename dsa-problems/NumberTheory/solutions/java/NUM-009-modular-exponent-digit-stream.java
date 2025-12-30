import java.util.*;
import java.math.BigInteger;

class Solution {
    private long power(long base, long exp, long mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }

    public long modExpStream(long a, long m, String e) {
        long ans = 1; // Represents a^0
        
        for (char c : e.toCharArray()) {
            int d = c - '0';
            // ans = ans^10 * a^d
            ans = power(ans, 10, m);
            long term = power(a, d, m);
            ans = (ans * term) % m;
        }
        
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long a = sc.nextLong();
            long m = sc.nextLong();
            String e = sc.next();
            
            Solution solution = new Solution();
            System.out.println(solution.modExpStream(a, m, e));
        }
        sc.close();
    }
}
