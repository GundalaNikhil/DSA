import java.util.*;
import java.io.*;

class Solution {
    Map<Character, Integer> prec = new HashMap<>();
    
    public Solution() {
        prec.put('+', 1); prec.put('-', 1);
        prec.put('*', 2); prec.put('/', 2); prec.put('%', 2);
        prec.put('^', 3);
        prec.put('(', 0);
    }

    public String solve(String expr) {
        StringBuilder postfix = new StringBuilder();
        Stack<Character> ops = new Stack<>();
        int redundant = 0;
        
        // 0: Start, 1: Operand, 2: Operator, 3: Open, 4: Close
        int lastType = 0;
        
        for (int i = 0; i < expr.length(); i++) {
            char c = expr.charAt(i);
            
            if (Character.isLetterOrDigit(c)) {
                if (lastType == 1 || lastType == 4) return "ERROR Invalid syntax 0";
                postfix.append(c);
                lastType = 1;
            } else if (c == '(') {
                if (lastType == 1 || lastType == 4) return "ERROR Invalid syntax 0";
                ops.push(c);
                lastType = 3;
            } else if (c == ')') {
                if (lastType == 0 || lastType == 2 || lastType == 3) return "ERROR Invalid syntax 0";
                
                boolean hasOp = false;
                while (!ops.isEmpty() && ops.peek() != '(') {
                    postfix.append(ops.pop());
                    hasOp = true;
                }
                
                if (ops.isEmpty()) return "ERROR Mismatched parentheses 0";
                ops.pop(); // Pop '('
                
                if (!hasOp) {
                    redundant++;
                }
                lastType = 4;
            } else if (prec.containsKey(c)) {
                if (lastType == 0 || lastType == 2 || lastType == 3) return "ERROR Invalid syntax 0";
                
                while (!ops.isEmpty() && ops.peek() != '(' && 
                      (prec.get(ops.peek()) > prec.get(c) || 
                      (prec.get(ops.peek()).equals(prec.get(c)) && c != '^'))) {
                    postfix.append(ops.pop());
                }
                ops.push(c);
                lastType = 2;
            } else {
                return "ERROR Invalid character 0";
            }
        }
        
        if (lastType == 0 || lastType == 2 || lastType == 3) return "ERROR Invalid syntax 0";
        
        while (!ops.isEmpty()) {
            if (ops.peek() == '(') return "ERROR Mismatched parentheses 0";
            postfix.append(ops.pop());
        }
        
        return "POSTFIX " + postfix.toString() + " " + redundant;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String expr = br.readLine();
        if (expr != null) {
            Solution sol = new Solution();
            System.out.println(sol.solve(expr.trim()));
        }
    }
}
