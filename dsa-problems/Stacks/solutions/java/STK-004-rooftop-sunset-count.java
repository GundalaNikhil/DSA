import java.util.*;

class Solution {
    public int countVisible(int[] h) {
        int count = 0;
        int maxH = -1; // Assuming heights are non-negative
        
        for (int height : h) {
            if (height > maxH) {
                count++;
                maxH = height;
            }
        }
        return count;
    }
}
