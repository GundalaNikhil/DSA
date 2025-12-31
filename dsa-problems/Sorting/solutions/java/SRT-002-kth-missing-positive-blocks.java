import java.util.*;

class Solution {
    public long[] solve(int[] arr, long[][] queries) {
        int n = arr.length;
        long[] results = new long[queries.length];
        
        for (int i = 0; i < queries.length; i++) {
            long k = queries[i][0];
            long b = queries[i][1];
            long m = k * b;
            
            // Binary search for largest idx such that arr[idx] - (idx + 1) < m
            int low = 0, high = n - 1;
            int idx = -1;
            
            while (low <= high) {
                int mid = low + (high - low) / 2;
                long missingCount = arr[mid] - (mid + 1);
                if (missingCount < m) {
                    idx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            
            results[i] = m + idx + 1;
        }
        return results;
    }
}
