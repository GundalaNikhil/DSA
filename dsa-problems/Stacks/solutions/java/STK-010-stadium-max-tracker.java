import java.util.*;

class Solution {
    public List<String> process(List<String[]> ops) {
        List<String> result = new ArrayList<>();
        Stack<Integer> mainStack = new Stack<>();
        Stack<Integer> maxStack = new Stack<>();
        
        for (String[] op : ops) {
            String cmd = op[0];
            
            if (cmd.equals("PUSH")) {
                int val = Integer.parseInt(op[1]);
                mainStack.push(val);
                if (maxStack.isEmpty() || val >= maxStack.peek()) {
                    maxStack.push(val);
                }
            } else if (cmd.equals("POP")) {
                if (mainStack.isEmpty()) {
                    result.add("EMPTY");
                } else {
                    int val = mainStack.pop();
                    result.add(String.valueOf(val));
                    if (val == maxStack.peek()) {
                        maxStack.pop();
                    }
                }
            } else if (cmd.equals("TOP")) {
                if (mainStack.isEmpty()) {
                    result.add("EMPTY");
                } else {
                    result.add(String.valueOf(mainStack.peek()));
                }
            } else if (cmd.equals("GETMAX")) {
                if (mainStack.isEmpty()) {
                    result.add("EMPTY");
                } else {
                    result.add(String.valueOf(maxStack.peek()));
                }
            }
        }
        return result;
    }
}
