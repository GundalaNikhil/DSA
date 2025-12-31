import java.util.*;

class Solution {
    public long swapAdjacent2BitBlocks(int x) {
        // Use logical right shift >>> to handle sign bit correctly for 32-bit int
        // Mask 0x33333333 gets blocks 0, 2, 4... (0011 0011 ...)
        // Mask 0xCCCCCCCC gets blocks 1, 3, 5... (1100 1100 ...)
        
        int evenBlocks = x & 0x33333333;
        int oddBlocks = x & 0xCCCCCCCC;
        
        // Move even blocks LEFT to odd positions
        // Move odd blocks RIGHT to even positions
        int res = (evenBlocks << 2) | (oddBlocks >>> 2);
        
        // Return as long to treat as unsigned value if necessary, though problem implies 32-bit swap
        return Integer.toUnsignedLong(res);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int x = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.swapAdjacent2BitBlocks(x));
        sc.close();
    }
}
