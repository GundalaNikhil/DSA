import java.util.*;

class Solution {
    public int[] mergeWithPriority(int[] A, int[] B) {
        int n = A.length;
        int m = B.length;
        int[] result = new int[n + m];

        int i = 0, j = 0, k = 0;

        while (i < n && j < m) {
            // Priority to A on tie: use <=
            if (A[i] <= B[j]) {
                result[k++] = A[i++];
            } else {
                result[k++] = B[j++];
            }
        }

        while (i < n) {
            result[k++] = A[i++];
        }

        while (j < m) {
            result[k++] = B[j++];
        }

        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextInt();

        int m = sc.nextInt();
        int[] B = new int[m];
        for (int i = 0; i < m; i++) B[i] = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.mergeWithPriority(A, B);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]).append(i == result.length - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
