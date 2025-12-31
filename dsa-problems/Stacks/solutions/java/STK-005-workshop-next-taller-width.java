import java.util.*;

class Solution {
    public int[] nextTallerWithin(int[] h, int w) {
        int n = h.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>(); // Stores indices
        
        for (int i = n - 1; i >= 0; i--) {
            // Maintain monotonic decreasing property (heights in stack are increasing)
            while (!stack.isEmpty() && h[stack.peek()] <= h[i]) {
                stack.pop();
            }
            
            if (stack.isEmpty()) {
                result[i] = -1;
            } else {
                int j = stack.peek();
                if (j - i <= w) {
                    result[i] = h[j];
                } else {
                    result[i] = -1;
                }
            }
            
            stack.push(i);
        }
        
        return result;
    }
}
