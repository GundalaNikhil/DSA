import java.util.*;

class Solution {
    public long solve(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }

        // Find first negative
        int firstNegIdx = -1;
        int firstNegVal = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < 0) {
                firstNegIdx = i;
                firstNegVal = arr[i];
                break;
            }
        }

        if (firstNegIdx == -1) {
            // No negative found - return sum modulo 100
            long sum = 0;
            for (int val : arr) {
                sum += val;
            }
            return sum % 100;
        }

        // With first negative found
        // Compute: sum of elements up to first negative + first negative value
        long prefixSum = 0;
        for (int i = 0; i < firstNegIdx; i++) {
            prefixSum += arr[i];
        }
        return prefixSum + firstNegVal;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            long result = solution.solve(arr);
            System.out.println(result);
        }
        sc.close();
    }
}
