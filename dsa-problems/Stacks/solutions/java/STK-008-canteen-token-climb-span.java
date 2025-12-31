import java.util.*;

class Solution {
    public int[] spans(int[] demand) {
        int n = demand.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>(); // Stores indices
        
        for (int i = 0; i < n; i++) {
            // Find nearest previous element >= current
            // Pop elements strictly smaller
            while (!stack.isEmpty() && demand[stack.peek()] < demand[i]) {
                stack.pop();
            }
            
            int prevIdx = stack.isEmpty() ? -1 : stack.peek();
            result[i] = i - prevIdx - 1;
            
            stack.push(i);
        }
        return result;
    }
}
