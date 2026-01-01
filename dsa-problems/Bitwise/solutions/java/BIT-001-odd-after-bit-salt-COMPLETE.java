import java.util.*;

class Solution {
    public long oddAfterBitSalt(int[] a, int salt) {
        long result = 0;
        // In Java, XOR works fine on ints.
        // We accumulate the XOR of (a[i] ^ salt)
        for (int x : a) {
            result ^= (x ^ salt);
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int salt = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.oddAfterBitSalt(a, salt));
        sc.close();
    }
}
