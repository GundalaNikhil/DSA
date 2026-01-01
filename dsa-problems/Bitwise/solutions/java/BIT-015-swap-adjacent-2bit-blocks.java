import java.util.*;

class Solution {
    public long swapAdjacent2BitBlocks(long x) {
        long mask32 = 0xFFFFFFFFL;
        long val = x & mask32;

        long evenBlocks = val & 0x33333333L;
        long oddBlocks = val & 0xCCCCCCCCL;

        long res = (evenBlocks << 2) | (oddBlocks >>> 2);
        return res & mask32;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long x = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.swapAdjacent2BitBlocks(x));
        sc.close();
    }
}
