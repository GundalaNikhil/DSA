import java.util.*;

class Solution {
    public long minSwapsToSort(int[] arr) {
        int n = arr.length;
        // Store (value, original_index)
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = arr[i];
            pairs[i][1] = i;
        }
        
        // Sort to find correct positions
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[0], b[0]));
        
        boolean[] visited = new boolean[n];
        long swaps = 0;
        
        for (int i = 0; i < n; i++) {
            if (visited[i] || pairs[i][1] == i) {
                continue;
            }
            
            int cycleSize = 0;
            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                // Move to the index where the element at j currently is
                // No. pairs is sorted.
                // pairs[i] is the element that belongs at index i.
                // Its current position is pairs[i].original_index.
                // So we have a mapping: position i needs element from pairs[i].original_index.
                // This defines a permutation.
                
                j = pairs[j][1];
                cycleSize++;
            }
            
            if (cycleSize > 0) {
                swaps += (cycleSize - 1);
            }
        }
        
        return swaps;
    }
}
