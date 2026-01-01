import java.util.*;

class Solution {
    public int[][] swapQueues(int[] q1, int[] q2) {
        return new int[][]{q2, q1};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] q1 = new int[n];
            int[] q2 = new int[n];
            for (int i = 0; i < n; i++) q1[i] = sc.nextInt();
            for (int i = 0; i < n; i++) q2[i] = sc.nextInt();
            
            Solution sol = new Solution();
            int[][] result = sol.swapQueues(q1, q2);
            for (int j = 0; j < 2; j++) {
                for (int i = 0; i < n; i++) {
                    if (i > 0) System.out.print(" ");
                    System.out.print(result[j][i]);
                }
                System.out.println();
            }
        }
    }
}
