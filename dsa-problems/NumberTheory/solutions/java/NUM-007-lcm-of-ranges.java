import java.util.*;

class Solution {
    public long lcmRange(int[] a, int l, int r, long MOD) {
        Map<Integer, Integer> maxExponents = new HashMap<>();
        
        for (int i = l; i <= r; i++) {
            int num = a[i];
            for (int p = 2; p * p <= num; p++) {
                if (num % p == 0) {
                    int count = 0;
                    while (num % p == 0) {
                        num /= p;
                        count++;
                    }
                    maxExponents.put(p, Math.max(maxExponents.getOrDefault(p, 0), count));
                }
            }
            if (num > 1) {
                maxExponents.put(num, Math.max(maxExponents.getOrDefault(num, 0), 1));
            }
        }
        
        long ans = 1;
        for (Map.Entry<Integer, Integer> entry : maxExponents.entrySet()) {
            int p = entry.getKey();
            int e = entry.getValue();
            long term = power(p, e, MOD);
            ans = (ans * term) % MOD;
        }
        return ans;
    }
    
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
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long MOD = sc.nextLong();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();

            Solution solution = new Solution();
            for (int i = 0; i < q; i++) {
                int l = sc.nextInt();
                int r = sc.nextInt();
                System.out.println(solution.lcmRange(a, l, r, MOD));
            }
        }
        sc.close();
    }
}
