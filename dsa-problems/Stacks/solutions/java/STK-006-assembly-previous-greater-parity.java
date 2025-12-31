import java.util.*;

class Solution {
    public int[] prevGreaterOppositeParity(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        
        // Stacks store indices
        List<Integer> evenStack = new ArrayList<>();
        List<Integer> oddStack = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            int val = arr[i];
            
            if (val % 2 == 0) {
                // Current is Even, look in Odd Stack
                int idx = findNearestGreater(oddStack, arr, val);
                if (idx != -1) result[i] = arr[idx];
                
                // Update Even Stack
                while (!evenStack.isEmpty() && arr[evenStack.get(evenStack.size() - 1)] <= val) {
                    evenStack.remove(evenStack.size() - 1);
                }
                evenStack.add(i);
            } else {
                // Current is Odd, look in Even Stack
                int idx = findNearestGreater(evenStack, arr, val);
                if (idx != -1) result[i] = arr[idx];
                
                // Update Odd Stack
                while (!oddStack.isEmpty() && arr[oddStack.get(oddStack.size() - 1)] <= val) {
                    oddStack.remove(oddStack.size() - 1);
                }
                oddStack.add(i);
            }
        }
        return result;
    }
    
    // Find the index in stack closest to the end (top) where arr[stack[k]] > val
    // Stack values are decreasing. We want the smallest stack value > val.
    // This corresponds to the rightmost valid element in the list.
    private int findNearestGreater(List<Integer> stack, int[] arr, int val) {
        if (stack.isEmpty()) return -1;
        
        int l = 0, r = stack.size() - 1;
        int ansIdx = -1;
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[stack.get(mid)] > val) {
                ansIdx = stack.get(mid);
                l = mid + 1; // Try to find a closer one (further right in stack)
            } else {
                r = mid - 1; // Too small, go left (larger values)
            }
        }
        return ansIdx;
    }
}
