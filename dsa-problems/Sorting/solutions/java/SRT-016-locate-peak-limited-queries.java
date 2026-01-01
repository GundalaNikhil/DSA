import java.util.*;

class Solution {
    public int findPeak(int[] arr, int qLimit) {
        int n = arr.length;
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 0;
        }
        if (arr[0] > arr[1]) {
            return 0;
        }
        for (int i = 1; i < n - 1; i++) {
            if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
                return i;
            }
        }
        if (arr[n - 1] > arr[n - 2]) {
            return n - 1;
        }
        return 0;
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
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.findPeak(arr, n));
        sc.close();
    }
}
