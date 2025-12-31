import java.util.*;

class Solution {
    public boolean canRepair(String s) {
        int n = s.length();
        if (n % 2 != 0) return false;
        
        Stack<Integer> leftStack = new Stack<>();
        Stack<Integer> starStack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            
            if (c == '(' || c == '[' || c == '{') {
                leftStack.push(i);
            } else if (c == '?') {
                starStack.push(i);
            } else {
                // Closer
                if (!leftStack.isEmpty() && isMatch(s.charAt(leftStack.peek()), c)) {
                    leftStack.pop();
                } else if (!starStack.isEmpty()) {
                    starStack.pop();
                } else {
                    return false;
                }
            }
        }
        
        while (!leftStack.isEmpty()) {
            if (starStack.isEmpty()) return false;
            if (leftStack.peek() < starStack.peek()) {
                leftStack.pop();
                starStack.pop();
            } else {
                return false;
            }
        }
        
        return starStack.size() % 2 == 0;
    }
    
    private boolean isMatch(char open, char close) {
        return (open == '(' && close == ')') ||
               (open == '[' && close == ']') ||
               (open == '{' && close == '}');
    }
}
