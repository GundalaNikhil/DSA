import java.util.*;

class Solution {
    public long minSwapsToSort(int[] arr, int k) {
        int n = arr.length;
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = arr[i];
            pairs[i][1] = i;
        }

        Arrays.sort(pairs, (a, b) -> Integer.compare(a[0], b[0]));

        long violations = 0;
        for (int targetIdx = 0; targetIdx < n; targetIdx++) {
            int originalIdx = pairs[targetIdx][1];
            if (Math.abs(targetIdx - originalIdx) > k) {
                violations++;
            }
        }

        return violations / 2;
    }

    public long minSwapsToSort(int[] arr) {
        return minSwapsToSort(arr, 0);
    }
}
