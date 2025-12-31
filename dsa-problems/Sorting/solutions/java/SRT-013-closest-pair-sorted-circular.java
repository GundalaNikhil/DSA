import java.util.*;

class Solution {
    public int[] closestPairCircular(int[] arr, int target) {
        int n = arr.length;
        if (n == 0) return new int[]{};
        
        // Find pivot (index of minimum element)
        int pivot = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i] < arr[pivot]) {
                pivot = i;
            }
        }
        
        int l = 0;
        int r = n - 1;
        
        long minDiff = Long.MAX_VALUE;
        int res1 = -1, res2 = -1;
        
        while (l < r) {
            int pL = (pivot + l) % n;
            int pR = (pivot + r) % n;
            
            long sum = (long)arr[pL] + arr[pR];
            long diff = Math.abs(sum - target);
            
            if (diff < minDiff) {
                minDiff = diff;
                res1 = arr[pL];
                res2 = arr[pR];
            }
            
            if (sum < target) {
                l++;
            } else {
                r--;
            }
        }
        
        return new int[]{res1, res2};
    }
}
