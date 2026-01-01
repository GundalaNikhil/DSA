import java.util.*;
import java.io.*;

class Solution {
    class Item {
        char c;
        int w;
        Item(char c, int w) {
            this.c = c;
            this.w = w;
        }
    }

    public String[] reduce(String s, int[] w) {
        Stack<Item> stack = new Stack<>();
        long totalRemoved = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            int currentWeight = w[i];
            
            if (!stack.isEmpty() && stack.peek().c == currentChar && (stack.peek().w + currentWeight) % 2 == 0) {
                totalRemoved += stack.peek().w + currentWeight;
                stack.pop();
            } else {
                stack.push(new Item(currentChar, currentWeight));
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (Item item : stack) {
            sb.append(item.c);
        }
        
        return new String[]{sb.toString(), String.valueOf(totalRemoved)};
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        // Fast I/O
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        
        try {
            int n = Integer.parseInt(line.trim());
            StringBuilder sBuilder = new StringBuilder();
            int[] w = new int[n];
            
            for (int i = 0; i < n; i++) {
                String[] parts = br.readLine().trim().split("\\s+");
                sBuilder.append(parts[0]);
                w[i] = Integer.parseInt(parts[1]);
            }
            
            Solution sol = new Solution();
            String[] res = sol.reduce(sBuilder.toString(), w);
            
            if (res[0].isEmpty()) {
                System.out.println("EMPTY " + res[1]);
            } else {
                System.out.println(res[0] + " " + res[1]);
            }
        } catch (NumberFormatException e) {
            return;
        }
    }
}
