import java.util.*;

class Solution {
    public int[] closestPair(int[] arr, int target) {
        int n = arr.length;
        int left = 0;
        int right = n - 1;
        
        long minDiff = Long.MAX_VALUE;
        int resLeft = -1;
        int resRight = -1;
        
        while (left < right) {
            long sum = (long) arr[left] + arr[right];
            long diff = Math.abs(sum - target);
            
            if (diff < minDiff) {
                minDiff = diff;
                resLeft = arr[left];
                resRight = arr[right];
            }
            // If diff is equal, we prefer smaller arr[left], which we already have
            // since left increases. So no update needed.
            
            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return new int[]{resLeft, resRight};
    }
}
