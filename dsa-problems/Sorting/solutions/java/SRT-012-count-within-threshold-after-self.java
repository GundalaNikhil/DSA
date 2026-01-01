import java.util.*;

class Solution {
    public long[] countWithinThreshold(int[] arr, long T) {
        int n = arr.length;
        long[] counts = new long[n];

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((long)arr[j] - (long)arr[i] <= T) {
                    counts[i]++;
                }
            }
        }

        return counts;
    }
}
