import java.util.*;

class Solution {
    public String takeOrSplit(int n, int[] heaps) {
        long xorSum = 0;
        for (int x : heaps) {
            xorSum ^= (x - 1);
        }
        return xorSum > 0 ? "First" : "Second";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] heaps = new int[n];
            for (int i = 0; i < n; i++) {
                heaps[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.takeOrSplit(n, heaps));
        }
        sc.close();
    }
}
