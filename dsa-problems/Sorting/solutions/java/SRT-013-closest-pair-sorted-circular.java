import java.util.*;

class Solution {
    public int[] closestPairCircular(int[] arr, int target) {
        int n = arr.length;
        if (n == 0) {
            return new int[0];
        }
        if (n == 1) {
            return new int[]{0, 0};
        }

        int minIdx = 0;
        int minDiff = Math.abs(arr[0] - arr[1]);
        for (int i = 0; i < n; i++) {
            int next = (i + 1) % n;
            int diff = Math.abs(arr[i] - arr[next]);
            if (diff < minDiff) {
                minDiff = diff;
                minIdx = i;
            }
        }

        int a = minIdx;
        int b = (minIdx + 1) % n;
        if (a > b) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        return new int[]{a, b};
    }
}
