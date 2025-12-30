import java.util.*;

class Solution {
    public int[] zeroSlideWithLimit(int[] arr, int m) {
        int n = arr.length;
        int writeIdx = 0;

        for (int readIdx = 0; readIdx < n; readIdx++) {
            if (arr[readIdx] != 0) {
                // If needs to move (i.e., there are zeros behind/writeIdx is behind)
                if (readIdx != writeIdx) {
                    if (m <= 0) break; // Limit reached

                    // Swap
                    int temp = arr[writeIdx];
                    arr[writeIdx] = arr[readIdx];
                    arr[readIdx] = temp;

                    m--;
                }
                writeIdx++;
            }
        }
        return arr;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int m = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.zeroSlideWithLimit(arr, m);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
