import java.util.*;

class Solution {
    long MOD = 1000000007L;

    public long eval(List<String> tokens, Map<String, Long> vars) {
        Stack<Long> stack = new Stack<>();
        
        for (String token : tokens) {
            if (vars.containsKey(token)) {
                stack.push(vars.get(token) % MOD);
            } else if (isNumber(token)) {
                stack.push(Long.parseLong(token) % MOD);
            } else if (token.equals("DUP")) {
                stack.push(stack.peek());
            } else if (token.equals("SWAP")) {
                long a = stack.pop();
                long b = stack.pop();
                stack.push(a);
                stack.push(b);
            } else {
                long b = stack.pop();
                long a = stack.pop();
                long res = 0;
                
                switch (token) {
                    case "+": res = (a + b) % MOD; break;
                    case "-": res = (a - b + MOD) % MOD; break;
                    case "*": res = (a * b) % MOD; break;
                    case "/": res = a / b; break; // Integer division as per problem
                    case "%": res = a % b; break;
                }
                stack.push(res);
            }
        }
        return stack.pop();
    }
    
    private boolean isNumber(String s) {
        try {
            Long.parseLong(s);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}
