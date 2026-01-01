import java.util.*;

class Solution {
    public long[] buildPrefixDistinct(int N) {
        int[] f = new int[N + 1];
        
        // Modified Sieve
        for (int i = 2; i <= N; i++) {
            if (f[i] == 0) { // i is prime
                for (int j = i; j <= N; j += i) {
                    f[j]++;
                }
            }
        }
        
        long[] pref = new long[N + 1];
        for (int i = 1; i <= N; i++) {
            pref[i] = pref[i - 1] + f[i];
        }
        
        return pref;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int N = sc.nextInt();
            int q = sc.nextInt();

            Solution solution = new Solution();
            long[] pref = solution.buildPrefixDistinct(N);

            for (int i = 0; i < q; i++) {
                int l = sc.nextInt();
                int r = sc.nextInt();
                System.out.println(pref[r] - pref[l - 1]);
            }
        }
        sc.close();
    }
}
