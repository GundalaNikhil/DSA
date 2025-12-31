import java.util.*;

class Solution {
    public boolean exactCountSubsetSum(int[] arr, int target, int k) {
        if (k == 0) return target == 0;
        if (target < 0) return false;
        int words = (target >> 6) + 1; // 64-bit words
        long[][] bits = new long[k + 1][words];
        bits[0][0] = 1L; // sum 0 reachable with 0 items

        for (int x : arr) {
            if (x > target) {
                // shifting by x would push all bits beyond target; still must process (as it affects counts) but no sums <= target will be added
            }
            for (int cnt = k; cnt >= 1; cnt--) {
                orShiftLeft(bits[cnt], bits[cnt - 1], x, target);
            }
        }

        return getBit(bits[k], target);
    }

    private static boolean getBit(long[] a, int pos) {
        int w = pos >> 6;
        int b = pos & 63;
        return ((a[w] >>> b) & 1L) != 0;
    }

    private static void setOr(long[] dst, long[] src) {
        for (int i = 0; i < dst.length; i++) dst[i] |= src[i];
    }

    private static void orShiftLeft(long[] dst, long[] src, int shift, int target) {
        if (shift == 0) {
            setOr(dst, src);
            return;
        }

        int wordShift = shift >> 6;
        int bitShift = shift & 63;
        int maxWord = target >> 6;

        long[] shifted = new long[dst.length];

        for (int i = 0; i <= maxWord; i++) {
            long val = src[i];
            if (val == 0) continue;
            int j = i + wordShift;
            if (j > maxWord) continue;
            shifted[j] |= (val << bitShift);
            if (bitShift != 0 && j + 1 <= maxWord) {
                shifted[j + 1] |= (val >>> (64 - bitShift));
            }
        }

        // Mask out bits beyond target in the last word
        int lastBits = (target & 63);
        if (lastBits != 63) {
            long mask = (1L << (lastBits + 1)) - 1L;
            shifted[maxWord] &= mask;
        }

        setOr(dst, shifted);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int target = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        System.out.println(new Solution().exactCountSubsetSum(arr, target, k) ? "true" : "false");
        sc.close();
    }
}
