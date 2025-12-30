import java.util.*;

class Solution {
    public int countLeaves(int n, int[] left, int[] right) {
        if (n == 0) return 0;
        // Iterative approach since we have the array
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] == -1 && right[i] == -1) {
                count++;
            }
        }
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            int val = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.countLeaves(n, left, right));
        sc.close();
    }
}
