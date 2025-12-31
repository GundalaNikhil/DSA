import java.util.*;

class Solution {
    public List<String> process(List<String[]> ops) {
        List<String> result = new ArrayList<>();
        Stack<String> stack = new Stack<>();
        
        for (String[] op : ops) {
            String command = op[0];
            
            if (command.equals("PUSH")) {
                stack.push(op[1]);
            } else if (command.equals("POP")) {
                if (stack.isEmpty()) {
                    result.add("EMPTY");
                } else {
                    result.add(stack.pop());
                }
            } else if (command.equals("TOP")) {
                if (stack.isEmpty()) {
                    result.add("EMPTY");
                } else {
                    result.add(stack.peek());
                }
            }
        }
        return result;
    }
}
