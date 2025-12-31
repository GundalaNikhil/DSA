import java.util.*;

class Solution {
    public String weightedMedian(int[] A, int[] B, long wA, long wB) {
        long n = A.length;
        long m = B.length;
        long total = n * wA + m * wB;
        
        if (total % 2 == 1) {
            long val = findKth(A, B, wA, wB, total / 2);
            return String.valueOf(val);
        } else {
            long val1 = findKth(A, B, wA, wB, total / 2 - 1);
            long val2 = findKth(A, B, wA, wB, total / 2);
            if ((val1 + val2) % 2 == 0) {
                return String.valueOf((val1 + val2) / 2);
            } else {
                return (val1 + val2) / 2 + ".5";
            }
        }
    }
    
    private long findKth(int[] A, int[] B, long wA, long wB, long k) {
        long low = -2000000000L; // Sufficiently small
        long high = 2000000000L; // Sufficiently large
        long ans = high;
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (countLessEqual(A, B, wA, wB, mid) > k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
    
    private long countLessEqual(int[] A, int[] B, long wA, long wB, long val) {
        long count = 0;
        count += upperBound(A, val) * wA;
        count += upperBound(B, val) * wB;
        return count;
    }
    
    private int upperBound(int[] arr, long val) {
        int l = 0, r = arr.length - 1;
        int res = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] <= val) {
                res = mid + 1;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return res;
    }
}
