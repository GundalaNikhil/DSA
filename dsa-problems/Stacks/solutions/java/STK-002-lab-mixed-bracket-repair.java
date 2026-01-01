import java.util.*;
import java.io.*;

class Solution {
    public int countChanges(String s) {
        Stack<Character> stack = new Stack<>();
        String opens = "([{";
        String closes = ")]}";
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put(')', '(');
        pairs.put(']', '[');
        pairs.put('}', '{');
        
        for (char c : s.toCharArray()) {
            if (opens.indexOf(c) != -1) {
                stack.push(c);
            } else if (closes.indexOf(c) != -1) {
                if (!stack.isEmpty() && stack.peek() == pairs.get(c)) {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            } else if (c == '?') {
                stack.push('(');
            }
        }
        
        return stack.size();
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line);
        }
        String s = sb.toString().trim();
        
        if (s.isEmpty()) {
            System.out.println(0);
            return;
        }

        Solution sol = new Solution();
        System.out.println(sol.countChanges(s));
    }
}
