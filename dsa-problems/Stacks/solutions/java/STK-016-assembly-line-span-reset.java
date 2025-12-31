import java.util.*;

class Solution {
    public int[] spans(int[] counts) {
        int n = counts.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && counts[stack.peek()] < counts[i]) {
                stack.pop();
            }
            
            if (stack.isEmpty()) {
                result[i] = i + 1;
            } else {
                result[i] = i - stack.peek();
            }
            
            stack.push(i);
        }
        return result;
    }
}
