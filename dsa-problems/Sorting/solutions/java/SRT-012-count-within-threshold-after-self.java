import java.util.*;

class Solution {
    private long[] counts;
    
    private class Pair {
        int val;
        int idx;
        Pair(int val, int idx) {
            this.val = val;
            this.idx = idx;
        }
    }
    
    public long[] countWithinThreshold(int[] arr, long T) {
        int n = arr.length;
        counts = new long[n];
        Pair[] pairs = new Pair[n];
        for (int i = 0; i < n; i++) {
            pairs[i] = new Pair(arr[i], i);
        }
        
        mergeSort(pairs, T);
        return counts;
    }
    
    private Pair[] mergeSort(Pair[] arr, long T) {
        int n = arr.length;
        if (n <= 1) return arr;
        
        int mid = n / 2;
        Pair[] left = mergeSort(Arrays.copyOfRange(arr, 0, mid), T);
        Pair[] right = mergeSort(Arrays.copyOfRange(arr, mid, n), T);
        
        // Count step
        int q = 0;
        for (int p = 0; p < left.length; p++) {
            // We want count of right[q] >= left[p].val - T
            // Since right is sorted ascending, we skip elements < left[p].val - T
            long threshold = (long)left[p].val - T;
            while (q < right.length && right[q].val < threshold) {
                q++;
            }
            counts[left[p].idx] += (right.length - q);
        }
        
        // Merge step
        return merge(left, right);
    }
    
    private Pair[] merge(Pair[] left, Pair[] right) {
        Pair[] res = new Pair[left.length + right.length];
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i].val <= right[j].val) {
                res[k++] = left[i++];
            } else {
                res[k++] = right[j++];
            }
        }
        while (i < left.length) res[k++] = left[i++];
        while (j < right.length) res[k++] = right[j++];
        return res;
    }
}
