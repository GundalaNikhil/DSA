import java.util.*;

class Solution {
    public long countSetBitsIndexedXor(int[] a) {
        long total = 0;
        for (int i = 0; i < a.length; i++) {
            // Integer.bitCount uses an efficient parallel bit counting algorithm
            total += Integer.bitCount(i ^ a[i]);
        }
        return total;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countSetBitsIndexedXor(a));
        sc.close();
    }
}
