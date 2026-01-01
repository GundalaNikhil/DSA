import java.util.*;

class Solution {
    public String intervalRemovalGame(int n, int[][] intervals) {
        long xorSum = 0;
        for (int[] interval : intervals) {
            long len = (long) interval[1] - interval[0];
            xorSum ^= len;
        }
        return xorSum > 0 ? "First" : "Second";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[][] intervals = new int[n][2];
            for (int i = 0; i < n; i++) {
                intervals[i][0] = sc.nextInt();
                intervals[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.intervalRemovalGame(n, intervals));
        }
        sc.close();
    }
}
