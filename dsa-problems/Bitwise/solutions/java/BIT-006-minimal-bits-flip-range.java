import java.util.*;

class Solution {
    public long minimalBitsFlipRange(long x, long y) {
        long diff = x ^ y;
        if (diff == 0) return 0;
        
        // Check if diff is of form 111...1
        // If so, diff + 1 is a power of 2 (100...0)
        // ANDing them should be 0.
        // Also ensure diff > 0, which is handled by diff==0 check.
        // Edge case: if diff is Long.MAX_VALUE (all 1s except sign?), 
        // Logic holds for unsigned interpretation but Java uses signed.
        // For inputs up to 10^12, we are well within 63 bits, so no overflow issues.
        
        if ((diff & (diff + 1)) == 0) {
            // Count bits. Since it's all 1s, count is just population count.
            return Long.bitCount(diff);
        }
        
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long x = sc.nextLong();
        long y = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.minimalBitsFlipRange(x, y));
        sc.close();
    }
}
