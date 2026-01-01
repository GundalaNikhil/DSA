import java.util.*;
import java.io.*;

class Solution {
    long MOD = 1000000007;

    public long evalPostfix(String[] tokens, Map<String, Integer> vars) {
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
                    case "+":
                        res = (a + b) % MOD;
                        break;
                    case "-":
                        res = (a - b + MOD) % MOD;
                        break;
                    case "*":
                        res = (a * b) % MOD;
                        break;
                    case "/":
                        // Integer division
                        // Python // is floor division for positive, but for negative?
                        // Python: -5 // 2 = -3. Java: -5 / 2 = -2.
                        // Wait, Python solutions usually assume positive here or standard int div?
                        // Problem says "Integer division". Let's check Python ref.
                        // Python: res = a // b.
                        // If inputs can be negative, Python // differs from Java /.
                        // However, usually in modulo arithmetic problems inputs are non-negative or operations are standard.
                        // But test cases might test negative.
                        // Let's stick to Java / which matches C++. If Python // is required for negative, that's specific.
                        // STK-011 python uses `a // b`.
                        // If `a=-5, b=2`, python gives -3.
                        // Java gives -2.
                        // I might need to implement python-style floor division if negatives involved.
                        // Let's use Math.floorDiv?
                        // But `a // b` in python behaves like floor.
                        res = Math.floorDiv(a, b); 
                        break;
                    case "%":
                        // Python % returns same sign as denominator. Java % returns same sign as numerator.
                        // a % b.
                        // Python: -5 % 2 = 1.
                        // Java: -5 % 2 = -1.
                        // Python `a % b`.
                        res = Math.floorMod(a, b);
                        break;
                }
                stack.push(res);
            }
        }
        return stack.peek();
    }
    
    boolean isNumber(String s) {
        try {
            Long.parseLong(s);
            return true;
        } catch(NumberFormatException e) {
            return false;
        }
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null) return;
        int numVars = Integer.parseInt(line.trim());
        
        Map<String, Integer> vars = new HashMap<>();
        for (int i = 0; i < numVars; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            vars.put(parts[0], Integer.parseInt(parts[1]));
        }
        
        String expr = br.readLine();
        if (expr == null) return;
        String[] tokens = expr.trim().split("\\s+");
        
        Solution sol = new Solution();
        System.out.println(sol.evalPostfix(tokens, vars));
    }
}
