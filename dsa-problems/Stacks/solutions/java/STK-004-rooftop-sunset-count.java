import java.util.*;
import java.io.*;

class Solution {
    public int countVisible(int[] h) {
        int n = h.length;
        Stack<Integer> stack = new Stack<>();
        int count = 0;
        
        // Scan from right to left
        for (int i = n - 1; i >= 0; i--) {
            // Remove buildings shorter than current
            // These buildings are blocked by the current (taller) building to their left?
            // Wait, problem says "see sunset". Usually implies looking West (left) or East (right)?
            // Python ref: "A building can see the sunset if there is no taller building to its right."
            // Python implementation scans right to left.
            // Stack keeps decreasing height indices from right?
            // "Remove buildings shorter than current": stack stores buildings to the right.
            // If current is taller than top of stack (which is to the right), then that building on stack is blocked by something even further right? No.
            
            // Let's mirror Python Logic:
            // for i from n-1 down to 0:
            //   while stack and h[stack.peek()] < h[i]: stack.pop()
            //   if stack empty: count++ (no taller building to right)
            //   stack.push(i)
            
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
            int[] h = new int[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) {
                    h[i] = sc.nextInt();
                }
            }
            Solution sol = new Solution();
            System.out.println(sol.countVisible(h));
        }
        sc.close();
    }
}
