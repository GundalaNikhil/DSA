import java.util.*;

class Solution {
    public void sortWithFixedOnes(int[] arr) {
        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            // Advance left if it points to 1 (fixed) or 0 (sorted correctly)
            while (left < right && (arr[left] == 0 || arr[left] == 1)) {
                left++;
            }

            // Retreat right if it points to 1 (fixed) or 2 (sorted correctly)
            while (left < right && (arr[right] == 2 || arr[right] == 1)) {
                right--;
            }

            // If valid misplacement found (arr[left]==2, arr[right]==0)
            if (left < right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
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
        solution.sortWithFixedOnes(arr);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]).append(i == arr.length - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
