import java.util.*;

class Solution {
    public int[] prefixAverages(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        long sum = 0;  // Use long to prevent overflow

        for (int i = 0; i < n; i++) {
            sum += arr[i];
            result[i] = (int)(sum / (i + 1));  // Integer division
        }

        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.prefixAverages(arr);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
