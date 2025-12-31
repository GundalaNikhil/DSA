import java.util.*;

class Solution {
    public int[] kthSmallestInWindows(int[] arr, int w, int k) {
        int n = arr.length;
        int[] result = new int[n - w + 1];
        
        // Max-Heap for smallest k elements
        PriorityQueue<Integer> left = new PriorityQueue<>(Collections.reverseOrder());
        // Min-Heap for largest w-k elements
        PriorityQueue<Integer> right = new PriorityQueue<>();
        
        Map<Integer, Integer> deleted = new HashMap<>();
        
        int leftSize = 0;
        int rightSize = 0;
        
        for (int i = 0; i < n; i++) {
            // Add new element
            int val = arr[i];
            if (leftSize < k) {
                left.offer(val);
                leftSize++;
            } else {
                if (val < left.peek()) {
                    right.offer(left.poll());
                    left.offer(val);
                    // Clean left top? No, we just swapped.
                    // We must clean before peeking.
                } else {
                    right.offer(val);
                }
            }
            
            // Restart logic with explicit balance function.
        }
        
        // Reset and use cleaner approach
        left.clear(); right.clear(); deleted.clear();
        leftSize = 0; rightSize = 0;
        
        for (int i = 0; i < n; i++) {
            // ADD
            int val = arr[i];
            // Clean tops first? No, clean when needed.
            
            // Heuristic insert
            if (left.isEmpty() || val <= left.peek()) {
                left.offer(val);
                leftSize++;
            } else {
                right.offer(val);
                rightSize++;
            }
            
            // REMOVE (if window full)
            if (i >= w) {
                int out = arr[i - w];
                deleted.put(out, deleted.getOrDefault(out, 0) + 1);
                
                // Where was 'out'?
                // We can't know for sure without checking, but we know the invariant:
                // All in Left <= All in Right.
                // If out <= left.peek(), it must be in Left (or deleted from Left).
                // But what if duplicates?
                // Standard logic: If out <= left.peek(), decrement leftSize. Else rightSize.
                // BUT, we must ensure left.peek() is valid first!
                
                clean(left, deleted);
                // Now left.peek() is valid (or null)
                
                if (!left.isEmpty() && out <= left.peek()) {
                    leftSize--;
                } else {
                    rightSize--;
                }
            }
            
            // REBALANCE
            // We want leftSize == k
            
            // 1. Clean tops
            clean(left, deleted);
            clean(right, deleted);
            
            // 2. Move R -> L if L needs more
            while (leftSize < k && !right.isEmpty()) {
                clean(right, deleted); // Ensure valid
                if (right.isEmpty()) break;
                left.offer(right.poll());
                leftSize++;
                rightSize--;
                clean(left, deleted); // Ensure valid top for next checks
            }
            
            // 3. Move L -> R if L has too many
            while (leftSize > k && !left.isEmpty()) {
                clean(left, deleted);
                if (left.isEmpty()) break;
                right.offer(left.poll());
                leftSize--;
                rightSize++;
                clean(right, deleted);
            }
            
            // 4. Ensure order (L.max <= R.min)
            // This is implicitly handled by insertion logic + rebalance?
            // If we insert to L but it belongs in R?
            // Example: L=[10], R=[5]. k=1.
            // L has 10. R has 5.
            // We need to swap.
            // Check: if !L.empty && !R.empty && L.peek > R.peek
            while (!left.isEmpty() && !right.isEmpty() && left.peek() > right.peek()) {
                int l = left.poll();
                int r = right.poll();
                left.offer(r);
                right.offer(l);
                clean(left, deleted);
                clean(right, deleted);
            }
            
            // Record result
            if (i >= w - 1) {
                clean(left, deleted);
                result[i - w + 1] = left.peek();
            }
        }
        
        return result;
    }
    
    private void clean(PriorityQueue<Integer> pq, Map<Integer, Integer> deleted) {
        while (!pq.isEmpty() && deleted.getOrDefault(pq.peek(), 0) > 0) {
            int val = pq.poll();
            deleted.put(val, deleted.get(val) - 1);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int w = sc.nextInt();
            int k = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            int[] result = solution.kthSmallestInWindows(arr, w, k);
            for (int i = 0; i < result.length; i++) {
                System.out.print(result[i]);
                if (i < result.length - 1) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
