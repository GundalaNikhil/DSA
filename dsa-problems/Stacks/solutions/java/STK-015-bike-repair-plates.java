import java.util.*;

class Solution {
    public int countUnsafe(int[] d) {
        int unsafeCount = 0;
        for (int i = 0; i < d.length - 1; i++) {
            if (d[i] < d[i+1]) {
                unsafeCount++;
            }
        }
        return unsafeCount;
    }
}
