import java.util.*;

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
