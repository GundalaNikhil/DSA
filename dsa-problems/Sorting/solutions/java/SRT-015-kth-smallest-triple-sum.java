import java.util.*;

class Solution {
    public long kthTripleSum(int[] arr, long k) {
        int n = arr.length;
        Arrays.sort(arr);
        
        long low = (long)arr[0] + arr[1] + arr[2];
        long high = (long)arr[n-1] + arr[n-2] + arr[n-3];
        long ans = high;
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (countLessEqual(arr, mid) >= k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
    
    private long countLessEqual(int[] arr, long target) {
        long count = 0;
        int n = arr.length;
        for (int i = 0; i < n - 2; i++) {
            // Optimization: If smallest sum starting with arr[i] > target, break
            if ((long)arr[i] + arr[i+1] + arr[i+2] > target) break;
            
            // Optimization: If largest sum starting with arr[i] <= target, add all
            if ((long)arr[i] + arr[n-2] + arr[n-1] <= target) {
                long remaining = n - 1 - i;
                count += remaining * (remaining - 1) / 2;
                continue;
            }
            
            long rem = target - arr[i];
            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                if (arr[l] + arr[r] <= rem) {
                    count += (r - l);
                    l++;
                } else {
                    r--;
                }
            }
        }
        return count;
    }
}
