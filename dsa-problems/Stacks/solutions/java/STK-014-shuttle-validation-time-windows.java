import java.util.*;

class Solution {
    public boolean validate(int[] push, long[] pushT, int[] pop, long[] popT, Map<Integer, Long> windows, Set<Integer> priority) {
        int n = push.length;
        Stack<Integer> stack = new Stack<>();
        Stack<Long> timeStack = new Stack<>();
        Stack<Integer> minPriorityStack = new Stack<>();
        
        int j = 0;
        for (int i = 0; i < n; i++) {
            int val = push[i];
            long time = pushT[i];
            
            stack.push(val);
            timeStack.push(time);
            
            int currentMin = minPriorityStack.isEmpty() ? Integer.MAX_VALUE : minPriorityStack.peek();
            if (priority.contains(val)) {
                currentMin = Math.min(currentMin, val);
            }
            minPriorityStack.push(currentMin);
            
            while (!stack.isEmpty() && j < n && stack.peek() == pop[j]) {
                int poppedVal = stack.pop();
                long pushedTime = timeStack.pop();
                minPriorityStack.pop(); // Remove current state
                
                long poppedTime = popT[j];
                
                // Check 1: Time Window
                if (windows.containsKey(poppedVal)) {
                    if (poppedTime - pushedTime > windows.get(poppedVal)) {
                        return false;
                    }
                }
                
                // Check 2: Priority
                // If poppedVal is Non-Priority, it must not be larger than any existing Priority
                if (!priority.contains(poppedVal)) {
                    int minP = minPriorityStack.isEmpty() ? Integer.MAX_VALUE : minPriorityStack.peek();
                    if (poppedVal > minP) {
                        return false;
                    }
                }
                
                j++;
            }
        }
        
        return stack.isEmpty();
    }
}
