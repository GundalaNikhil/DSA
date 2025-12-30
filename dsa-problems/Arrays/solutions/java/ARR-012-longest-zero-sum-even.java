import java.util.*;

class Solution {
    public int longestZeroSumEvenLength(int[] arr) {
        // Map: Sum -> int array of size 2. [0] for even index, [1] for odd index.
        // Initialize with Integer.MIN_VALUE or similar to indicate "not seen"
        Map<Long, int[]> map = new HashMap<>();

        long currentSum = 0;
        int maxLen = 0;

        // Base case: Sum 0 at index -1. -1 is odd.
        map.put(0L, new int[]{Integer.MIN_VALUE, -1});

        for (int i = 0; i < arr.length; i++) {
            currentSum += arr[i];
            int parity = i & 1; // 0 for even, 1 for odd

            map.putIfAbsent(currentSum, new int[]{Integer.MIN_VALUE, Integer.MIN_VALUE});
            int[] firstSeen = map.get(currentSum);

            if (firstSeen[parity] != Integer.MIN_VALUE) {
                // Found a previous occurrence with same parity -> length is even
                int len = i - firstSeen[parity];
                if (len > maxLen) {
                    maxLen = len;
                }
            } else {
                // First time seeing this sum with this parity
                firstSeen[parity] = i;
            }
        }

        return maxLen;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.longestZeroSumEvenLength(arr);
        System.out.println(result);
        sc.close();
    }
}
