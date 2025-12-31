import java.util.*;

class Solution {
    private int[] memo;
    private int n;
    private int[] a;

    private int solve(int mask) {
        if (mask == (1 << n) - 1) return 0;
        if (memo[mask] != -1) return memo[mask];

        int res = Integer.MAX_VALUE;
        
        // Find the first unset element
        int i = 0;
        while (((mask >> i) & 1) == 1) {
            i++;
        }
        
        // Try pairing i with every other unset element j
        for (int j = i + 1; j < n; j++) {
            if (((mask >> j) & 1) == 0) {
                int pairXor = a[i] ^ a[j];
                // Recurse for the rest
                int subRes = solve(mask | (1 << i) | (1 << j));
                res = Math.min(res, Math.max(pairXor, subRes));
            }
        }
        
        return memo[mask] = res;
    }

    public int minimizeMaxPairXor(int[] a) {
        this.n = a.length;
        this.a = a;
        this.memo = new int[1 << n];
        Arrays.fill(memo, -1);
        return solve(0);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.minimizeMaxPairXor(a));
        sc.close();
    }
}
