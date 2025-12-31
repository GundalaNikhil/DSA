import java.util.*;

class Solution {
    public int weightedBalancePoint(int[] a, int L, int R) {
        long totalSum = 0;
        for (int x : a) {
            totalSum += x;
        }

        long leftSum = 0;
        long L_long = L; // Use long for multiplication
        long R_long = R;

        for (int i = 0; i < a.length; i++) {
            // Right sum is total minus (left part + current element)
            long rightSum = totalSum - leftSum - a[i];

            if (leftSum * L_long == rightSum * R_long) {
                return i;
            }

            leftSum += a[i];
        }

        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;

        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();

        int L = sc.nextInt();
        int R = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.weightedBalancePoint(a, L, R));
        sc.close();
    }
}
