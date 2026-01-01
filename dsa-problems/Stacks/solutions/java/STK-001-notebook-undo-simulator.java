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

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        List<String[]> ops = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String op = sc.next();
            if (op.equals("PUSH")) {
                ops.add(new String[]{op, sc.next()});
            } else {
                ops.add(new String[]{op});
            }
        }

        Solution solution = new Solution();
        List<String> out = solution.process(ops);
        for (String s : out) System.out.println(s);
        sc.close();
    }
}
