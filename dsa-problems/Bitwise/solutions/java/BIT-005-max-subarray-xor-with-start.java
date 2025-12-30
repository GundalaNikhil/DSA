import java.util.*;

class Solution {
    public long maxSubarrayXorWithStart(int[] a, int s) {
        long currentXor = 0;
        long maxXor = 0; // Or Long.MIN_VALUE, but XOR is >= 0
        
        // Subarray must contain at least a[s]
        boolean first = true;
        
        for (int i = s; i < a.length; i++) {
            currentXor ^= a[i];
            if (first) {
                maxXor = currentXor;
                first = false;
            } else {
                maxXor = Math.max(maxXor, currentXor);
            }
        }
        
        return maxXor;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int s = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maxSubarrayXorWithStart(a, s));
        sc.close();
    }
}
