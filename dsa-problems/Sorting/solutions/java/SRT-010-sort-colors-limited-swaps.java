import java.util.*;

class Solution {
    public boolean sortWithSwaps(int[] arr, long S) {
        int n = arr.length;
        int count0 = 0;
        int count1 = 0;
        for (int v : arr) {
            if (v == 0) count0++;
            else if (v == 1) count1++;
        }

        int misplaced = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0 && i >= count0) {
                misplaced++;
            } else if (arr[i] == 1 && (i < count0 || i >= count0 + count1)) {
                misplaced++;
            } else if (arr[i] == 2 && i < count0 + count1) {
                misplaced++;
            }
        }

        long swapsNeeded = misplaced / 2;
        return swapsNeeded <= S;
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
        long s = sc.nextLong();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        boolean ok = solution.sortWithSwaps(arr, s);
        System.out.println(ok ? "YES" : "NO");
        sc.close();
    }
}
