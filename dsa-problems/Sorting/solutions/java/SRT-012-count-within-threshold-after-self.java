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

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        long t = sc.nextLong();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        long[] result = solution.countWithinThreshold(arr, t);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
