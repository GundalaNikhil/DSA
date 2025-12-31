import java.util.*;

class Solution {
    public int longestAfterChange(int[] arr) {
        int n = arr.length;
        if (n <= 1) return n;
        
        int[] L = new int[n];
        int[] R = new int[n];
        
        // Compute L
        L[0] = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i] > arr[i-1]) L[i] = L[i-1] + 1;
            else L[i] = 1;
        }
        
        // Compute R
        R[n-1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] < arr[i+1]) R[i] = R[i+1] + 1;
            else R[i] = 1;
        }
        
        int maxLen = 1;
        // Check original max (optional, covered by logic below usually)
        for (int len : L) maxLen = Math.max(maxLen, len);
        
        for (int i = 0; i < n; i++) {
            // Change arr[i]
            
            // Connect to left only
            if (i > 0) maxLen = Math.max(maxLen, L[i-1] + 1);
            
            // Connect to right only
            if (i < n - 1) maxLen = Math.max(maxLen, R[i+1] + 1);
            
            // Connect both
            if (i > 0 && i < n - 1 && (long)arr[i+1] - arr[i-1] >= 2) {
                maxLen = Math.max(maxLen, L[i-1] + 1 + R[i+1]);
            }
        }
        
        return maxLen;
    }
}
