import java.util.*;

class Solution {
    public int[] firstNegatives(int[] values, int k) {
        int n = values.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> queue = new ArrayDeque<>(); // Stores indices
        
        int idx = 0;
        for (int i = 0; i < n; i++) {
            // Add new element if negative
            if (values[i] < 0) {
                queue.offerLast(i);
            }
            
            // Remove expired from front
            if (!queue.isEmpty() && queue.peekFirst() <= i - k) {
                queue.pollFirst();
            }
            
            // Record result if window is full size
            if (i >= k - 1) {
                if (queue.isEmpty()) {
                    result[idx++] = 0;
                } else {
                    result[idx++] = values[queue.peekFirst()];
                }
            }
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] values = new int[n];
            for (int i = 0; i < n; i++) {
                values[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            int[] result = solution.firstNegatives(values, k);
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
