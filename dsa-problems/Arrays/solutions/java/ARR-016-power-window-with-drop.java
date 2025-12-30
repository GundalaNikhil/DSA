import java.util.*;

class Solution {
    public long maxWindowSumWithDrop(int[] arr, int k) {
        int n = arr.length;
        if (n < k) return 0;

        long currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += arr[i];
        }

        long maxTotal = currentSum;

        for (int i = k; i < n; i++) {
            currentSum += arr[i];
            currentSum -= arr[i - k];
            if (currentSum > maxTotal) {
                maxTotal = currentSum;
            }
        }

        return maxTotal;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        
        int k = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.maxWindowSumWithDrop(arr, k);
        System.out.println(result);
        sc.close();
    }
}
