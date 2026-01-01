import java.util.*;

class Solution {
    private long power(long base, long exp, int mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }

    public long factorialMissingPrime(long n, int p) {
        if (p == 0) return 0; // Should not happen based on constraints
        
        long numBlocks = n / p;
        long remainder = n % p;
        
        // Contribution from full blocks: (-1)^numBlocks
        // -1 is equivalent to p-1
        long res = power(p - 1, numBlocks, p);
        
        // Contribution from remainder
        long remFact = 1;
        for (int i = 1; i <= remainder; i++) {
            remFact = (remFact * i) % p;
        }
        
        return (res * remFact) % p;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            int p = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.factorialMissingPrime(n, p));
        }
        sc.close();
    }
}
