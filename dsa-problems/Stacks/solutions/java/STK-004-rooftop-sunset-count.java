import java.util.*;
import java.io.*;

class Solution {
    public int countVisible(long[] h) {
        int n = h.length;
        Stack<Integer> stack = new Stack<>();
        int count = 0;
        
        // Scan from right to left
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && h[stack.peek()] < h[i]) {
                stack.pop();
            }
            
            if (stack.isEmpty()) {
                count++;
            }
            
            stack.push(i);
        }
        return count;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            long[] h = new long[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextLong()) {
                    h[i] = sc.nextLong();
                }
            }
            Solution sol = new Solution();
            System.out.println(sol.countVisible(h));
        }
        sc.close();
    }
}
