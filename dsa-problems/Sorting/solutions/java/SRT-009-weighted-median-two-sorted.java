import java.util.*;

class Solution {
    public String weightedMedian(int[] A, int[] B, long wA, long wB) {
        int n = A.length;
        int m = B.length;
        int[] combined = new int[n + m];
        System.arraycopy(A, 0, combined, 0, n);
        System.arraycopy(B, 0, combined, n, m);
        Arrays.sort(combined);

        int len = combined.length;
        if (len % 2 == 1) {
            return String.valueOf(combined[len / 2]);
        }

        int mid1 = combined[len / 2 - 1];
        int mid2 = combined[len / 2];
        int avg = (mid1 + mid2) / 2;
        return String.valueOf(avg);
    }
}
