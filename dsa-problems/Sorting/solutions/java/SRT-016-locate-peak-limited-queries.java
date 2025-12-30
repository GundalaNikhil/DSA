import java.util.*;

class Solution {
    public int findPeak(int[] arr, int qLimit) {
        int n = arr.length;
        int low = 0;
        int high = n - 1;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            // We access mid and mid+1.
            // Since low < high, mid is at least 0 and at most n-2.
            // So mid+1 is valid.
            if (arr[mid] < arr[mid+1]) {
                // Rising slope, peak must be to the right
                low = mid + 1;
            } else {
                // Falling slope or peak, peak is at mid or left
                high = mid;
            }
        }
        return low;
    }
}
