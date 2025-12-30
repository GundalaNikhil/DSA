import java.util.*;

class Solution {
    public boolean hasPairWithForbidden(int[] arr, int target, Set<Integer> forbidden) {
        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            // Skip forbidden indices
            if (forbidden.contains(left)) {
                left++;
                continue;
            }
            if (forbidden.contains(right)) {
                right--;
                continue;
            }

            // Standard 2-Sum Logic
            long sum = (long)arr[left] + arr[right];

            if (sum == target) {
                return true;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        int target = sc.nextInt();
        int f = sc.nextInt();
        Set<Integer> forbidden = new HashSet<>();
        for (int i = 0; i < f; i++) forbidden.add(sc.nextInt());

        Solution solution = new Solution();
        boolean result = solution.hasPairWithForbidden(arr, target, forbidden);
        System.out.println(result ? "true" : "false");
        sc.close();
    }
}
