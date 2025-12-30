import java.util.*;

class Solution {
    public int[] reverseFirstK(int[] values, int k) {
        Queue<Integer> queue = new LinkedList<>();
        for (int v : values) queue.offer(v);
        
        Stack<Integer> stack = new Stack<>();
        
        // 1. Dequeue first K and push to stack
        for (int i = 0; i < k; i++) {
            stack.push(queue.poll());
        }
        
        // 2. Pop from stack and enqueue
        while (!stack.isEmpty()) {
            queue.offer(stack.pop());
        }
        
        // 3. Rotate remaining N-K elements
        int n = values.length;
        for (int i = 0; i < n - k; i++) {
            queue.offer(queue.poll());
        }
        
        // Convert back to array
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = queue.poll();
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] values = new int[n];
            for (int i = 0; i < n; i++) {
                values[i] = sc.nextInt();
            }
            int k = sc.nextInt();
    
            Solution solution = new Solution();
            int[] result = solution.reverseFirstK(values, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
