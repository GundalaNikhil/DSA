import java.util.*;

class Solution {
    public int[] twoUniqueWithTriplesMask(int[] a, int M) {
        // Step 1: Find a differentiating bit that is also in M
        int splitBit = -1;
        for (int i = 0; i < 31; i++) {
            // Only examine bits allowed by M
            if (((M >> i) & 1) == 0) continue;

            int count = 0;
            for (int x : a) {
                if (((x >> i) & 1) == 1) {
                    count++;
                }
            }
            // If count % 3 == 1, then the two uniques differ at this bit.
            if (count % 3 == 1) {
                splitBit = i;
                break;
            }
        }

        // If no split bit found in M, find any distinguishing bit
        if (splitBit == -1) {
            for (int i = 0; i < 31; i++) {
                int count = 0;
                for (int x : a) {
                    if (((x >> i) & 1) == 1) {
                        count++;
                    }
                }
                if (count % 3 == 1) {
                    splitBit = i;
                    break;
                }
            }
        }

        // Step 2: Reconstruct the two numbers separately
        int num1 = 0;
        int num2 = 0;

        // We can do this bit by bit for each number
        for (int i = 0; i < 31; i++) {
            int c1 = 0;
            int c2 = 0;
            for (int x : a) {
                int bitVal = (x >> i) & 1;
                // Check which group x belongs to based on splitBit
                if (((x >> splitBit) & 1) == 0) {
                    c1 += bitVal;
                } else {
                    c2 += bitVal;
                }
            }

            if (c1 % 3 == 1) num1 |= (1 << i);
            if (c2 % 3 == 1) num2 |= (1 << i);
        }

        int[] result = new int[]{num1, num2};
        Arrays.sort(result);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int M = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.twoUniqueWithTriplesMask(a, M);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
