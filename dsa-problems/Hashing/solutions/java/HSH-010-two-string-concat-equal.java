import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;

    public boolean checkConcatenationEqual(String a, String b, String c, String d) {
        if (a.length() + b.length() != c.length() + d.length()) {
            return false;
        }

        long hA = computeHash(a);
        long hB = computeHash(b);
        long hC = computeHash(c);
        long hD = computeHash(d);

        long combinedAB = combine(hA, hB, b.length());
        long combinedCD = combine(hC, hD, d.length());

        return combinedAB == combinedCD;
    }

    private long computeHash(String s) {
        long h = 0;
        for (char ch : s.toCharArray()) {
            h = (h * BASE + ch) % MOD;
        }
        return h;
    }

    private long combine(long h1, long h2, int len2) {
        long p = 1;
        long b = BASE;
        // Modular exponentiation for B^len2
        int exp = len2;
        while (exp > 0) {
            if ((exp & 1) == 1) p = (p * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }

        return (h1 * p + h2) % MOD;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String a = sc.nextLine();
            String b = sc.nextLine();
            String c = sc.nextLine();
            String d = sc.nextLine();

            Solution solution = new Solution();
            System.out.println(solution.checkConcatenationEqual(a, b, c, d));
        }
        sc.close();
    }
}
