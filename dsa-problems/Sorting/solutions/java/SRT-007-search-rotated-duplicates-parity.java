import java.util.*;

class Solution {
    public int countEvenIndices(int[] arr, int x) {
        int n = arr.length;
        int pivot = findPivot(arr, 0, n - 1);
        
        int count = 0;
        // Search in left part [0, pivot-1]
        if (pivot > 0) {
            int[] range = searchRange(arr, 0, pivot - 1, x);
            if (range[0] != -1) {
                count += countEvens(range[0], range[1]);
            }
        }
        
        // Search in right part [pivot, n-1]
        int[] range = searchRange(arr, pivot, n - 1, x);
        if (range[0] != -1) {
            count += countEvens(range[0], range[1]);
        }
        
        return count;
    }
    
    private int findPivot(int[] arr, int low, int high) {
        // Returns index of minimum element
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] > arr[high]) {
                low = mid + 1;
            } else if (arr[mid] < arr[high]) {
                high = mid;
            } else {
                // Duplicates: worst case O(N)
                high--;
            }
        }
        return low;
    }
    
    private int[] searchRange(int[] arr, int low, int high, int target) {
        int start = -1, end = -1;
        
        // Find first
        int l = low, r = high;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] >= target) {
                if (arr[mid] == target) start = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        
        if (start == -1) return new int[]{-1, -1};
        
        // Find last
        l = low; r = high;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] <= target) {
                if (arr[mid] == target) end = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        return new int[]{start, end};
    }
    
    private int countEvens(int L, int R) {
        if (L > R) return 0;
        int len = R - L + 1;
        if (len % 2 == 0) return len / 2;
        return (L % 2 == 0) ? (len + 1) / 2 : (len - 1) / 2;
    }
}
